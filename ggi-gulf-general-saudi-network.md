---
name: ggi-gulf-general-saudi-network
description: Gulf General Cooperative Insurance (الخليجية العامة / ggi-sa.com) — publishes an SME provider network PDF, but its CCHI accreditation dates have almost all lapsed (only 2 of 423 still valid as of Nov 2026). Read when the user's company is Gulf General / GGCI, to explain the file exists but is stale and hand them the verification route.
---

# Gulf General Cooperative Insurance (GGCI) — a list that has mostly expired

## Status

**GGCI publishes a real provider list — but it is effectively out of date.**

Its SME network PDF (13 pages, dated **14 September 2025**) carries provider names, CCHI
accreditation numbers, expiry dates, class marks and telephones. That is genuinely the most
complete single network file found in this project.

**But 421 of its 423 accreditations have expired.** Only **2** remain valid as of
11 November 2026. Presenting the other 421 as "hospitals you can use" would send members to
facilities whose GGCI accreditation has lapsed.

Verified 11 November 2026. See `sources/index.md` and `network/README.md`.

---

## The rule this skill exists to protect

A hospital may accept **GGCI** and still not accept the member's class — and here, it may not
accept GGCI at all any more. This skill therefore:

- **may name a provider only as "listed in GGCI's Sept-2025 file"**, never as "covered today";
- **states the accreditation expiry** with every name it gives;
- **warns** that the list is stale and must be re-confirmed with GGCI.

---

## The data — what the file contains

| Column | Example |
|---|---|
| Provider name (EN) | `AL MOUWASAT HOSPITAL- JUBAIL` |
| CCHI No | `1086` |
| Expire Date | `18-May-2027` |
| Class mark (الفئات) | `RF` / `•` / `• 01` / `RF 01` |
| Telephone | `9200 02258` |
| Provider name (AR) | مجمع شعاع الطبي |

**423 provider rows across 59 cities.**

## The expiry problem — the central finding

| | Count |
|---|---|
| Total providers in the file | 423 |
| **Accreditations still valid on 11 Nov 2026** | **2** |
| Expired | **421** |

The **only two still valid**:

| Provider | City | Valid to |
|---|---|---|
| **AL MOUWASAT HOSPITAL – JUBAIL** | Jubail | 18 May 2027 |
| **AL QUWAYIYAH GENERAL HOSPITAL (MOH)** | Al Quwayiyah | 1 Feb 2027 |

Every other provider's accredited validity ended between **Dec 2025 and late 2026**.

**What this means:** the file is a snapshot of September 2025. It is not wrong — it was accurate
when published. It is **expired**. Either GGCI has re-accredited most providers and not
republished the list, or its SME network has shrunk dramatically. **The skill cannot tell which,
and must not guess.**

## The class marks — also unexplained

The `الفئات` column holds codes without a published legend:

| Mark | Providers |
|---|---|
| `RF` | 207 |
| `•` | 191 |
| `• 01` | 15 |
| `RF 01` | 10 |

`RF` plausibly means Referral, and `01` a tier — but GGCI does not say, so the skill carries the
mark verbatim and never translates it into a class name.

---

## What the agent must do for a GGCI user

1. Confirm the company is Gulf General / GGCI (Arabic: الخليجية العامة للتأمين). If unsure which
   Gulf insurer they hold, ask — there are several.
2. Ask the class on their card and the city.
3. **Lead with the currency warning**, not the provider name:
   > "GGCI last published its SME network in September 2025, and almost every accreditation in
   > that file has since lapsed. I can tell you what the file says, but you must confirm before
   > travelling."
4. If their hospital is one of the **two still-valid** entries, say so with the date — that is a
   real, current fact.
5. Otherwise, name the provider **only as a September-2025 listing**, and give its expiry date so
   the user sees why it needs confirming.
6. Give the contacts: **920012654** (unified), **8002440054** (toll-free), WhatsApp
   `966920012654`.
7. Give the hospital question: *"Do you bill Gulf General [class] directly?"*

---


### The answer block — use this shape every time

1. **What they hold:** GGCI medical policy (SME network).
2. **Class:** ask for Class A / Class B; GGCI's file uses marks (RF, •, • 01, RF 01) with no published
   legend.
3. **What to do next:** warn first that the published file is from September 2025 and almost every
   accreditation has lapsed. Then, if relevant, name the provider as a September-2025 listing with
   its expiry date. Contacts: **920012654**, **8002440054**.
4. **Always ask the hospital:** *"Do you bill Gulf General Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the expiry finding, the class-mark limit, procedure. |
| `tiers-and-packages.md` | Products, mark analysis, the expiry table. |
| `network/<city>.md` | 59 city files, each row carrying its expiry date. |
| `network/README.md` | Method, losses, and why the list is flagged stale. |
| `sources/index.md` | Every URL and result. |

---

## Change log

- 2026-11-11 — skill created. SME network PDF (14 Sep 2025) parsed: 423 providers, 59 cities.
  **421 of 423 accreditations expired**; only 2 valid. Skill flags the file as stale rather than
  presenting it as current coverage.
