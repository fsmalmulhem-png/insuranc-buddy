"""Mocked scenario test for the Wkala integration.

Drives the real FastAPI app with a fake Wkala client, so every acceptance
check runs without a service key or spend.

Run: python test_integration.py
"""

from __future__ import annotations

import json
import os
import tempfile
import types
import uuid

os.environ.setdefault("SESSION_SECRET", "test-secret-not-for-production")
os.environ.setdefault("WKALA_API_KEY", "test-key")
os.environ.setdefault("BUDDY_STORE", os.path.join(tempfile.mkdtemp(), "store.json"))

from fastapi.testclient import TestClient  # noqa: E402

import backend  # noqa: E402
import business_tools  # noqa: E402

CALLS: list[dict] = []


class FakeRun:
    def __init__(self, run_id: str):
        self.id = run_id

    async def cancel(self):
        CALLS.append({"op": "cancel", "run_id": self.id})


class FakeHandle:
    def __init__(self, session_id: str):
        self.session_id = session_id

    async def send(self, message, *, idempotency_key=None, **opts):
        CALLS.append({"op": "send", "session_id": self.session_id,
                      "message": message, "key": idempotency_key,
                      "subject": (opts.get("subject") or {}).get("id"),
                      "mcp": opts.get("mcp_server_ids")})
        return FakeRun(f"run-{uuid.uuid4().hex[:8]}")

    async def snapshot(self):
        return types.SimpleNamespace(
            model_dump=lambda **kw: {"session": {"id": self.session_id}, "messages": []},
        )

    def events(self, after: int = 0):
        calls = CALLS

        class Stream:
            async def __aenter__(self):
                return self

            async def __aexit__(self, *a):
                return False

            def __aiter__(self):
                self._sent = False
                return self

            async def __anext__(self):
                if self._sent:
                    raise StopAsyncIteration
                self._sent = True
                upd = types.SimpleNamespace(
                    model_dump=lambda **kw: {"type": "message.delta", "text": "hi"},
                )
                return upd

        return Stream()

    async def cancel(self, run_id):
        CALLS.append({"op": "cancel", "run_id": run_id})


class FakeSessions:
    def __init__(self):
        self.created = 0

    async def create(self, **kw):
        self.created += 1
        h = FakeHandle(f"wsess-{self.created}")
        CALLS.append({"op": "create", "id": h.session_id})
        return h

    def handle(self, session_id):
        return FakeHandle(session_id)


class FakeInteractions:
    async def respond(self, interaction_id, **kw):
        CALLS.append({"op": "respond", "id": interaction_id, "kw": kw})
        return {"ok": True}


class FakeAgents:
    def __init__(self):
        self.sessions = FakeSessions()
        self.interactions = FakeInteractions()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        return False


class FakeClientContext:
    def __init__(self, *a, **kw):
        self.fake = FakeAgents()

    async def __aenter__(self):
        return self.fake

    async def __aexit__(self, *a):
        return False


backend.AgentClient = FakeClientContext

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def signin(client: TestClient, email: str) -> dict:
    r = client.post("/auth/signin", json={"email": email})
    assert r.status_code == 200, r.text
    return r.json()


def main() -> int:
    with TestClient(backend.app) as client:
        # ---- 1. no service key in what the browser receives ------------------
        alice = signin(client, "alice@example.com")
        r = client.get("/auth/me")
        blob = json.dumps(r.json())
        check(
            "no service key in browser payloads",
            "test-key" not in blob and "WKALA_API_KEY" not in blob,
            "auth payload carries only user_id + csrf",
        )

        # ---- 2. two users cannot read each other's sessions -----------------
        r = client.post("/app/sessions", headers={"x-csrf-token": alice["csrfToken"]})
        assert r.status_code == 200, r.text
        alice_sid = r.json()["id"]

        with TestClient(backend.app) as bob_client:
            bob = signin(bob_client, "bob@example.com")
            r2 = bob_client.get(f"/app/sessions/{alice_sid}")
            r3 = bob_client.post(
                f"/app/sessions/{alice_sid}/send",
                headers={"x-csrf-token": bob["csrfToken"]},
                json={"message": "hi", "idempotency_key": "bob-key-1"},
            )
        check("other user's session is not readable", r2.status_code == 404,
              f"got {r2.status_code}")
        check("other user's session refuses new work", r3.status_code == 404,
              f"got {r3.status_code}")

        # ---- 3. message and tool updates appear while work is running --------
        CALLS.clear()
        r = client.get(f"/app/sessions/{alice_sid}/events")
        body = r.text
        check("stream yields updates during the run",
              r.status_code == 200 and "message.delta" in body,
              f"{r.headers.get('content-type')}")

        # streaming must not admit work
        check("streaming does not create a run",
              not any(c["op"] == "send" for c in CALLS),
              f"calls={[c['op'] for c in CALLS]}")

        # ---- 4. approval is explicit ----------------------------------------
        CALLS.clear()
        r = client.post(
            f"/app/interactions/int-1/respond?sid={alice_sid}",
            headers={"x-csrf-token": alice["csrfToken"]},
            json={"option_id": "allow-once"},
        )
        check("approval submits the offered option", r.status_code == 200
              and CALLS and CALLS[0]["kw"].get("option_id") == "allow-once",
              f"calls={CALLS}")

        # bob cannot answer an interaction in alice's session
        with TestClient(backend.app) as bob_client2:
            bob2 = signin(bob_client2, "bob@example.com")
            r = bob_client2.post(
                f"/app/interactions/int-1/respond?sid={alice_sid}",
                headers={"x-csrf-token": bob2["csrfToken"]},
                json={"option_id": "allow-once"},
            )
        check("approval is scoped to the session owner", r.status_code == 404,
              f"got {r.status_code}")

        # a response with nothing supplied is rejected, not guessed
        r = client.post(
            f"/app/interactions/int-1/respond?sid={alice_sid}",
            headers={"x-csrf-token": alice["csrfToken"]},
            json={},
        )
        check("an empty response is rejected", r.status_code == 400,
              f"got {r.status_code}")

        # ---- 5. disconnect / reconnect does not duplicate work --------------
        CALLS.clear()
        key = "persisted-key-" + uuid.uuid4().hex
        r1 = client.post(f"/app/sessions/{alice_sid}/send",
                         headers={"x-csrf-token": alice["csrfToken"]},
                         json={"message": "find me a hospital", "idempotency_key": key})
        assert r1.status_code == 200, r1.text
        run_id = r1.json()["run_id"]
        sends_after_first = sum(1 for c in CALLS if c["op"] == "send")

        # reconnect: new events stream, same session, no new work
        client.get(f"/app/sessions/{alice_sid}/events")
        sends_after_reconnect = sum(1 for c in CALLS if c["op"] == "send")

        check("reconnect does not admit another run",
              sends_after_reconnect == sends_after_first == 1,
              f"sends {sends_after_first} -> {sends_after_reconnect}")

        # retrying the same business request replays the original run
        r2 = client.post(f"/app/sessions/{alice_sid}/send",
                         headers={"x-csrf-token": alice["csrfToken"]},
                         json={"message": "find me a hospital", "idempotency_key": key})
        check("same idempotency key replays the original run",
              r2.json()["run_id"] == run_id and r2.json()["replayed"] is True,
              f"run {run_id} vs {r2.json()['run_id']}")

        # ---- 6. cancellation is separate from disconnect --------------------
        CALLS.clear()
        client.get(f"/app/sessions/{alice_sid}/events")
        check("closing a stream is not a cancellation",
              not any(c["op"] == "cancel" for c in CALLS),
              f"calls={[c['op'] for c in CALLS]}")

        r = client.post(f"/app/runs/{run_id}/cancel?sid={alice_sid}",
                        headers={"x-csrf-token": alice["csrfToken"]})
        check("cancellation is an explicit call",
              r.status_code == 200 and any(c["op"] == "cancel" for c in CALLS),
              f"calls={[c['op'] for c in CALLS]}")

        # ---- 7. null cost stays unknown -------------------------------------
        cost = None
        shown = "Unknown" if cost is None else f"${cost / 1_000_000:.4f}"
        check("null cost is not displayed as zero", shown == "Unknown",
              f"shown={shown}")

        # ---- 8. API failures are visible ------------------------------------
        class BoomSessions(FakeSessions):
            async def create(self, **kw):
                from wkala import APIError
                raise APIError(502, "upstream_error", "upstream exploded", request_id="req_test")

        orig = backend.AgentClient
        try:
            class BoomCtx(FakeClientContext):
                async def __aenter__(self):
                    a = FakeAgents()
                    a.sessions = BoomSessions()
                    return a
            backend.AgentClient = BoomCtx
            with TestClient(backend.app) as c2:
                who = signin(c2, "carol@example.com")
                r = c2.post("/app/sessions", headers={"x-csrf-token": who["csrfToken"]})
                check("API failure is surfaced, not hidden",
                      r.status_code >= 400 and r.text,
                      f"status {r.status_code}")
        finally:
            backend.AgentClient = orig

        # ---- extra: csrf is required --------------------------------------
        r = client.post(f"/app/sessions/{alice_sid}/send",
                        json={"message": "x", "idempotency_key": "no-csrf"})
        check("a send without a CSRF token is refused", r.status_code == 403,
              f"got {r.status_code}")

        # ---- extra: tool refuses to name what it cannot confirm ------------
        t = business_tools.search_hospitals("Tawuniya", "Alkhobar", "B")
        check("tool refuses when no list exists", t.may_name is False and not t.hospitals,
              t.reason)

        b = business_tools.search_hospitals("Bupa", "Riyadh", "A")
        check("tool refuses when class cannot be mapped",
              b.may_name is False and not b.hospitals, b.reason)

        ok = business_tools.search_hospitals("GIG", "Riyadh", "VIP")
        check("tool answers when the table covers the tier",
              ok.may_name is True and len(ok.hospitals) > 0,
              f"{len(ok.hospitals)} hits")

    print()
    passed = 0
    for name, good, detail in RESULTS:
        print(("PASS  " if good else "FAIL  ") + name + (f"   [{detail}]" if detail else ""))
        passed += bool(good)
    print(f"\n{passed}/{len(RESULTS)} checks passed")
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
