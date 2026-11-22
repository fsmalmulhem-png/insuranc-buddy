# MEDGULF — sources checked

Every URL below was opened on **11 November 2026**. The result column is what happened.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.medgulf.com.sa/robots.txt` | 200 — Allow all, sitemap at `/home/sitemap.xml` | Finding the real sitemap (the root `/sitemap.xml` is a 404) |
| 2 | `https://www.medgulf.com.sa/home/sitemap.xml` | 200 — **50 routes** | Enumerating every route; proving no network/download route exists |
| 3 | `https://www.medgulf.com.sa/home/riadi-sme-health-insurance` | 200 — full content | **Primary source**: five RIADI tiers, provider counts, starting prices |
| 4 | `https://www.medgulf.com.sa/home/napd-program` | 200 — redirects to the RIADI page | Same content, confirms no separate network page |
| 5 | `https://www.medgulf.com.sa/home/group-health` | 200 — nav/footer shell only | No tier table, no provider list |
| 6 | `https://www.medgulf.com.sa/home/faqs` | 200 — full content | Contact numbers: health care 8001188555 (24/7), sales 920024292 |
| 7 | `https://www.medgulf.com.sa/home/mobile-application` | 200 — content | App description; no provider list |
| 8 | `https://www.medgulf.com.sa/home/network` and 3 similar guesses | 200 but SPA shell | Routes do not exist; server answers any unknown path with the app frame |
| 9 | `https://www.medgulf.com.sa/home/main.bc094c72e1aaa88a.js` | 200 — 2.2 MB | **Decisive**: no network/provider/hospital API endpoint in the client bundle |
| 10 | `https://www.medgulf.com.sa/sitemap.xml` | 404 | Confirms the sitemap lives under `/home/` |

## What the site is built with

Angular single-page app, `<base href="/home/">`, bundles served from `/home/`. API host is
`mg-prodapi.medgulf.com.sa` with only motor and SME-client endpoints in the public bundle.

## Notable: this site was open, unlike Tawuniya's

Direct HTTP requests to `medgulf.com.sa` succeed (200) — the site does not block crawlers.
That matters for the comparison in the write-up: MEDGULF is crawlable and still publishes no
provider list. That is a stronger finding than Tawuniya's: Tawuniya could plausibly argue the
list exists but is gated; MEDGULF's absence is a **publication choice**, not a bot defence.

## Third-party lists not used

No third-party provider list was adopted. Any that exist would be undated, employer-specific
and unverifiable — the same reasoning recorded in the Tawuniya skill's sources file. The one
search performed was rate-limited before returning usable results, so none were even
inspected in detail; nothing from outside MEDGULF's own domain informs this skill.

## Prices — provenance note

The "Starting from" figures (220 / 400 / 550 / 1,000 / 1,500 SAR including VAT) are displayed
on the RIADI page alongside each tier. MEDGULF does not state on that page the unit those
prices are per. They are recorded for traceability and ordering only, and must not be quoted
to a user as a cost estimate — this skill's role excludes cost quotes.
