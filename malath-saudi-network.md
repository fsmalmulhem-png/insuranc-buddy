---
name: malath-saudi-network
description: Malath Insurance (Malath / ملاذ للتأمين التعاوني) health products and their published network. Read only when the user's company is Malath, and only to state which product/class they hold and to hand them the verification route. This skill holds no provider names — do not name a hospital for a Malath member.
---

# Malath Insurance — health products and what is published

## Status

**Products known. Network list NOT obtainable.** Malath does publish a medical network as a
downloadable PDF — `Malath_Medical_Network_List_R.pdf`, linked from its Downloads and
Products pages — but the file could not be retrieved: Malath's host is unreachable from this
environment, the PDF itself was never archived, and the copy is dated 2018. **No provider
may be named for a Malath member from this skill.**

See `network/README.md` for the retrieval attempts in full.

---

## The rule this skill exists to protect

A hospital may accept **Malath** and still not accept the member's plan or class. This skill
never answers at company level. Because it holds no provider names, its only correct
provider answer is **"I cannot confirm this"**, plus the hospital's phone number and the exact
question:

> *"Do you bill Malath [class] directly?"*

---

## What Malath sells in health — verified

Malath lists these health products:

| Product | Malath's own description | Network published? |
|---|---|---|
| **Medical Insurance program for SME** | Small & medium establishments. Malath states it "has a various number of **plans and classes**..." | A 2018 network PDF is linked — not retrievable |
| **Health Insurance** (group / corporate) | "Group health insurance — grants for the staff of institutions, bodies and companies in the form of a group contract." Covers in-patient, out-patient, or comprehensive | No |
| **Medical Malpractice Insurance** | Professional liability for practitioners, not member treatment | Not applicable |

Malath states all health products are CCHI-compliant, and that higher classes get
"additional upgraded benefits as per employer's interests".

### The important detail: Malath says "classes"

This is the only one of the four companies checked so far whose own public wording uses the
word **classes** for its SME health tiers. That is worth noting, because it is the closest any
insurer has come to the Class A / Class B vocabulary printed on member cards.

But note what is *not* established:

- Malath does not publish **how many** classes there are, **what they are called**, or
  **which class is A or B**.
- It does not publish which providers belong to which class.
- "Classes" in Malath's sentence may be internal commercial categories rather than the
  Class A / Class B a card prints. **Do not assume they are the same thing.**

So a Malath user saying "Class B" tells you they are on one of Malath's classes — but not
which one, and not what it covers. Do not pretend otherwise.

## What is known to be absent

- No class-by-class provider table on the public site.
- No city-level network breakdown.
- No current (post-2018) network file found.
- No online provider lookup equivalent to Tawuniya's.

---

## What the agent must do for a Malath user

1. Confirm the company is Malath. If not, do not use this skill.
2. Ask the class shown on the card (Class A / Class B). If they do not know, say where to look
   and wait.
3. Ask whether it is an **SME/employer plan** or an individual/group policy — this changes who
   can answer the network question.
4. Ask the city and the service.
5. **Do not name a hospital.** Say plainly that Malath publishes a network list but you cannot
   confirm a provider for their class.
6. Give them what does work:
   - **Call Malath — 9200 15815** (the call-centre number printed site-wide), and ask for
     their class's hospital network.
   - **Ask the hospital directly:** *"Do you bill Malath Class [A/B] directly?"*
7. State that coverage and networks change, and that an employer contract can fix the class,
   so confirm before travelling.

Contact details verified from Malath's own Contact page: call centre **9200 15815**, email
`info@malath.com.sa`, head office Riyadh `011 4168222`.

---


### The answer block — use this shape every time

1. **What they hold:** Malath medical policy — SME or individual.
2. **Class:** ask for Class A / Class B; Malath never defines its classes publicly.
3. **What to do next:** call **9200 15815**. Note the published network PDF is from 2018 and could not
   be retrieved.
4. **Always ask the hospital:** *"Do you bill Malath Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, products, the "classes" wording, and the agent procedure. |
| `tiers-and-packages.md` | Malath's health products and what its class wording does and does not tell you. |
| `network/README.md` | The network PDF that exists, every retrieval attempt, and what would close it. |
| `sources/index.md` | Every URL checked, including which came from the archive. |

---

## A note on how this skill's facts were obtained

The live Malath site could not be reached from this environment (connection timeouts on both
IPs). The product, contact and downloads pages were read from **Internet Archive snapshots**.
That is why every page carries a date and why the network PDF — never archived, and 2018 even
at its newest — is treated as unavailable rather than invented. See `sources/index.md`.

---

## Change log

- 2026-11-11 — skill created. Products and contact details read from archived snapshots of
  malath.com.sa. A medical network PDF is linked by Malath but was not retrievable; skill
  holds no provider data and refuses to name hospitals.
