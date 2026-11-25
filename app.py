"""Insurance Buddy — WAICY 2026 LLM & AI Agent track.

Streamlit UI. In this version every message goes to the model, and the model
calls the provider tables as a tool. The tables remain authoritative: the model
can only name a hospital that search_hospitals() returns, and that function
refuses when it cannot confirm a class.
"""

from __future__ import annotations

import json
import os

import streamlit as st

import business_tools
import fast_answers
import llm_config

DATA = os.path.join(os.path.dirname(__file__), "data")
PROMPT_FILE = os.path.join(os.path.dirname(__file__), "prompt.txt")

MODE = os.environ.get("BUDDY_MODE", "llm")

st.set_page_config(page_title="Insurance Buddy", page_icon="🏥", layout="centered")

CSS = """
<style>
  .block-container { max-width: 780px; padding-top: 2.2rem; }
  #MainMenu, footer { visibility: hidden; }
  .buddy-head { font-size: 1.5rem; font-weight: 650; letter-spacing: -0.02em; }
  .buddy-sub { color: #667085; font-size: .88rem; margin: .15rem 0 1.4rem; }
  .pill { display: inline-block; font-size: .72rem; padding: .1rem .5rem;
          border-radius: 999px; background: #ecfdf3; color: #027a48;
          border: 1px solid #abefc6; margin-left: .35rem; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


@st.cache_data
def load_prompt() -> str:
    with open(PROMPT_FILE, encoding="utf-8") as f:
        return f.read()


# --- tools the model may call ------------------------------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_hospitals",
            "description": (
                "Look up hospitals that accept a given insurer and class in a "
                "given city. Call this whenever the user wants a hospital, "
                "clinic or provider named. Returns either matching providers "
                "or the reason none can be confirmed."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "insurer": {"type": "string",
                                "description": "Insurer name as the user said it"},
                    "city": {"type": "string",
                             "description": "Saudi city name"},
                    "class_level": {
                        "type": "string",
                        "description": "Class printed on the card: A+, A, B, C, D, VIP, VVIP",
                    },
                },
                "required": ["insurer", "city", "class_level"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "carrier_summary",
            "description": (
                "Check whether an insurer publishes a provider list at all, and "
                "how many cities it covers."
            ),
            "parameters": {
                "type": "object",
                "properties": {"insurer": {"type": "string"}},
                "required": ["insurer"],
            },
        },
    },
]


def run_tool(name: str, args: dict) -> str:
    """Execute one tool call and return a string for the model."""
    try:
        if name == "search_hospitals":
            res = business_tools.search_hospitals(
                args.get("insurer", ""),
                args.get("city", ""),
                args.get("class_level", ""),
            )
            if not res.may_name or not res.hospitals:
                return json.dumps({"may_name": False, "reason": res.reason,
                                   "hospitals": []})
            return json.dumps({
                "may_name": True,
                "carrier": res.carrier,
                "city": res.city,
                "class_level": res.class_level,
                "hospitals": [
                    {"name": h.name, "phone": h.phone, "type": h.provider_type}
                    for h in res.hospitals
                ],
            })
        if name == "carrier_summary":
            return json.dumps(
                business_tools.carrier_summary(args.get("insurer", "")))
    except Exception as exc:
        return json.dumps({"error": type(exc).__name__})
    return json.dumps({"error": "unknown tool"})


def llm_reply(messages):
    system = load_prompt()
    provider = st.session_state.get("llm_provider", llm_config.DEFAULT_PROVIDER)
    typed = st.session_state.get("llm_key_typed")
    client = llm_config.build_client(provider, typed)
    model = llm_config.model_name(provider)

    convo = [{"role": "system", "content": system}] + messages

    for _ in range(4):
        r = client.chat.completions.create(
            model=model,
            messages=convo,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0.2,
            max_tokens=500,
        )
        msg = r.choices[0].message
        if not getattr(msg, "tool_calls", None):
            return msg.content or ""

        convo.append({
            "role": "assistant",
            "content": msg.content,
            "tool_calls": [
                {"id": tc.id, "type": "function",
                 "function": {"name": tc.function.name,
                              "arguments": tc.function.arguments}}
                for tc in msg.tool_calls
            ],
        })
        for tc in msg.tool_calls:
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            convo.append({"role": "tool", "tool_call_id": tc.id,
                          "content": run_tool(tc.function.name, args)})

    return ("I could not finish that lookup. Ask again with your insurer, "
            "class and city.")


# --- model key panel ---------------------------------------------------------

def _key_panel():
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
        st.caption("No key. This version answers through the model, so a key "
                   "is required.")

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
                st.caption("The key is valid but the account has no credit.")
            elif "401" in msg or "auth" in msg.lower() or "invalid" in msg.lower():
                st.caption("The key was rejected. Check it was copied whole.")

    st.caption("The key never leaves this session.")


# --- header ------------------------------------------------------------------

st.markdown('<div class="buddy-head">Insurance Buddy</div>',
            unsafe_allow_html=True)
st.markdown('<div class="buddy-sub">Which hospital will actually treat you, '
            'at your insurance class — Saudi Arabia.</div>',
            unsafe_allow_html=True)

with st.sidebar:
    st.caption("Insurance Buddy — WAICY 2026")
    st.write("")
    _key_panel()
    st.write("")
    if st.button("Clear the conversation", use_container_width=True):
        for k in ("messages",):
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()


# --- chat --------------------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("Hello — I can help you find which hospitals accept your "
                    "insurance. Tell me what you need, or ask me anything about "
                    "how cover works.")

if text := st.chat_input("Type your message…"):
    st.session_state.messages.append({"role": "user", "content": text})
    with st.chat_message("user"):
        st.markdown(text)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Looking that up…"):
                out = llm_reply(st.session_state.messages)
        except Exception as e:
            out = ("I cannot reach the model right now. Ask at the desk: "
                   '"Do you bill my insurer at my class?"')
            st.caption(f"Error: {type(e).__name__}")
        st.markdown(out, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": out})
