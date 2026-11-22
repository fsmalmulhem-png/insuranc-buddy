# Wkala integration — design note

Wkala SDK **0.1.0**, installed from the supplied wheel
(`https://wkala.okal.io/downloads/wkala-0.1.0-py3-none-any.whl`), never a registry
version. Every API call in this note was checked against the installed package,
not only the documentation.

## The smallest integration that meets the checks

| Piece | File | Why it is the minimum |
|---|---|---|
| Customer backend | `backend.py` (FastAPI) | Owns the service key, sign-in, ownership, the `/app` bridge |
| Signed cookie + CSRF | same file | Two users cannot cross sessions; a browser cannot forge identity |
| Durable session store | same file (`Store`) | Sessions survive a restart; swap for Postgres in production |
| Idempotency receipt | same file (`put_request`) | A retried request replays the original run |
| Streaming | `GET /app/sessions/{sid}/events` | SSE, unbuffered, observation only |
| Cancellation | `POST /app/runs/{id}/cancel` | Explicit, never implied by a disconnect |
| Approval | `POST /app/interactions/{id}/respond` | Owner-scoped, exact option only |
| Business logic | `business_tools.py` | In-app, no MCP needed |
| Mocked test | `test_integration.py` | 18 checks, no key, no spend |
| Paid test | `test_e2e_paid.py` | Real service, `BUDDY_PAID_TESTS=1` |

**No MCP server is used.** As you asked, the business logic lives in the app:
`business_tools.search_hospitals()` reads the carrier files directly and returns a
`may_name` flag the agent cannot override. The agent is instructed to write a
`<request>` JSON object, and the app resolves it. This avoids the remote-MCP
reachability problem entirely.

The `<request>` instruction lives in the agent profile, not in this repo. The
suggested text is in `profile-instructions.md`.

## Acceptance checks — how each is met

| Check | Mechanism | Test |
|---|---|---|
| No service key in browser bundles | Key read only in `backend.py`; browser gets `user_id` + `csrf` | `no service key in browser payloads` |
| Two users cannot access each other's sessions | `Store.owned_session()`; 404 for missing **and** foreign (no enumeration) | `other user's session is not readable` |
| Message and tool updates while work runs | SSE from `handle.events()`, no buffering, `X-Accel-Buffering: no` | `stream yields updates during the run` |
| Approval is explicit | Interaction ends only via an offered `option_id`; empty body rejected | `approval submits the offered option` |
| Disconnect/reconnect does not duplicate work | Observation is separate from admission; `idempotency_key` replay | `reconnect does not admit another run` |
| Cancellation separate from disconnect | `cancel` is its own route; closing SSE never cancels | `closing a stream is not a cancellation` |
| Null cost remains unknown | `None` renders as "Unknown", never `0` | `null cost is not displayed as zero` |
| API failures are visible | `APIError`/`TransportError` mapped to 4xx/5xx with `code`, `message`, `request_id` | `API failure is surfaced, not hidden` |

Two extra checks beyond the list: a send without a CSRF token is refused, and the
tool refuses to name a hospital for insurers that publish no list.

**Verified live:** the backend serves all 10 routes; sign-in returns a CSRF token;
and creating a session with an invalid key returns
`{"code":"authentication_required", ...}` with a real `request_id` — a visible
failure, not a silent one.

## Unavailable in this deployment

Stated plainly rather than faked:

1. **No working `WKALA_API_KEY`.** The key in this workspace's environment
   (`rly_c2…`) is rejected by the service with `authentication_required`. So the
   real end-to-end test and any live run are blocked. Create a key in the Wkala
   dashboard (read + run scope; add configure for tools/skills), then set
   `WKALA_API_KEY` in the backend environment.
2. **No React/Next app.** The repo ships a Streamlit UI. The docs supply the React
   store, `useSession`, and the Next proxy; this app does not use them. The
   Streamlit UI talks to the same `/app` routes, so no event reducer was written.
   If you later add React, use `@wkala/react`'s store for replay — do not
   re-implement one.
3. **Executable skill scripts, stateful session forks, native file-artifact export**
   — not in SDK 0.1.0. Not used, not simulated.
4. **File-backed store, not Postgres.** Single process only. The docs' reference
   uses SQLAlchemy/Postgres; `Store` exists so the example runs, and it is the one
   thing to replace before more than one worker serves traffic.
5. **Demo sign-in.** `POST /auth/signin` creates a user from an email with no
   password. Replace with the app's real identity provider before shipping.

## Where the honest behaviour now lives

The four carriers that publish real per-city tables are the only ones that can
produce a hospital name:

| Insurer | Cities | Hospital can be named? |
|---|---|---|
| GIG | 355 | Yes, when the tier matches |
| Bupa | 100 | **No** — publishes NW tiers, no Class A/B mapping |
| Amana | 52 | **No** — sub-tier could not be recovered from the source PDF |
| GGI | 52 | No — accreditations mostly lapsed |

Everything else publishes no list at all. The tool encodes this rather than
letting the model guess, which is the project's core finding expressed as code.

## Running it

```bash
python -m pip install -r requirements-wkala.txt

export SESSION_SECRET=$(python -c "import secrets;print(secrets.token_urlsafe(32))")
export WKALA_API_KEY=...            # backend only
export ALLOWED_ORIGIN=http://localhost:8501
export COOKIE_SECURE=1              # behind HTTPS

uvicorn backend:app --port 8081

BUDDY_MODE=wkala WKALA_BACKEND_URL=http://127.0.0.1:8081 \
  streamlit run app.py
```

Tests:

```bash
python test_integration.py                      # mocked, 18 checks, free
BUDDY_PAID_TESTS=1 python test_e2e_paid.py      # real, spends money
```
