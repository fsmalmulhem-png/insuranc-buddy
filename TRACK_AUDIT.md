# Am I on track? — audit against the LLM track rules

Checked against the official track skill: `waicy-2026-large-language-models`.
Dates from the track's delivery schedule. Anything I could not verify from files
is marked **UNVERIFIED**, not assumed.

---

## Verdict up front

**The engineering is ahead. The submission paperwork is behind.**

Two of the five required items are done. The three that carry 50% of the AI
criteria — and one pass/fail link — are not started.

| Required item | State | Due | Owner |
|---|---|---|---|
| Specific AI service defined | **Done** | 2026-11-02 | Students |
| Iterative design documented | **Material exists, not written up** | 2026-11-14 | Student writer |
| **Link to chatbot (live)** | **MISSING** | 2026-11-18 | Student presenter |
| **Link to chat history (≥10 msgs)** | **MISSING** | 2026-11-18 | Student presenter |
| 3 user profiles | **Not written** | 2026-11-06 | Student design lead |
| PDF (`LLM_ProjectName.pdf`) | **Not started** | 2026-11-23 | Packaging lead |
| Drive folder, shared | Not started | 2026-11-23 | Packaging lead |

**Today is 18 November. Two rows are due today and both are missing.**

---

## Where you are ahead of schedule

These are genuinely done and provable from files in the repo:

- **A working app** — Streamlit, runs, health-checks `ok`
- **Real data** — 25 carriers, 697 city tables extracted from the insurers' own
  published locators
- **54 automated checks passing** — 28 + 18 + 10
- **The honest-refusal behaviour** the rubric explicitly rewards ("know when to
  say I don't know")
- **A measured iterative history** — v4 → v10, each version with the specific
  failure that forced it

That is more technical evidence than most entries will have. Do not throw it
away.

---

## Where you are at risk

### 1. The scope may be too narrow in the wrong way — check this yourself

The track wants an advisor that **adapts to different users**. Read the tip:

> "Would my advisor give the same recommendation to everyone? If yes, it
> probably needs more personalization."

Insurance Buddy asks for **insurer, class, city**. It does not adapt to age,
experience, budget or preference — and for good reason: those genuinely do not
change which hospital accepts your card.

**This is defensible, but you must argue it explicitly in the PDF**, or a judge
will read it as un-personalised. The project's own note already has the answer:
segments are defined by *behaviour* (plan changed / choosing between plans /
family coverage / chronic condition), not demographics. Write that argument.
It is one of your strongest points — do not leave it implicit.

### 2. Three user profiles are missing

Required, due 6 Nov, still not written. And required to be *behaviourally*
different, which your scope already supports:

- Plan just changed (new job, new city)
- Choosing between two plans at enrolment
- Chronic condition needing continuity of care

For each: who, what they need, what the AI must consider. Then **show the
advisor answering each differently** — that is the evidence a judge looks for.

### 3. `997` — CONFIRMED

Confirmed by the team on 18 November 2026 as the Saudi Red Crescent ambulance
number. No change needed to the prompt.

**For the PDF:** cite the source in References (Saudi Red Crescent Authority).
A judge checking a health app's emergency number is a reasonable thing to
expect; having the citation ready is what turns a claim into a sourced fact.

---

## The two blockers, and they are due today

Both are pass/fail items. Neither is a document — both are links.

**Link 1 — the chatbot.** The app is built and tested. It is not deployed. The
GitHub repo `siudro/insurance-buddy` is still private. Deployment needs the repo
owner's account; I cannot do it.

**Link 2 — the chat history.** Needs ≥10 exchanged messages against the
**final edition**. You have a script (`TASK6_CHAT_HISTORY.md`) but not a
recording. A script is not evidence.

**These two are the same 15 minutes of work.** Deploy, then have the
conversation on the live app.

---

## The order that actually gets you to 23 November

| Now | Deploy, then do the 10-message chat live | both links, today |
|---|---|---|
| Next | Three user profiles | 30 min, you write them |
| Next | Limitations + Future Development | 30 min, you have the material |
| Then | Iterative process write-up | the v4→v10 log is already evidence |
| Then | References (APA) | list the insurer locator URLs |
| Last | Assemble PDF, create Drive folder, share | 23 Nov |

Folder must be named `LLM_ProjectName` inside the **LLM** parent
(`1n-ZZ4hAPPVBYmYkg7ZHIu8CVXGhv_idg`). No category segment — this track has none.

---

## What is NOT required (do not spend time on it)

The rubric says advanced capabilities are **optional**, and judged only on
whether they add value. That means:

- Wkala integration — optional. Already built; do not polish it further.
- Docker, backend, FastAPI — infrastructure for the demo, not scored.
- Making it faster than 4 ms — already far past what a judge can perceive.

**Do not do more engineering. Do the paperwork.**

---

## The one question I need answered

**Are you the student on this project, or are you coordinating on someone
else's behalf?**

The track requires the PDF drafted by the team, and the profiles and chat
history to be the team's own. If you are coordinating, Sedra needs to know that
these three written items are hers to produce — they are scored artefacts.

I will not write the profiles, the rubric argument, or the PDF prose for you,
because those are the things being graded. I will structure them, check them,
and tell you what a judge will mark down.
