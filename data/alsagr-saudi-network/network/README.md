# Al Sagr — the network, and how a member reaches it

## Al Sagr publishes no provider file — but it publishes the way to the answer

No city files exist in this skill. What exists instead is Al Sagr's own published procedure for
a member to check their network, reproduced here in full because it is the single most useful
thing any of the seven companies has provided.

## The published route — verbatim from Al Sagr's FAQ

Al Sagr's FAQ asks **"كيف أستفسر عن الشبكة الطبية؟"** (*How do I enquire about the medical
network?*) and answers:

> The medical network is managed by **TCS** (the medical claims administrator). Three routes:

| # | Route | Detail |
|---|---|---|
| 1 | **Call TCS** | `8003037858` or `920012493` — **24/7** |
| 2 | **Alsagr Health app** | Android: `2u.pw/T9pT8co3` · iOS: `2u.pw/vck54pi6` |
| 3 | **TCS web portal** | `https://www.tcs-ksa.net:1192/` — enter **National ID** and **year of birth** |

The FAQ also gives Al Sagr's own lines: sales/WhatsApp **920001043**, central **8003040114**.

This is a complete answer to "is hospital X covered for me?" — requiring only the member's own
National ID. It is a *lookup*, not a *list*.

## Why it cannot be converted into city tables

- **It is member-scoped.** It answers for the person whose National ID is entered, against the
  network attached to *their* policy. Different members of the same employer can get different
  answers if their classes differ.
- **It is behind a form.** No bulk query, no export, no download.
- **TCS is not reachable from this environment.** Direct requests to `tcs-ksa.net` time out
  (25s+), on both the main host and port 2050; the text proxy returns 422 on connection.
  Portal port 1192 could not be exercised.

So the route is documented and handed to the user, not harvested. That is the correct outcome:
it genuinely solves the member's problem, and it does so without the advisor guessing.

## What was checked on Al Sagr's own site

| # | Attempt | Result |
|---|---|---|
| 1 | `alsagr.com/robots.txt` | 200 — crawlable |
| 2 | `alsagr.com/sitemap.xml` | 200, but redirects into the SPA; no provider routes |
| 3 | Retail portal (`/Ecommerce/`) | Angular SPA. Products: Motor, Travel, Property, Medical Malpractice — **no health for individuals** |
| 4 | Medical Malpractice product page | Loaded; carries the FAQ above |
| 5 | `assets/Templates/*.pdf` (23 files enumerated) | All governance, financials and policy wordings. **No network file** |
| 6 | `Template1–6.pdf` probed directly | 404 — those links are stale |
| 7 | Hash-route probes (`#/Network`, `#/Hospitals`, …) | All return the SPA shell; routes do not exist |
| 8 | TCS host, direct and proxied | Unreachable |

## What would legitimately deepen this skill

1. **A member exporting their Alsagr Health app network** — would give one policy's real list.
2. **TCS's own directory**, if it is ever published — TCS administers networks for several
   Saudi insurers, so it may hold a superset.
3. **A policy pack** — Al Sagr or TCS may ship a network booklet with the card.

## What the agent does instead

Hands the member TCS's 24/7 numbers and the app, and still gives them the hospital question.
See `../SKILL.md`.
