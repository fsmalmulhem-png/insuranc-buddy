# Al Sagr — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.alsagr.com/robots.txt` | 200 — crawlable | Confirming access |
| 2 | `https://www.alsagr.com/sitemap.xml` | 200, redirects to SPA | No provider routes |
| 3 | `https://www.alsagr.com/` | 200 → `alsagr.com/Ecommerce/#/home` | Homepage copy ("48 products"), contact 8003040114 |
| 4 | `https://alsagr.com/Ecommerce/#MEDMAL_Product` | 200 via proxy — full content | **Primary source**: the whole medical FAQ, including the TCS route |
| 5 | `alsagr.com/Ecommerce/assets/Templates/*.pdf` (23 enumerated) | Listed in site markup | Proving no network PDF exists among them |
| 6 | `Template1–6.pdf` (direct) | 404 | Stale links; confirms no hidden medical content there |
| 7 | `https://www.tcs-ksa.net/` — direct | Timeout (25s) | TCS unreachable |
| 8 | `https://www.tcs-ksa.net/` — text proxy | 422 connection failure | Same |
| 9 | `https://tcs-ksa.net:2050/` — proxied | 422 | Same |

## Numbers captured, and where each came from

| Number | Source | Purpose |
|---|---|---|
| **8003037858** | FAQ `tel:` link | TCS — medical network enquiry, 24/7 |
| **920012493** | FAQ `tel:` link | TCS — medical network enquiry, 24/7 |
| **920001043** | FAQ text + `wa.me` link | Al Sagr sales, WhatsApp available |
| **8003040114** | Site header | Al Sagr central contact |

All four are Al Sagr's own published numbers, not a directory listing.

## Portal URL

`https://www.tcs-ksa.net:1192/` — the TCS member lookup Al Sagr points to, taking National ID
and year of birth. Recorded as published; not exercised, because the host is unreachable from
this environment and the portal requires a member's ID.

## App links

Al Sagr's FAQ publishes two shortened links for "Alsagr Health":
`2u.pw/T9pT8co3` (Android) and `2u.pw/vck54pi6` (iOS). Recorded as given; not resolved.

## A note on the site's plumbing

`alsagr.com` serves its retail app at `/Ecommerce/` as an Angular SPA. Direct requests to that
path return **404**, while the proxy-rendered page works — the app answers only with a browser
context. Consequence: hash routes like `#/Network` cannot be probed by URL, and all 200
responses to such probes are the shell, not content. Anyone re-checking this should treat a 200
from a hash route as meaningless.

## Nothing from outside alsagr.com informs this skill

No third-party directory was adopted. TCS is named *by Al Sagr*, which is why it appears here —
it is the insurer's own administrator, not a secondary source.
