---
name: amana-coop-saudi-network
description: Amana Cooperative Insurance (التعاونية أمانة / amana.sa) — one of only two companies in this set that publishes full provider network PDFs, with Class A/B/C networks split into Advance/Elite/Standard. Read when the user's company is Amana, to name a provider from the city tables and state which published network list it came from.
---

# Amana Cooperative Insurance — real network files, Class A/B/C structure

## Status

**The second company in this set with actual provider lists.** Amana publishes **two network
PDFs openly on its homepage**, dated **21 May 2026**:

- `Amana-Full-Network-21-05-2026-Existing-Policies.pdf` — **49 pages**
- `Amana-SME-Network-Basic-21-05-2026.pdf` — **43 pages**

Converted into **159 city files** holding **1,851 unique providers** — more than Bupa's 1,181.

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Amana** and still not accept the member's class. This skill works at
**class level** and names providers only from the converted tables, always stating which
published list the provider came from.

---

## The network structure — verified from the PDFs

Amana splits its network **twice**: first by class, then by sub-tier.

### The Full network (existing policies, effective before 14-04-2026)

| Class | Sub-tiers |
|---|---|
| **VIP** | Advance, Elite, Standard |
| **A** | Advance, Elite, Standard |
| **B** | Advance, Elite, Standard |
| **C0222** | Advance, Elite, Standard |
| **C** | CVT, 0333, 0444 |

### The SME Basic network

| Network |
|---|
| SME **VIP** |
| SME **A** |
| SME **B** |
| SME **X** (0444) |
| SME **R** (0555) |

So "Class A" and "Class B" are **real, published classes** at Amana — with three sub-tiers each.
This is the second company (after Saudi Enaya) where a card's A/B can be placed.

## What this skill CAN do — and what it cannot

**Can:** name a provider in a city, its type, its owner (Private / MOH), and its telephone, and
say which of the two published lists it appears on.

**Cannot (honestly):** say *which sub-tier* (Advance / Elite / Standard) a provider belongs to.
The PDFs encode that as a row of tick marks across 13–21 columns, and the column count is not
consistent across pages, so the tick-to-network mapping cannot be recovered reliably from the
text extraction. **Do not infer a sub-tier.** Say the provider is in the list, name the list, and
have the member confirm the sub-tier with Amana.

That limitation is recorded in `network/README.md` rather than papered over.

---

## What the agent must do for an Amana user

1. Confirm the company is Amana Cooperative Insurance (Arabic: التعاونية أمانة). If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). Amana publishes both, plus VIP and C.
3. Ask the city and the service.
4. Look the provider up in `network/<city>.md` and **name it**, citing the published list it
   appears on and the date (21 May 2026).
5. **Do not claim a sub-tier** (Advance/Elite/Standard) unless the user states it — the data
   here does not carry it. Offer: *"confirm with Amana which sub-tier your plan uses."*
6. Always give the hospital question as a final check:
   *"Do you bill Amana Class [A/B] directly?"*

Contacts, published on the homepage: **inside KSA 8001240242**, **outside KSA +966114847800**,
**medical approvals 920002039**.

---


### The answer block — use this shape every time

1. **What they hold:** Amana medical policy — SME or corporate.
2. **Class:** VIP, A, B, or C0222 / C for the full network; SME VIP/A/B/X/R for SME.
3. **What to do next:** look the provider up in `network/<city>.md` and name it, stating which
   published list it came from. Do **not** claim a sub-tier (Advance/Elite/Standard) — that data
   could not be recovered.
4. **Always ask the hospital:** *"Do you bill Amana Class [X] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, network structure, procedure. |
| `tiers-and-packages.md` | The class/sub-tier structure in full. |
| `network/<city>.md` | **159 city files**, 1,851 providers. |
| `network/README.md` | Conversion method, the tick-mark limitation. |
| `sources/index.md` | Both PDF URLs, dates, page counts. |

---

## Note on the URL supplied

`amana-coop.com.sa` **has no DNS record**. `amana.com.sa` is a Riyadh **accounting firm**. The
insurer is **`amana.sa`** (with `amanainsurance.com` as an older site). Recorded in
`sources/index.md`.

---

## Change log

- 2026-11-11 — skill created. Two network PDFs downloaded and converted into 159 city files
  (1,851 providers). Sub-tier tick mapping not recoverable; documented, not guessed.
