---
name: al-etihad-saudi-network
description: Al Etihad Insurance (aletihad.com.sa) — its website is an unbuilt placeholder, so nothing about its health products, tiers or hospital network is publicly available. Read only when the user's company is Al Etihad, to say plainly that nothing is published and hand them the verification route. Holds no data at all — never name a hospital.
---

# Al Etihad Insurance — nothing is published

## Status

**Nothing known. The website is a placeholder.** `aletihad.com.sa` serves a single page
reading **"Comming soon"** — 13 bytes of text, no navigation, no products, no contact
details, no robots file, no sitemap. It has been in that state in every capture the Internet
Archive holds, the oldest from **2021** and the newest from **2025**.

Verified 11 November 2026. See `sources/index.md`.

---

## What this means for the skill

This is not a conversion that failed, and it is not a site that blocks crawlers. **There is no
content to read.** The domain resolves and answers, and the answer is a coming-soon page.

So this skill:

- knows **no** Al Etihad product names,
- knows **no** tiers or classes,
- knows **no** providers, cities or phone numbers,
- and therefore **must not answer anything about Al Etihad coverage.**

---

## The rule this skill exists to protect

A hospital may accept **Al Etihad** and still not accept the member's class. This skill cannot
even establish the company level, let alone the class level. Its only correct answer is
**"I cannot confirm this"**, plus the exact question to ask the hospital:

> *"Do you bill Al Etihad Class [A/B] directly?"*

---

## What the agent must do for an Al Etihad user

1. Confirm the company is Al Etihad Insurance. If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and
   wait — this is still worth asking, because the hospital will need it.
3. Ask the city and the service.
4. **Say plainly that you cannot confirm anything.** Do not guess product names, tiers, or
   whether Al Etihad even offers the product they hold. Do not name a hospital.
5. Give them what does work — the sources that do not depend on Al Etihad's website:
   - **The card and policy documents**, which carry the insurer's contact number and the policy
     number. The member already holds these.
   - **CCHI's insurance-status service** — `eservices.chi.gov.sa` — which lets a member check
     that their policy is active and in force. This does not list providers, but it does confirm
     the member is covered at all.
   - **Ask the hospital directly:** *"Do you bill Al Etihad Class [A/B] directly?"*
6. State that you are not able to confirm this company's network, and that the member should
   contact the company using the number on their card before travelling.

### The answer block — use this shape every time

1. **What they hold:** Al Etihad policy. What it covers is unknown; their site publishes nothing.
2. **Class:** ask for Class A / Class B. It is worth asking — the hospital will need it.
3. **What to do next:** use the number printed on their card or policy, and check the policy is
   active at `eservices.chi.gov.sa`. Do not invent a number.
4. **Always ask the hospital:** *"Do you bill Al Etihad Class [A/B] directly?"*

**Do not invent a phone number for Al Etihad.** None is published on the site, and a
fabricated number is worse than no number.

---

## Why this is worth recording rather than skipping

For the write-up, this is the far end of the publication spectrum. Five companies checked:

| Company | What its public site gives a member |
|---|---|
| Bupa | Network files, per level |
| MedGulf | Tier names and provider counts |
| Arabian Shield | One paragraph saying the network is "wide and distinctive" |
| Tawuniya | A search box (no file) |
| **Al Etihad** | **"Coming soon"** |

That ordering measures disclosure directly, and Al Etihad is the case where a member has
literally no public route to an answer — only the card, the insurer's phone line, and the
hospital's own reception desk.

---

## If the project needs Al Etihad coverage

The website will not help until it is built. Realistic routes, none of which are built:

1. **The member's own card pack** — an Al Etihad policy document will carry the insurer's
   number and likely a network booklet.
2. **A call to the company** using the number on the card.
3. **CCHI** — `eservices.chi.gov.sa` confirms whether a policy exists and is active, and
   households in Saudi Arabia are regulated through it. It does not list providers.
4. **The hospital's reception desk** — the fallback the whole project is built around.

Record in the write-up that Al Etihad's website was checked on a given date and was a
placeholder; if it is built later, this skill should be revisited.

---

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status and the agent procedure. |
| `network/README.md` | What was checked and what was found. |
| `sources/index.md` | The URLs and their results. |

---

## Change log

- 2026-11-11 — skill created. `aletihad.com.sa` serves a "Comming soon" page in every capture
  from 2021 to 2025. Skill holds no data and refuses to answer about Al Etihad coverage.

