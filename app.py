"""Insurance Buddy — WAICY 2026 LLM & AI Agent track.

The layout: a quiet paper page, a chat, and under each answer the traversal
that produced it. The tree is the real control flow of search_hospitals(),
recorded by trace.build_trace() — not a decoration.

Every message goes to the model. The model calls the provider tables as a
tool. The tables remain authoritative: a hospital can only be named if
search_hospitals() returned it for that class.
"""

from __future__ import annotations

import json
import os
import re

import streamlit as st

import business_tools
import llm_config
import trace as tracer
import ui

DATA = os.path.join(os.path.dirname(__file__), "data")
PROMPT_FILE = os.path.join(os.path.dirname(__file__), "prompt.txt")

st.set_page_config(page_title="Insurance Buddy", page_icon="🏥", layout="centered")
st.markdown(ui.APP_CSS, unsafe_allow_html=True)


@st.cache_data
def load_prompt() -> str:
    with open(PROMPT_FILE, encoding="utf-8") as f:
        return f.read()


# --- facts, read from the user's own words -----------------------------------

CITY_ALIASES = {
    "alkhobar": "al khobar", "al-khobar": "al khobar", "khobar": "al khobar",
    "alkhubar": "al khubar", "khubar": "al khubar",
    "mecca": "makkah", "medina": "madinah", "al ahsa": "hofuf",
}


def read_facts(text: str) -> dict:
    """Insurer, city and class as stated in one message, best effort."""
    found = {"insurer": "", "city": "", "class": ""}
    carrier = business_tools.find_carrier(text)
    if carrier:
        found["insurer"] = carrier.replace("-saudi-network", "").replace("-", " ")
    low = text.lower()
    for alias, canonical in CITY_ALIASES.items():
        if alias in low:
            found["city"] = canonical.title()
            break
    m = re.search(r"\bclass\s*([A-E])\s*(\+)?", text, re.I)
    if m:
        found["class"] = m.group(1).upper() + (m.group(2) or "")
    else:
        m = re.search(r"\b(VIP|VVIP)\b", text, re.I)
        if m:
            found["class"] = m.group(1).upper()
    return found


# --- tools -------------------------------------------------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_hospitals",
            "description": (
                "Look up hospitals that accept a given insurer and class in a "
                "given city. Call this whenever the user wants a hospital named. "
                "Returns matching providers, or the reason none can be confirmed."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "insurer": {"type": "string"},
                    "city": {"type": "string"},
                    "class_level": {"type": "string"},
                },
                "required": ["insurer", "city", "class_level"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "carrier_summary",
            "description": "Check whether an insurer publishes a list at all.",
            "parameters": {
                "type": "object",
                "properties": {"insurer": {"type": "string"}},
                "required": ["insurer"],
            },
        },
    },
]


def run_tool(name: str, args: dict) -> str:
    try:
        if name == "search_hospitals":
            res = business_tools.search_hospitals(
                args.get("insurer", ""), args.get("city", ""),
                args.get("class_level", ""))
            if not res.may_name or not res.hospitals:
                return json.dumps({"may_name": False, "reason": res.reason,
                                   "hospitals": []})
            return json.dumps({
                "may_name": True,
                "hospitals": [{"name": h.name, "phone": h.phone} for h in res.hospitals],
            })
        if name == "carrier_summary":
            return json.dumps(business_tools.carrier_summary(args.get("insurer", "")))
    except Exception as exc:
        return json.dumps({"error": type(exc).__name__})
    return json.dumps({"error": "unknown tool"})


def llm_reply(messages, on_lookup=None):
    system = load_prompt()
    provider = st.session_state.get("llm_provider", llm_config.DEFAULT_PROVIDER)
    typed = st.session_state.get("llm_key_typed")
    client = llm_config.build_client(provider, typed)
    model = llm_config.model_name(provider)
    convo = [{"role": "system", "content": system}] + messages

    for _ in range(4):
        r = client.chat.completions.create(
            model=model, messages=convo, tools=TOOLS,
            tool_choice="auto", temperature=0.2, max_tokens=500)
        msg = r.choices[0].message
        if not getattr(msg, "tool_calls", None):
            return msg.content or ""

        convo.append({
            "role": "assistant", "content": msg.content,
            "tool_calls": [{"id": tc.id, "type": "function",
                            "function": {"name": tc.function.name,
                                         "arguments": tc.function.arguments}}
                           for tc in msg.tool_calls],
        })
        for tc in msg.tool_calls:
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            if tc.function.name == "search_hospitals" and on_lookup:
                on_lookup(args)
            convo.append({"role": "tool", "tool_call_id": tc.id,
                          "content": run_tool(tc.function.name, args)})

    return "I could not finish that lookup. Ask again with your insurer, class and city."


# --- sidebar -----------------------------------------------------------------

with st.sidebar:
    st.markdown(ui.sidebar_block(), unsafe_allow_html=True)

    provider = st.selectbox(
        "Provider", options=list(llm_config.PROVIDERS),
        format_func=lambda p: llm_config.PROVIDERS[p]["label"],
        index=list(llm_config.PROVIDERS).index(
            st.session_state.get("llm_provider", llm_config.DEFAULT_PROVIDER)),
        key="llm_provider", label_visibility="collapsed")

    typed = st.text_input(
        "API key", type="password", key="llm_key_typed",
        placeholder="sk-…", label_visibility="collapsed")

    stt = llm_config.status(provider, typed)
    st.markdown(
        f'<div class="sb-note">'
        f'{("Key present · " + stt.preview) if stt.present else "No key set"}'
        f"<br>Model: {stt.model}</div>", unsafe_allow_html=True)

    if st.button("Test the key", use_container_width=True):
        with st.spinner(""):
            ok, msg = llm_config.check_live(provider, typed)
        st.session_state["llm_check"] = (ok, msg)
    if "llm_check" in st.session_state:
        ok, msg = st.session_state["llm_check"]
        (st.success if ok else st.error)(msg)

    st.markdown("<div style='height:.6rem'></div>", unsafe_allow_html=True)
    if st.button("Start again", use_container_width=True):
        for k in ("messages", "llm_check"):
            st.session_state.pop(k, None)
        st.rerun()

# --- page --------------------------------------------------------------------

st.markdown(ui.mast(), unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown(ui.turn(
        "bot",
        "Hello. Ask me anything about how your cover works — or tell me your "
        "insurer, class and city and I will find the hospitals that accept you."),
        unsafe_allow_html=True)

for m in st.session_state.messages:
    rendered = m.get("rendered")
    st.markdown(ui.turn("you" if m["role"] == "user" else "bot",
                        m["content"] if m["role"] == "user" else "",
                        rendered=rendered),
                unsafe_allow_html=True)

if text := st.chat_input("Type your message…"):
    facts = read_facts(text)
    st.session_state.messages.append({"role": "user", "content": text})

    captured = {}

    def on_lookup(args):
        captured["trace"] = tracer.build_trace(
            args.get("insurer", ""), args.get("city", ""),
            args.get("class_level", ""))

    try:
        with st.spinner("Looking that up…"):
            out = llm_reply(
                [{"role": m["role"], "content": m["content"]}
                 for m in st.session_state.messages],
                on_lookup=on_lookup)
    except Exception as e:
        out = ('I cannot reach the model right now. At the desk, ask: '
               '"Do you bill my insurer at my class?"')
        st.session_state.messages.append(
            {"role": "assistant", "content": out,
             "rendered": out + f'<div class="ib-note">{type(e).__name__}</div>'})
        st.rerun()

    tr = captured.get("trace")
    if tr is None and facts["insurer"] and facts["city"] and facts["class"]:
        tr = tracer.build_trace(facts["insurer"], facts["city"], facts["class"])

    rendered = out.replace("\n", "<br>")
    if tr is not None:
        rendered = ui.tree(tr) + rendered

    st.session_state.messages.append(
        {"role": "assistant", "content": out, "rendered": rendered})
    st.rerun()
