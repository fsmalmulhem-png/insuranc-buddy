"""Insurance Buddy — redesigned UI."""

APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

:root{
  --paper:#FAF8F4;
  --ink:#1C1917;
  --ink-2:#4A4540;
  --ink-3:#8C8781;
  --line:#E7E2DA;
  --line-2:#D6CFC3;
  --accent:#1F4E5F;
  --ok:#2F6B4F;
  --stop:#A33A2A;
}

/* force the light palette even when the visitor's system is dark */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
.stApp > header{
  background:var(--paper) !important;
  color:var(--ink) !important;
  color-scheme:light !important;
}

html, body{ background:var(--paper) !important; }

html, body, [class*="css"], .stApp{
  font-family:'Inter', -apple-system, sans-serif;
}

.block-container{
  max-width:800px;
  padding-top:3rem;
  padding-bottom:7rem;
}

#MainMenu, footer{ visibility:hidden; }
[data-testid="stHeader"]{ background:transparent !important; }
[data-testid="stDecoration"]{ display:none; }

/* ---- masthead ---------------------------------------------------------- */
.ib-mast{ display:flex; align-items:baseline; gap:.65rem; margin-bottom:.15rem; }
.ib-mark{
  width:25px; height:25px; border:1.5px solid var(--accent); border-radius:6px;
  display:inline-flex; align-items:center; justify-content:center;
  font-family:'JetBrains Mono', monospace; font-size:10.5px; color:var(--accent);
  transform:translateY(2px);
}
.ib-title{
  font-family:'Fraunces', Georgia, serif; font-size:1.65rem; font-weight:600;
  letter-spacing:-.015em; color:var(--ink); line-height:1.15;
}
.ib-sub{
  color:var(--ink-2); font-size:.9rem; margin:.5rem 0 0; line-height:1.55;
  max-width:44ch;
}
.ib-rule{ border-top:1px solid var(--line); margin:1.7rem 0 1.4rem; }

/* ---- chat -------------------------------------------------------------- */
.ib-turn{ margin:1.35rem 0; }
.ib-who{
  font-size:.68rem; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; margin-bottom:.4rem;
}
.ib-you{
  background:#fff; border:1px solid var(--line); border-radius:10px;
  padding:.68rem .85rem; font-size:.94rem; line-height:1.55; color:var(--ink);
}
.ib-bot{
  border-left:2.5px solid var(--accent); padding:.05rem 0 .05rem .95rem;
  font-size:.95rem; line-height:1.6; color:var(--ink);
}
.ib-bot ul{ margin:.5rem 0; padding-left:1.1rem; }
.ib-bot li{ margin:.18rem 0; }

/* ---- traversal tree ---------------------------------------------------- */
.ib-tree{
  margin:.75rem 0 1rem; padding:.9rem 1rem .8rem;
  background:#fff; border:1px solid var(--line); border-radius:10px;
}
.ib-tree-head{
  font-size:.66rem; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; margin-bottom:.8rem;
}
.ib-node{ position:relative; padding-left:1.55rem; padding-bottom:.62rem; }
.ib-node:last-child{ padding-bottom:0; }
.ib-node::before{
  content:""; position:absolute; left:.38rem; top:1.35rem; bottom:0;
  border-left:2.5px dotted #BFB5A4;
}
.ib-node:last-child::before{ display:none; }
.ib-node::after{
  content:""; position:absolute; left:.95rem; top:1.05rem; width:.5rem;
  border-top:2px dotted #BFB5A4;
}
.ib-dot{
  position:absolute; left:0; top:.42rem; width:13px; height:13px;
  border-radius:50%; border:2.5px solid var(--line-2); background:#fff;
}
.ib-dot.ok{ border-color:var(--ok); background:var(--ok); }
.ib-dot.stop{ border-color:var(--stop); background:var(--stop); }
.ib-dot.wait{ border-color:var(--line-2); background:#fff; }

.ib-lbl{ font-size:.88rem; font-weight:500; color:var(--ink); line-height:1.3; }
.ib-det{
  font-family:'JetBrains Mono', monospace; font-size:.72rem;
  color:var(--ink-3); margin-top:.1rem; line-height:1.4;
}
.ib-node.ok .ib-lbl{ color:var(--ok); }
.ib-node.stop .ib-lbl{ color:var(--stop); }
.ib-node.wait .ib-lbl{ color:var(--ink-3); font-weight:400; }

.ib-hits{
  margin-top:.7rem; padding-top:.7rem; border-top:1px solid var(--line);
  font-size:.85rem; color:var(--ink-2); line-height:1.5;
}
.ib-hits b{ color:var(--ink); font-weight:600; }

.ib-note{
  margin:.5rem 0 0; padding:.55rem .75rem; border-radius:7px;
  background:#F7EDEA; border:1px solid #EBD5CF;
  font-size:.83rem; color:#7A2A1D; line-height:1.5;
}

/* ---- native widgets, restyled to match -------------------------------- */
[data-testid="stChatInput"],
[data-testid="stBottom"] > div,
[data-testid="stBottomBlockContainer"]{
  background:var(--paper) !important;
  border-top:1px solid var(--line) !important;
}
[data-testid="stChatInput"] textarea{
  background:#fff !important; color:var(--ink) !important;
  border:1px solid var(--line-2) !important; border-radius:10px !important;
  font-family:'Inter', sans-serif !important; font-size:.94rem !important;
}
[data-testid="stChatInput"] textarea::placeholder{ color:var(--ink-3) !important; }
[data-testid="stChatInputSubmitButton"]{ color:var(--accent) !important; }

section[data-testid="stSidebar"]{
  background:#F1EDE5 !important;
  border-right:1px solid var(--line) !important;
}
section[data-testid="stSidebar"] *{ color:var(--ink) !important; }

.stSelectbox > div > div,
.stTextInput > div > div input{
  background:#fff !important; color:var(--ink) !important;
  border:1px solid var(--line-2) !important; border-radius:8px !important;
}
.stButton > button{
  background:#fff !important; color:var(--ink) !important;
  border:1px solid var(--line-2) !important; border-radius:8px !important;
  font-family:'Inter', sans-serif !important; font-size:.86rem !important;
  font-weight:500 !important; box-shadow:none !important;
}
.stButton > button:hover{
  border-color:var(--accent) !important; color:var(--accent) !important;
}

.sb-head{
  font-family:'Fraunces', Georgia, serif; font-size:1rem; font-weight:600;
  color:var(--ink); margin-bottom:.15rem;
}
.sb-note{ font-size:.75rem; color:var(--ink-3); line-height:1.5; margin-bottom:.9rem; }
</style>
"""


def mast(company_line: str = "WAICY 2026 · LLM &amp; AI Agent") -> str:
    return f"""
<div class="ib-mast">
  <span class="ib-mark">IB</span>
  <span class="ib-title">Insurance Buddy</span>
</div>
<p class="ib-sub">Which hospitals will actually treat you, at the insurance
class printed on your card — Saudi Arabia. {company_line}.</p>
<div class="ib-rule"></div>
"""


NODE_ICON = {"passed": "ok", "failed": "stop", "blocked": "wait", "pending": "wait"}


def tree(trace) -> str:
    if trace is None:
        return ""
    parts = ['<div class="ib-tree"><div class="ib-tree-head">Traversal</div>']
    for step in trace.steps:
        cls = NODE_ICON.get(step.state, "wait")
        label_cls = {"passed": "ok", "failed": "stop"}.get(step.state, "wait")
        parts.append(
            f'<div class="ib-node {label_cls}">'
            f'<span class="ib-dot {cls}"></span>'
            f'<div class="ib-lbl">{step.label}</div>'
            f'<div class="ib-det">{step.detail}</div></div>'
        )
    if trace.may_name and trace.hospitals:
        names = ", ".join(h.name for h in trace.hospitals[:4])
        parts.append(
            f'<div class="ib-hits"><b>{len(trace.hospitals)} providers</b> '
            f"state this class — {names}</div>")
    elif trace.reason:
        parts.append(f'<div class="ib-note">{trace.reason}</div>')
    parts.append("</div>")
    return "".join(parts)


def turn(who: str, text: str, rendered: str | None = None) -> str:
    if who == "you":
        return (f'<div class="ib-turn"><div class="ib-who">You</div>'
                f'<div class="ib-you">{text}</div></div>')
    body = rendered if rendered is not None else text.replace("\n", "<br>")
    return (f'<div class="ib-turn"><div class="ib-who">Insurance Buddy</div>'
            f'<div class="ib-bot">{body}</div></div>')


def sidebar_block() -> str:
    return ('<div class="sb-head">Model key</div>'
            '<div class="sb-note">Held in this browser session only. '
            'Never written to disk and never logged.</div>')


def sidebar_ready() -> str:
    return ('<div class="sb-head">Ready</div>'
            '<div class="sb-note">The model key is configured on the server. '
            'Nothing to enter here.</div>')
