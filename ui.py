"""Insurance Buddy — redesigned UI.

Design notes:
  - warm paper background, one accent, no neon, no glow, no gradients
  - typography does the work: a serif for headings, a sans for body
  - the traversal tree is drawn with CSS borders, not an image or canvas
  - every visual element is reproducible in Streamlit's markup; no JS
"""

APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

:root{
  --paper:#FAF8F4;
  --ink:#1C1917;
  --ink-2:#57534E;
  --ink-3:#8C8781;
  --line:#E7E2DA;
  --line-2:#D6CFC3;
  --accent:#1F4E5F;
  --accent-soft:#EEF3F4;
  --ok:#2F6B4F;
  --ok-soft:#EDF4EF;
  --stop:#A33A2A;
  --stop-soft:#F7EDEA;
}

html, body, [class*="css"]{
  font-family:'Inter', -apple-system, sans-serif;
  color:var(--ink);
}

.stApp{ background:var(--paper); }

.block-container{
  max-width:860px;
  padding-top:3.4rem;
  padding-bottom:6rem;
}

#MainMenu, footer, header{ visibility:hidden; }

/* ---- masthead ---------------------------------------------------------- */
.ib-mast{ display:flex; align-items:baseline; gap:.7rem; margin-bottom:.2rem; }
.ib-mark{
  width:26px; height:26px; border:1.5px solid var(--accent); border-radius:6px;
  display:inline-flex; align-items:center; justify-content:center;
  font-family:'JetBrains Mono', monospace; font-size:11px; color:var(--accent);
  letter-spacing:-.02em; transform:translateY(2px);
}
.ib-title{
  font-family:'Fraunces', Georgia, serif; font-size:1.72rem; font-weight:600;
  letter-spacing:-.015em; color:var(--ink); line-height:1.1;
}
.ib-sub{
  color:var(--ink-2); font-size:.92rem; margin:.55rem 0 0;
  max-width:46ch; line-height:1.55;
}
.ib-rule{ border-top:1px solid var(--line); margin:1.9rem 0 1.6rem; }

/* ---- chat -------------------------------------------------------------- */
.ib-turn{ margin:1.5rem 0; }
.ib-who{
  font-size:.7rem; letter-spacing:.11em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; margin-bottom:.45rem;
}
.ib-you{
  background:#fff; border:1px solid var(--line); border-radius:11px;
  padding:.72rem .9rem; font-size:.95rem; line-height:1.55;
}
.ib-bot{
  border-left:2px solid var(--accent); padding:.1rem 0 .1rem 1rem;
  font-size:.97rem; line-height:1.62;
}

/* ---- traversal tree ---------------------------------------------------- */
.ib-tree{
  margin:.85rem 0 1.15rem; padding:1rem 1.05rem .85rem;
  background:#fff; border:1px solid var(--line); border-radius:11px;
}
.ib-tree-head{
  font-size:.68rem; letter-spacing:.11em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; margin-bottom:.85rem;
}
.ib-node{ position:relative; padding-left:1.6rem; padding-bottom:.72rem; }
.ib-node:last-child{ padding-bottom:0; }
.ib-node::before{
  content:""; position:absolute; left:.40rem; top:1.48rem; bottom:-.02rem;
  border-left:2.5px dotted #BFB5A4;
}
.ib-node:last-child::before{ display:none; }
.ib-node::after{
  content:""; position:absolute; left:1.02rem; top:1.15rem; width:.5rem;
  border-top:2px dotted #C9C0B1;
}
.ib-dot{
  position:absolute; left:0; top:.5rem; width:14px; height:14px;
  border-radius:50%; border:2.5px solid var(--line-2); background:#fff;
}
.ib-dot.ok{ border-color:var(--ok); background:var(--ok); }
.ib-dot.stop{ border-color:var(--stop); background:var(--stop); }
.ib-dot.wait{ border-color:var(--line-2); background:#fff; }

.ib-lbl{ font-size:.9rem; font-weight:500; color:var(--ink); line-height:1.3; }
.ib-det{
  font-family:'JetBrains Mono', monospace; font-size:.74rem;
  color:var(--ink-3); margin-top:.12rem; line-height:1.4;
}
.ib-node.ok .ib-lbl{ color:var(--ok); }
.ib-node.stop .ib-lbl{ color:var(--stop); }
.ib-node.wait .ib-lbl{ color:var(--ink-3); font-weight:400; }

.ib-hits{
  margin-top:.8rem; padding-top:.8rem; border-top:1px solid var(--line);
  font-size:.86rem; color:var(--ink-2);
}
.ib-hits b{ color:var(--ink); font-weight:600; }

.ib-note{
  margin:.55rem 0 0; padding:.6rem .8rem; border-radius:8px;
  background:var(--stop-soft); border:1px solid #EBD9D4;
  font-size:.84rem; color:#7A2A1D; line-height:1.5;
}

/* ---- input ------------------------------------------------------------- */
div[data-testid="stChatInput"]{ border-top:1px solid var(--line); }
div[data-testid="stChatInput"] textarea{
  background:#fff; border:1px solid var(--line-2); border-radius:10px;
  font-family:'Inter', sans-serif; font-size:.95rem;
}
div[data-testid="stChatInput"] textarea:focus{
  border-color:var(--accent); box-shadow:none;
}

/* ---- sidebar ----------------------------------------------------------- */
section[data-testid="stSidebar"]{ background:#F4F1EA; border-right:1px solid var(--line); }
section[data-testid="stSidebar"] .block-container{ padding-top:2rem; }
.sb-head{
  font-family:'Fraunces', Georgia, serif; font-size:1.02rem; font-weight:600;
  color:var(--ink); margin-bottom:.15rem;
}
.sb-note{ font-size:.76rem; color:var(--ink-3); line-height:1.5; margin-bottom:1rem; }
.sb-key{ font-size:.7rem; letter-spacing:.1em; text-transform:uppercase;
         color:var(--ink-3); font-weight:600; }
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
    """Render a Trace as a dotted traversal tree."""
    if trace is None:
        return ""

    head = "Traversal"
    parts = [f'<div class="ib-tree"><div class="ib-tree-head">{head}</div>']

    for step in trace.steps:
        cls = NODE_ICON.get(step.state, "wait")
        label_cls = {"passed": "ok", "failed": "stop"}.get(step.state, "wait")
        parts.append(
            f'<div class="ib-node {label_cls}">'
            f'<span class="ib-dot {cls}"></span>'
            f'<div class="ib-lbl">{step.label}</div>'
            f'<div class="ib-det">{step.detail}</div>'
            f"</div>"
        )

    if trace.may_name and trace.hospitals:
        names = ", ".join(h.name for h in trace.hospitals[:4])
        parts.append(
            f'<div class="ib-hits"><b>{len(trace.hospitals)} providers</b> '
            f"state this class — {names}</div>"
        )
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
