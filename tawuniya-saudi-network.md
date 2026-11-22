---
name: tawuniya-saudi-network
description: The Tawuniya (Tawuniya / التعاونية) medical network in Saudi Arabia — what Tawuniya publishes, what it does not, and why no provider may be named for a Tawuniya member from this skill. Read this only when the user's company is Tawuniya.
---

# Tawuniya — what it publishes, and why this skill names no provider

## Status

**Structure loaded, network data NOT loaded.** Tawuniya publishes its medical network as an
interactive, location-based search on its own website — not as a downloadable file. No
provider list for Tawuniya was obtained. **Do not name a hospital for a Tawuniya member.**

This is not an unfinished conversion. It is the verified state of Tawuniya's public
publication as of 10 November 2026, and it is a finding in its own right. See
`network/README.md`.

---

## The rule this skill exists to protect

A hospital may accept **Tawuniya** and still not accept the member's plan or class. This
skill never answers at company level. Since it holds no provider list, it cannot answer at
plan level either — so its only correct answer is **"I cannot confirm this"**, plus the
hospital's phone number and the exact question:

> *"Do you bill Tawuniya [class/plan] directly?"*

---

## What Tawuniya publishes — verified

| What | Where | Format | Usable as a list? |
|---|---|---|---|
| Network coverage search | `www.tawuniya.com/en/individuals/customer-service/network-coverage` (Arabic: `/ar/individuals/customer-service/network-coverage`) | Interactive map + search box, `Covered / Not covered` per provider | **No** — rendered per query, not a file |
| Download center | `www.tawuniya.com/download-center` | Page exists in the sitemap, but returns a 404 / application error | No |
| Primary providers service | `www.tawuniya.com/services/primary-providers` | Marketing page | No |
| Corporate health | `www.tawuniya.com/corporate` | Marketing page | No |
| Medical SME | `www.tawuniya.com/medicalsme` | Marketing page | No |

Checked and found absent: a network PDF, a network Excel file, a bulk provider endpoint.
The site's pages are a single-page application that blocks automated retrieval (403 to
direct requests, and the route chunk fails to load through a text proxy). Everything above
was confirmed from the public sitemap and the pages that did render.

## Why this matters for the project

Bupa publishes a downloadable network per level — imperfect, but a file a third party can
read. Tawuniya publishes a search box. A member can look themselves up on the Tawuniya site
**if they know which plan they are on**; nobody can compile the list for them, and nobody can
answer "is hospital X in Tawuniya's network for my class" without being that member.

That difference between the two companies is exactly the inconsistency the project's
interviews described — and here it is measurable: one insurer gives you a spreadsheet, the
other gives you a query interface.

---

## The class problem, which Tawuniya also does not solve

Tawuniya, like Bupa, sells health insurance through corporate and SME employers. The plan a
member is on is set by the employer's contract, and the network attached to it can vary by
contract. Tawuniya publishes no mapping from "Class A / Class B" (what cards print) to a
network list.

So even if a provider list existed, the skill would still have to ask which plan or class,
and would still be unable to bridge card wording to network. Record that; do not paper over it.

---

## What the agent must do for a Tawuniya user

1. Confirm the company is Tawuniya. If not, do not use this skill.
2. Ask the class on the card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Tawuniya's network is not in this skill.
5. Say plainly: *"I cannot confirm which Tawuniya providers cover your class — Tawuniya does
   not publish that as a list."*
6. Give them the two things that do work:
   - **Check it themselves on Tawuniya's own page:** `www.tawuniya.com/en/individuals/customer-service/network-coverage` — search the hospital name; it shows Covered / Not covered for their plan.
   - **Ask the hospital directly:** call and ask *"Do you bill Tawuniya Class [A/B] directly?"*
7. State that coverage and networks change and Tawuniya can vary a network by employer
   contract, so confirm before travelling.

---


### The answer block — use this shape every time

1. **What they hold:** Tawuniya medical policy.
2. **Class:** ask for Class A / Class B; Tawuniya publishes no mapping to any network.
3. **What to do next:** search the hospital at
   `tawuniya.com/en/individuals/customer-service/network-coverage`. Note the page defaults to showing
   branch offices — the user must search by hospital name.
4. **Always ask the hospital:** *"Do you bill Tawuniya Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the publication finding, and the exact procedure for a Tawuniya user. |
| `tiers-and-packages.md` | What is known about Tawuniya's plans and the Class A/B gap. |
| `network/README.md` | Why there are no city files, what was tried, and what would close the gap. |
| `sources/index.md` | Every URL checked, the result, and the date. |

---

## Ways this skill could be filled — for the project owner

None of these are built. Listed because they define what "Tawuniya covered" would require:

1. **A member's own lookup** — a Tawuniya member on a known plan searches their hospital and
   reports the answer. Reliable, but only one hospital at a time and needs the member.
2. **A Tawuniya policy schedule** — the employer's schedule lists the network name. Still not
   a provider list, but it names the plan.
3. **A supplier/B2B feed** — Tawuniya has a `become-a-supplier` route; provider directories
   are sometimes available to contracted providers only.
4. **The voice-agent idea already scoped as future work** — calling the hospital and asking
   the exact question is precisely the fallback this skill currently hands to the user.

---

## Change log

- 2026-11-10 — skill created. Tawuniya's public site checked; no downloadable network file
  exists. Skill deliberately holds no provider data and refuses to name hospitals.
