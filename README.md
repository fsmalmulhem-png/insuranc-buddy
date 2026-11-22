# Insurance Buddy — webapp

WAICY 2026, LLM & AI Agent track.

A chat app that answers one question: **which hospital will actually treat me, at
my insurance class?** Saudi insurers publish coverage per class, not per company,
and the class is often missing. This app holds 25 carriers' verified network data
and refuses to name a hospital it cannot confirm.

## Answers in milliseconds, not seconds

Most questions are answered from the carrier tables with no model call at all:

| Question | Time |
|---|---|
| Insurer publishes no list → refusal | 0.1 ms |
| Class cannot be mapped → refusal | 2–3 ms |
| Full answer with hospitals and phones | 4–7 ms |
| Only what the tables cannot settle | ~1–2 s (model) |

`fast_answers.py` decides which path to take. The model is the last resort, so
the app is instant for the questions people actually ask — and works with no
API key at all for those.

**Getting a public link:** see [DEPLOY.md](DEPLOY.md).

## What is here

| Path | What |
|---|---|
| `app.py` | Streamlit UI (direct mode, or Wkala mode) |
| `backend.py` | FastAPI customer backend — owns the Wkala key, sign-in, ownership |
| `business_tools.py` | Carrier lookup: carrier summary + per-city hospital search |
| `fast_answers.py` | Instant path: answers from tables; the model is the last resort |
| `llm_config.py` | Model key handling: DeepSeek/OpenAI, session-only, never logged |
| `DEPLOY.md` | How to get a link judges can open |
| `prompt.txt` | The v10 system prompt |
| `profile-instructions.md` | Agent profile text, including the `<request>` protocol |
| `data/` | 25 carrier folders: `SKILL.md`, tiers, and published per-city tables |
| `test_app.py` | Carrier-detection tests |
| `test_fast_answers.py` | Instant-path tests, including a 50 ms ceiling |
| `test_integration.py` | Mocked Wkala integration — 18 checks, free |
| `test_e2e_paid.py` | Real end-to-end, behind `BUDDY_PAID_TESTS=1` |
| `WKALA_INTEGRATION.md` | Design note, acceptance checks, known gaps |

## Which insurers can name a hospital

Five carry per-city provider tables. The tool encodes this:

| Insurer | Cities | May a hospital be named? |
|---|---|---|
| GIG | 356 | Yes, when the tier matches |
| Tawuniya | 36 | **Yes for Class A** — parsed from the app's PDF (1,345 providers) |
| Bupa | 100 | No — publishes NW tiers, no Class A/B mapping |
| Amana | 160 | No — sub-tier unrecoverable from the source PDF |
| GGI | 60 | No — accreditations mostly lapsed |
| the other 20 | 0 | No — publish no list at all |

That refusal is the project's finding, not a limitation of the code.

**Tawuniya was originally listed as publishing nothing.** That was wrong: the
network exists in the mobile app and its downloadable PDF, not on the public
website. A policy holder supplied it during our interviews. See
`data/tawuniya-saudi-network/network/README.md` for what changed and why the
automated checks could not reach it — the lesson is that "I cannot fetch it" is
not the same as "it does not exist".

## Run locally (direct mode, no Wkala)

```bash
python -m venv .venv
./.venv/bin/pip install -r requirements-wkala.txt
echo 'OPENAI_API_KEY = "sk-..."' > .streamlit/secrets.toml
./.venv/bin/streamlit run app.py
```

## Run with Wkala

```bash
export SESSION_SECRET=$(python -c "import secrets;print(secrets.token_urlsafe(32))")
export WKALA_API_KEY=...          # backend only
export ALLOWED_ORIGIN=http://localhost:8501

uvicorn backend:app --port 8081
BUDDY_MODE=wkala WKALA_BACKEND_URL=http://127.0.0.1:8081 streamlit run app.py
```

## Tests

```bash
python test_app.py               # carrier detection
python test_fast_answers.py      # instant path, each case under 50 ms
python test_llm_config.py        # key format, precedence, redaction
BUDDY_PAID_TESTS=1 python test_llm_config.py   # + one real model call
python test_integration.py       # 18 mocked checks, no key, no spend
BUDDY_PAID_TESTS=1 python test_e2e_paid.py   # real service, spends money
```

## Docker

```bash
docker build -t insurance-buddy .
docker run -p 8080:8080 -p 8081:8081 \
  -e SESSION_SECRET=... -e OPENAI_API_KEY=... insurance-buddy
```

The image starts the backend on 8081 and the UI on 8080. Put one origin in front
of both before exposing it (see `WKALA_INTEGRATION.md`).

**Never commit a key.** `.gitignore` covers `.env` and `.streamlit/secrets.toml`.
