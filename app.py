"""Insurance Buddy — WAICY 2026 LLM & AI Agent track.

Streamlit UI. Works in two modes:

  LLM mode   (default): one chat box, the v10 system prompt, the right carrier
             file loaded once the insurer is known.
  Wkala mode (WKALA_BACKEND_URL set): messages, tool calls, approvals and usage
             stream from the Wkala customer backend in backend.py. The browser
             never holds a service key.

Set BUDDY_MODE=wkala to use the backend.
"""

from __future__ import annotations

import json
import os
import uuid

import streamlit as st

import business_tools
import fast_answers
import llm_config

DATA = os.path.join(os.path.dirname(__file__), "data")
PROMPT_FILE = os.path.join(os.path.dirname(__file__), "prompt.txt")

MODE = os.environ.get("BUDDY_MODE", "llm")

# Warm the table index once so the first user message is not the slow one.
fast_answers.prefetch_warm()
BACKEND = os.environ.get("WKALA_BACKEND_URL", "").rstrip("/")

st.set_page_config(page_title="Insurance Buddy", page_icon="🏥", layout="centered")

CSS = """
<style>
  .block-container { max-width: 780px; padding-top: 2.2rem; }
  #MainMenu, footer { visibility: hidden; }
  .buddy-head { font-size: 1.5rem; font-weight: 650; letter-spacing: -0.02em; }
  .buddy-sub { color: #667085; font-size: .88rem; margin: .15rem 0 1.4rem; }
  .buddy-answer { line-height: 1.55; }
  .buddy-answer strong { font-weight: 600; }
  div[data-testid="stChatMessage"] { background: transparent; }
  .card { border: 1px solid #e4e7ec; border-radius: 12px; padding: .8rem .95rem;
          margin: .45rem 0; background: #fff; }
  .card h4 { margin: 0 0 .35rem; font-size: .95rem; font-weight: 620; }
  .meta { color: #667085; font-size: .78rem; }
  .pill { display: inline-block; font-size: .72rem; padding: .1rem .5rem;
          border-radius: 999px; background: #ecfdf3; color: #027a48;
          border: 1px solid #abefc6; margin-left: .35rem; }
  .pill-n { background: #fef3f2; color: #b42318; border-color: #fecdca; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# --- provider list choice ----------------------------------------------------

def carriers_with_lists() -> list[str]:
    """Insurers that publish real per-city provider tables."""
    out = []
    for name in sorted(os.listdir(DATA)):
        d = os.path.join(DATA, name, "network")
        if os.path.isdir(d) and any(f.endswith(".md") and f != "README.md"
                                    for f in os.listdir(d)):
            out.append(name)
    return out


@st.cache_data
def load_prompt() -> str:
    with open(PROMPT_FILE, encoding="utf-8") as f:
        return f.read()


# --- LLM mode ----------------------------------------------------------------

def llm_reply(messages, carrier_file):
    system = load_prompt()
    if carrier_file:
        path = os.path.join(DATA, f"{carrier_file}.md")
        with open(path, encoding="utf-8") as f:
            body = f.read()
        system += ("\n\n## THE PROVIDER LIST FOR THIS USER'S COMPANY\n"
                   "The user's insurer is known. Use the tools to look up their city "
                   "and class. Never name any hospital these files do not list.\n\n" + body)
    else:
        system += ("\n\n## NO PROVIDER LIST YET\nYou do not yet know their insurer. "
                   "Ask which insurer is on their card. Name no hospital.")

    provider = st.session_state.get("llm_provider", llm_config.DEFAULT_PROVIDER)
    typed = st.session_state.get("llm_key_typed")
    client = llm_config.build_client(provider, typed)
    r = client.chat.completions.create(
        model=llm_config.model_name(provider),
        messages=[{"role": "system", "content": system}] + messages,
        temperature=0.2, max_tokens=400,
    )
    return r.choices[0].message.content


# --- LLM key panel -----------------------------------------------------------

def _key_panel():
    """Enter or check the model key. The key is held in this session only."""
    st.markdown("**Model key**")
    provider = st.selectbox(
        "Provider",
        options=list(llm_config.PROVIDERS),
        format_func=lambda p: llm_config.PROVIDERS[p]["label"],
        index=list(llm_config.PROVIDERS).index(
            st.session_state.get("llm_provider", llm_config.DEFAULT_PROVIDER)),
        key="llm_provider",
    )
    spec = llm_config.PROVIDERS[provider]

    typed = st.text_input(
        f"{spec['label']} API key",
        type="password",
        key="llm_key_typed",
        placeholder="sk-…",
        help=f"Get one at {spec['docs']}. Stored in this browser session only.",
    )

    stt = llm_config.status(provider, typed)
    if stt.present:
        st.caption(f"Using a key from **{stt.source}** ({stt.preview})")
        st.caption(f"Model: `{stt.model}`")
    else:
        st.caption("No key. The app still answers from the hospital tables.")

    if typed:
        ok, why = llm_config.looks_valid(provider, typed)
        (st.success if ok else st.warning)(why)

    if st.button("Test the key", use_container_width=True):
        with st.spinner("Calling the model…"):
            ok, msg = llm_config.check_live(provider, typed)
        st.session_state["llm_check"] = (ok, msg)

    if "llm_check" in st.session_state:
        ok, msg = st.session_state["llm_check"]
        if ok:
            st.success(msg)
        else:
            st.error(msg)
            if "402" in msg or "Insufficient" in msg or "balance" in msg.lower():
                st.caption("The key is valid but the account has no credit. "
                           "Top up at " + spec["docs"] + " — the table answers "
                           "keep working without it.")
            elif "401" in msg or "auth" in msg.lower() or "invalid" in msg.lower():
                st.caption("The key was rejected. Check it was copied whole, and "
                           "has not been rotated.")

    st.caption("The key never leaves this session: not saved to disk, not logged.")


# --- header ------------------------------------------------------------------

st.markdown('<div class="buddy-head">Insurance Buddy</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="buddy-sub">Which hospital will actually treat you, at your '
    'insurance class — Saudi Arabia.</div>', unsafe_allow_html=True)

if MODE == "wkala" and not BACKEND:
    st.error("WKALA_BACKEND_URL is not set. The Wkala UI needs the customer backend.")
    st.stop()

lists = carriers_with_lists()

with st.sidebar:
    st.caption("Insurance Buddy — WAICY 2026")
    if MODE == "wkala":
        st.markdown('<span class="pill">Wkala mode</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="pill">Direct mode</span>', unsafe_allow_html=True)
    st.write("")
    st.caption(f"{len(lists)} insurer(s) publish a provider table:")
    for c in lists:
        st.caption("· " + c.replace("-saudi-network", "").replace("-", " ").title())
    st.divider()
    _key_panel()
    st.divider()
    if st.button("Start over", use_container_width=True):
        for k in list(st.session_state):
            del st.session_state[k]
        st.rerun()


# --- direct mode -------------------------------------------------------------

if MODE != "wkala":
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "carrier" not in st.session_state:
        st.session_state.carrier = None

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown("Hello. Which insurer is on your card, "
                        "and which city are you in?")

    if text := st.chat_input("Type your message…"):
        # Read the facts out of this message FIRST, so the answer below uses
        # them. Detecting after the call made every answer one message late.
        found = (business_tools.find_carrier(text)
                 or st.session_state.carrier
                 or next((business_tools.find_carrier(m["content"])
                          for m in reversed(st.session_state.messages)
                          if m["role"] == "user"), None))
        st.session_state.carrier = found
        st.session_state.city = fast_answers.find_city(text) or st.session_state.get("city")
        st.session_state.class_level = (fast_answers.find_class(text)
                                        or st.session_state.get("class_level"))

        # The table path answers in single-digit milliseconds. The model is
        # only reached when the published data genuinely cannot settle it.
        fast = fast_answers.respond(
            text,
            st.session_state.messages,
            carrier=st.session_state.carrier,
            city=st.session_state.get("city"),
            class_level=st.session_state.get("class_level"),
        )

        st.session_state.messages.append({"role": "user", "content": text})
        with st.chat_message("user"):
            st.markdown(text)

        with st.chat_message("assistant"):
            if fast.kind in ("answer", "ask"):
                out = fast.text
                st.markdown(out, unsafe_allow_html=True)
            else:
                # Last resort: the model, with the table still authoritative.
                try:
                    with st.spinner(""):
                        out = llm_reply(st.session_state.messages,
                                        st.session_state.carrier)
                except Exception as e:
                    out = ("I cannot answer that from the published data, and the "
                           "model is unavailable. Ask the hospital desk: \"Do you "
                           "bill my insurer at my class?\"")
                    st.caption(f"Error: {type(e).__name__}")
                st.markdown(out, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": out})

# --- wkala mode --------------------------------------------------------------

else:
    import httpx

    if "user" not in st.session_state:
        st.session_state.user = None
    if "session_id" not in st.session_state:
        st.session_state.session_id = None
    if "results" not in st.session_state:
        st.session_state.results = []
    if "pending" not in st.session_state:
        st.session_state.pending = []

    def api(method: str, path: str, **kw):
        url = f"{BACKEND}{path}"
        return httpx.request(method, url, timeout=60, **kw)

    if not st.session_state.user:
        st.info("Sign in to use the agent. This is the app's own login — "
                "the Wkala service key stays on the server.")
        email = st.text_input("Email")
        if st.button("Sign in", disabled=not email):
            r = api("POST", "/auth/signin", json={"email": email})
            if r.status_code == 200:
                st.session_state.user = r.json()
                st.rerun()
            else:
                st.error(f"Sign-in failed: {r.status_code}")
        st.stop()

    user = st.session_state.user
    csrf = user["csrfToken"]

    if not st.session_state.session_id:
        r = api("POST", "/app/sessions", headers={"x-csrf-token": csrf})
        if r.status_code == 200:
            st.session_state.session_id = r.json()["id"]
        else:
            st.error(f"Could not create a session: {r.status_code} {r.text[:200]}")
            st.stop()

    sid = st.session_state.session_id

    snap = api("GET", f"/app/sessions/{sid}")
    if snap.status_code != 200:
        st.error(f"Could not load the session: {snap.status_code} {snap.text[:200]}")
        st.stop()

    data = snap.json()
    for msg in data.get("messages", []):
        role = msg.get("role", "assistant")
        with st.chat_message(role):
            for part in msg.get("parts", []):
                if part.get("type") == "text":
                    st.markdown(part.get("text", ""))
                else:
                    st.caption(f"[{part.get('type')} content]")

    for tool in data.get("tool_calls", []) or []:
        with st.container():
            st.markdown(
                f'<div class="card"><h4>{tool.get("title", "Tool")}'
                f'<span class="pill">{tool.get("status", "")}</span></h4>'
                f'<div class="meta">{json.dumps(tool.get("output"))[:300]}</div></div>',
                unsafe_allow_html=True,
            )

    for it in data.get("interactions", []) or []:
        if it.get("status") == "pending":
            st.warning(it.get("prompt", "Input is required"))
            for opt in it.get("permission_options", []) or []:
                if st.button(opt.get("label", opt.get("id")), key=f"opt-{it['id']}-{opt['id']}"):
                    r = api("POST",
                            f"/app/interactions/{it['id']}/respond?sid={sid}",
                            headers={"x-csrf-token": csrf},
                            json={"option_id": opt["id"]})
                    if r.status_code == 200:
                        st.rerun()
                    else:
                        st.error(f"Response rejected: {r.status_code}")

    if text := st.chat_input("Type your message…"):
        key = str(uuid.uuid4())
        r = api("POST", f"/app/sessions/{sid}/send",
                headers={"x-csrf-token": csrf},
                json={"message": text, "idempotency_key": key})
        if r.status_code == 200:
            st.rerun()
        else:
         st.error(f"Could not start work: {r.status_code} {r.text[:300]}")


