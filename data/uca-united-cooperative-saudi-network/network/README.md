# UCA — network files

## None published, and the site is unreachable

UCA states its medical network is "appointed by the Company" but publishes no list of who is in it.
No city files exist in this skill.

## The live site does not respond

`uca.com.sa` and `www.uca.com.sa` both resolve to **5.149.133.230**, but every connection attempt
times out — direct request (25s), HTTP and HTTPS, and via a text-rendering proxy (422).

This may be a temporary outage, a hosting migration, or a retired site. **The skill cannot tell
which, and does not guess.** If the site returns, the finding should be re-checked.

## The evidence comes from the archive

All content was read from **Internet Archive snapshots** of UCA's own pages:

| Page | Archive result |
|---|---|
| `/products/` | 200 — 155,437 bytes |
| `/company/` | 200 — 167,491 bytes |
| `/faqs/` | 404 in archive |

The newest snapshot used is **14 February 2025**. So the facts about products and licensing are
UCA's, as of early 2025 — not necessarily today.

## What was checked for a network file

| # | Attempt | Result |
|---|---|---|
| 1 | Wayback CDX index for `uca.com.sa*` (500 rows) | Only `MedicalInsurance.js` and `medical.png` icons — **no network PDF or Excel** |
| 2 | Archived `/products/` full text | The "appointed by the Company" sentence; no names |
| 3 | Archived `/company/` | Licensed lines; no network |
| 4 | Live site | Unreachable |

Attempt 1 is the decisive one: the archive index for the whole domain contains no network document.

## What would legitimately fill this skill

1. **The member's policy schedule** — UCA's own text says benefits and network are "as shown in the
   policy schedule". That document is the authoritative source and the member already holds it.
2. **A call to 800 244 4442** asking which hospitals are appointed for a given class.
3. **The Insurance Authority's register**, to confirm UCA's current licensing status if the site
   stays down.

## What the agent does instead

Names UCA's own phrase — "network appointed by the Company" — so the member knows the concept
exists, points them at their policy schedule, and gives the hospital question.
