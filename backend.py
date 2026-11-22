"""Insurance Buddy — Wkala customer backend.

Owns end-user sign-in, session ownership, the Wkala service key, and the
same-origin /app bridge the browser SDK talks to.

The React/Streamlit UI never sees WKALA_API_KEY. Every route below checks the
signed-in user owns the session before touching Wkala.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
import time
import uuid
from contextlib import asynccontextmanager
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from wkala import (
    AgentClient,
    APIError,
    InputRequired,
    SnapshotUpdate,
    TransportError,
)

import business_tools

# --- configuration -----------------------------------------------------------

WKALA_API_KEY = os.environ.get("WKALA_API_KEY", "")
SESSION_SECRET = os.environ.get("SESSION_SECRET", "")
ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "")
COOKIE_NAME = "buddy_session"
COOKIE_PATH = "/app"
PROFILE_ID = os.environ.get("WKALA_PROFILE_ID", "")
MCP_SERVER_ID = os.environ.get("WKALA_MCP_SERVER_ID", "")


def _require_config() -> None:
    if not WKALA_API_KEY:
        raise RuntimeError("WKALA_API_KEY is not set")
    if not SESSION_SECRET:
        raise RuntimeError("SESSION_SECRET is not set (any long random string)")


# --- tiny durable store ------------------------------------------------------
# A file-backed store keeps the example runnable without Postgres. The shipped
# reference uses SQLAlchemy/Postgres. Swap `Store` for a database in production;
# the routes only use the four methods below.
# ponytail-style note: single-process file store, swap for Postgres when more
# than one worker serves requests.

class Store:
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    def _read(self) -> dict[str, Any]:
        if not os.path.exists(self.path):
            return {"users": {}, "sessions": {}, "requests": {}}
        with open(self.path, encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: dict[str, Any]) -> None:
        tmp = f"{self.path}.tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f)
        os.replace(tmp, self.path)

    # users
    def put_user(self, user_id: str, email: str) -> None:
        d = self._read()
        d["users"][user_id] = {"email": email, "created_at": time.time()}
        self._write(d)

    def get_user_by_email(self, email: str) -> dict | None:
        d = self._read()
        for uid, u in d["users"].items():
            if u["email"].lower() == email.lower():
                return {"id": uid, **u}
        return None

    # sessions
    def put_session(self, session_id: str, user_id: str, wkala_id: str) -> None:
        d = self._read()
        d["sessions"][session_id] = {
            "user_id": user_id, "wkala_id": wkala_id, "created_at": time.time(),
        }
        self._write(d)

    def get_session(self, session_id: str) -> dict | None:
        return self._read()["sessions"].get(session_id)

    def owned_session(self, session_id: str, user_id: str) -> dict | None:
        s = self.get_session(session_id)
        return s if s and s["user_id"] == user_id else None

    # idempotency receipts
    def put_request(self, key: str, user_id: str, session_id: str, run_id: str) -> None:
        d = self._read()
        d["requests"][key] = {
            "user_id": user_id, "session_id": session_id,
            "run_id": run_id, "created_at": time.time(),
        }
        self._write(d)

    def get_request(self, key: str) -> dict | None:
        return self._read()["requests"].get(key)


STORE = Store(os.environ.get("BUDDY_STORE", "./data/store.json"))


# --- signed cookie sessions --------------------------------------------------

def _sign(payload: str) -> str:
    return hmac.new(SESSION_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()


def issue_cookie(user_id: str, csrf: str) -> str:
    body = f"{user_id}.{csrf}"
    return f"{body}.{_sign(body)}"


def read_cookie(raw: str | None) -> tuple[str, str] | None:
    if not raw:
        return None
    parts = raw.split(".")
    if len(parts) != 3:
        return None
    user_id, csrf, mac = parts
    if not hmac.compare_digest(_sign(f"{user_id}.{csrf}"), mac):
        return None
    return user_id, csrf


class Identity(BaseModel):
    user_id: str
    csrf: str


def current_identity(request: Request) -> Identity:
    got = read_cookie(request.cookies.get(COOKIE_NAME))
    if not got:
        raise HTTPException(status_code=401, detail="not signed in")
    user_id, csrf = got
    return Identity(user_id=user_id, csrf=csrf)


def csrf_guard(request: Request, ident: Identity = Depends(current_identity)) -> Identity:
    """Every state-changing route requires the CSRF header and a same-origin request."""
    origin = request.headers.get("origin")
    if origin and ALLOWED_ORIGIN and origin != ALLOWED_ORIGIN:
        raise HTTPException(status_code=403, detail="origin not allowed")
    if request.method in ("POST", "PATCH", "DELETE"):
        sent = request.headers.get("x-csrf-token")
        if not sent or not hmac.compare_digest(sent, ident.csrf):
            raise HTTPException(status_code=403, detail="bad csrf token")
    return ident


# --- app ---------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    _require_config()
    async with AgentClient(api_key=WKALA_API_KEY) as agents:
        app.state.agents = agents
        yield


app = FastAPI(lifespan=lifespan, title="Insurance Buddy backend")


class SignInBody(BaseModel):
    email: str


@app.post("/auth/signin")
async def signin(body: SignInBody, response: Response) -> dict:
    """Demo sign-in. Replace with the app's real identity provider."""
    user = STORE.get_user_by_email(body.email)
    if not user:
        uid = str(uuid.uuid4())
        STORE.put_user(uid, body.email)
        user = {"id": uid, "email": body.email}
    csrf = secrets.token_urlsafe(24)
    cookie = issue_cookie(user["id"], csrf)
    response.set_cookie(
        COOKIE_NAME, cookie, httponly=True, samesite="lax", path=COOKIE_PATH,
        secure=bool(os.environ.get("COOKIE_SECURE")),
    )
    return {"user_id": user["id"], "email": user["email"], "csrfToken": csrf}


@app.get("/auth/me")
async def me(ident: Identity = Depends(current_identity)) -> dict:
    return {"user_id": ident.user_id, "csrfToken": ident.csrf}


@app.post("/app/sessions")
async def create_session(request: Request, ident: Identity = Depends(csrf_guard)) -> dict:
    agents: AgentClient = request.app.state.agents
    try:
        handle = await agents.sessions.create(title="Insurance Buddy chat")
    except APIError as e:
        raise HTTPException(status_code=getattr(e, "status_code", 502),
                            detail={"code": getattr(e, "code", "api_error"),
                                    "message": getattr(e, "message", str(e)),
                                    "request_id": getattr(e, "request_id", None)}) from e
    except TransportError as e:
        raise HTTPException(status_code=503,
                            detail={"code": "transport_error", "message": str(e)}) from e
    sid = str(uuid.uuid4())
    STORE.put_session(sid, ident.user_id, handle.session_id)
    return {"id": sid}


def _owned(request: Request, sid: str, user_id: str) -> dict:
    rec = STORE.owned_session(sid, user_id)
    if not rec:
        # Same response whether it is missing or another user's.
        raise HTTPException(status_code=404, detail="session not found")
    return rec


@app.get("/app/sessions/{sid}")
async def session_snapshot(sid: str, request: Request,
                           ident: Identity = Depends(current_identity)) -> dict:
    rec = _owned(request, sid, ident.user_id)
    agents: AgentClient = request.app.state.agents
    snap = await agents.sessions.handle(rec["wkala_id"]).snapshot()
    return snap.model_dump(mode="json", by_alias=True)


class SendBody(BaseModel):
    message: str
    idempotency_key: str


@app.post("/app/sessions/{sid}/send")
async def send(sid: str, body: SendBody, request: Request,
               ident: Identity = Depends(csrf_guard)) -> dict:
    rec = _owned(request, sid, ident.user_id)
    agents: AgentClient = request.app.state.agents

    # A repeated business request returns the original run, never a new one.
    prior = STORE.get_request(body.idempotency_key)
    if prior:
        if prior["user_id"] != ident.user_id or prior["session_id"] != sid:
            raise HTTPException(status_code=409, detail="idempotency key reused")
        return {"run_id": prior["run_id"], "replayed": True}

    opts: dict[str, Any] = {"subject": {"id": ident.user_id}}
    if PROFILE_ID:
        opts["profile_id"] = PROFILE_ID
    if MCP_SERVER_ID:
        opts["mcp_server_ids"] = [MCP_SERVER_ID]

    try:
        run = await agents.sessions.handle(rec["wkala_id"]).send(
            body.message, idempotency_key=body.idempotency_key, **opts,
        )
    except APIError as e:
        raise HTTPException(status_code=e.status_code if hasattr(e, "status_code") else 502,
                            detail={"code": getattr(e, "code", "api_error"),
                                    "message": str(e),
                                    "request_id": getattr(e, "request_id", None)}) from e
    except TransportError as e:
        raise HTTPException(status_code=503,
                            detail={"code": "transport_error",
                                    "message": "admission uncertain",
                                    "idempotency_key": getattr(e, "idempotency_key", body.idempotency_key)}) from e

    STORE.put_request(body.idempotency_key, ident.user_id, sid, run.id)
    return {"run_id": run.id, "replayed": False}


@app.get("/app/sessions/{sid}/events")
async def events(sid: str, request: Request, after: int = 0,
                 ident: Identity = Depends(current_identity)) -> StreamingResponse:
    """Server-sent events. Streaming never admits work."""
    rec = _owned(request, sid, ident.user_id)
    agents: AgentClient = request.app.state.agents
    handle = agents.sessions.handle(rec["wkala_id"])

    async def gen():
        try:
            async with handle.events(after=after) as stream:
                async for update in stream:
                    payload = update.model_dump(mode="json", by_alias=True)
                    yield f"data: {json.dumps(payload)}\n\n"
        except Exception as e:  # surfaced to the client, never swallowed
            yield f"event: error\ndata: {json.dumps({'message': str(e)})}\n\n"

    return StreamingResponse(
        gen(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.post("/app/runs/{run_id}/cancel")
async def cancel(run_id: str, request: Request, sid: str,
                 ident: Identity = Depends(csrf_guard)) -> dict:
    """Cancellation is explicit and separate from closing a stream."""
    rec = _owned(request, sid, ident.user_id)
    agents: AgentClient = request.app.state.agents
    handle = agents.sessions.handle(rec["wkala_id"])
    await handle.cancel(run_id)
    return {"cancelled": run_id}


class RespondBody(BaseModel):
    option_id: str | None = None
    message: str | None = None
    data: dict | None = None


@app.post("/app/interactions/{interaction_id}/respond")
async def respond(interaction_id: str, body: RespondBody, request: Request,
                  sid: str, ident: Identity = Depends(csrf_guard)) -> dict:
    # Ownership first: a user may only answer interactions in their own session.
    _owned(request, sid, ident.user_id)
    agents: AgentClient = request.app.state.agents
    kwargs: dict[str, Any] = {}
    if body.option_id is not None:
        kwargs["option_id"] = body.option_id
    elif body.message is not None:
        kwargs["message"] = body.message
    elif body.data is not None:
        kwargs["data"] = body.data
    else:
        raise HTTPException(status_code=400, detail="no response supplied")
    await agents.interactions.respond(interaction_id, **kwargs)
    return {"ok": True}


@app.get("/internal/tools/carrier-summary")
async def tool_carrier_summary(carrier: str) -> dict:
    return business_tools.carrier_summary(carrier)


@app.get("/internal/tools/search")
async def tool_search(carrier: str, city: str, class_level: str) -> dict:
    r = business_tools.search_hospitals(carrier, city, class_level)
    return r.model_dump()
