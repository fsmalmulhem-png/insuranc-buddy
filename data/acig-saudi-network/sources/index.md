# ACIG — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.acig.com.sa/` (direct) | 200 — 18,308 bytes, Angular shell | Company identity, Arabic name, meta description listing health insurance |
| 2 | `https://www.acig.com.sa/main-SU6B3345.js` | 200 — 740 KB | **Primary source**: complete route list, product IDs, contact numbers |
| 3 | `https://medonline.acig.com.sa/MemberPortal/` | 200 — 6,362 bytes | Member portal identified as "Toshfa" |
| 4 | `https://medonline.acig.com.sa/MemberPortal/main.840b04bd1ff69384.js` | 200 — 3 MB | **Primary source**: provider components, auth guards, API base |
| 5 | `https://medonline.acig.com.sa/Ecommerce/` | 200 — 74 KB | Portal sister app |
| 6 | `acig.com.sa/robots.txt`, `/sitemap.xml` | Proxy timeout (422) | — |
| 7 | `acig.com.sa/download-center`, `/frequently-asked-questions` | 200 but identical SPA shell; proxy 422 | Confirmed no server-rendered content |
| 8 | `/MemberPortal/Provider`, `/MemberPortal/ProviderOnline` | 404 | Confirmed guarded |

## Contact numbers, and where each came from

| Number | Source in bundle | Purpose |
|---|---|---|
| **8001246999** | `href="tel:8001246999"` | ACIG support / contact container |
| **920012331** | `window.open("https://wa.me/966920012331")` | WhatsApp support |

Both are taken from real `tel:` / `wa.me` links in ACIG's own bundle, not from a directory.

## Routes extracted from the public bundle

`home`, `about-acig`, `all-products`, `products`, `individuals-insurance`,
`company-insurance`, `business`, `services`, `claims`, `customer-service`,
`frequently-asked-questions`, `download-center`, `branches`, `contact-us`, `media-center`,
`complaints`-family (`add-complaint`, `complaint-procedures`), `jobs`,
`cancel-business-insurance`, `cancel-medical-insurance`, `requirements`, `mediation-center`,
`privacy-policy`, `report-fraud`, `report-violation`, `most-common`, `maintenance`.

**No `network`, `providers`, `hospitals` or `hospitals`-equivalent route exists.** That is the
decisive enumeration: the public site has no provider page to read.

## Sites referenced by the bundle

- `eservices.acig.com.sa` — endorsements
- `medonline.acig.com.sa` — Toshfa member portal + ecommerce
- `onlinegeneralclaims.acig.com.sa` — non-motor claims
- `tech.acig.com.sa` — ACIG Tech

None of these publishes a provider list.

## Method note

This site is a pure client-rendered SPA: every HTML route returns the same shell, so page text
could not be read directly and the text-rendering proxy timed out on most routes. The reliable
route was to fetch and parse the JavaScript bundles, which is where the routes, product IDs and
contact numbers above came from. Anyone re-checking should do the same rather than fetching the
HTML.
