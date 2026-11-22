# Deploy — getting a link people can open

Two things matter for judges: the link opens, and it answers without a wait.

## The speed decision, first

Measured on the real data:

| Path | Time | What handles it |
|---|---|---|
| Carrier not in the list → refusal | **0.1 ms** | local tables |
| Class cannot be mapped → refusal | **2–3 ms** | local tables |
| Full answer with hospitals | **4–7 ms** | local tables |
| Anything the tables cannot settle | **~1–2 s** | the model |

**Most questions never reach the model.** `fast_answers.respond()` resolves them
from the carrier tables and returns `kind="answer"` or `kind="ask"`. Only
`kind="model"` falls through to an LLM call. That is why the app feels instant:
the slow path is the rare path.

This also means the app works **without any LLM key** for the common questions.
You do not need a paid model to demo it.

## The model key (optional)

The app answers most questions from the tables with **no model at all**. A key
is only needed for the questions the tables cannot settle.

**In the UI:** sidebar → **Provider** (DeepSeek is the default) → paste the key
→ **Test the key**. It is held in that browser session only: not written to
disk, not logged, never sent anywhere but the provider. Only the last four
characters are shown.

**On the host:** set `DEEPSEEK_API_KEY` as an environment secret, or add
`.streamlit/secrets.toml`:

```toml
DEEPSEEK_API_KEY = "sk-..."
```

That file is in `.gitignore` — never commit it.

**DeepSeek specifics:** base URL `https://api.deepseek.com`, model
`deepseek-chat`. It is OpenAI-compatible, so the same client works.

**A 402 "Insufficient Balance" means the key is valid and the account is out of
credit.** The key check passes authentication; only billing blocks the call.
Top up at <https://platform.deepseek.com/api_keys>. Until then the table
answers keep working — nothing else breaks.

## Option 1 — Streamlit Community Cloud (free, fastest to a link)

Best fit: no Docker needed, one public URL, sleeps after inactivity.

1. The repo `siudro/insurance-buddy` is private. Streamlit Cloud can deploy a
   private repo, but the app itself must be reachable. Simplest is to make the
   repo public, or connect the GitHub account that owns it.
2. Go to <https://share.streamlit.io> → **New app**.
3. Repo: `siudro/insurance-buddy`, branch `main`, main file `app.py`.
4. In **Advanced settings → Secrets**, optionally add:
   ```toml
   OPENAI_API_KEY = "sk-..."
   ```
   Optional — the table path works without it.
5. Deploy. You get `https://<name>.streamlit.app`.

**Caveat:** free apps go to sleep after inactivity. The first visit takes ~30 s
to wake. If a judge lands on a sleeping app and waits 30 s, that is the opposite
of "quick". Either accept it, or use Option 2.

## Option 2 — any container host (no cold sleep)

The repo has a working `Dockerfile`. Render, Railway, Fly.io and Cloud Run all
accept it.

```bash
docker build -t insurance-buddy .
docker run -p 8080:8080 -p 8081:8081 insurance-buddy
```

On each host: connect the repo, pick the Dockerfile, set the port to **8080**,
add `OPENAI_API_KEY` as an environment secret if you want the model fallback.
Keep an instance warm (Render's free tier sleeps too; a paid small instance does
not).

## Option 3 — share the link in the submission

A public URL is what the LLM track asks for. Whatever host you pick, put the
final URL in Task 3 and in the PDF.

## What to check before you send the link

- [ ] Open it in a **private browser window** — proves no login is needed
- [ ] Ask "I have Bupa Class B in Riyadh" — should answer in under a second
- [ ] Ask "I am sick, which hospital?" — should ask for the insurer, not refuse
- [ ] Ask for an insurer that publishes nothing (Tawuniya) — should refuse honestly
- [ ] Confirm no key appears in the page source or browser network tab
- [ ] Load it on a phone

## Known limits of this deployment

- Direct mode (Streamlit) does not carry the Wkala streams. Wkala mode needs the
  FastAPI backend on a second port plus a real `WKALA_API_KEY`, which is
  currently invalid in this workspace.
- File-backed session store: single process only.
- The model fallback needs `OPENAI_API_KEY`; without it the app still answers
  from tables and says so when it cannot.
