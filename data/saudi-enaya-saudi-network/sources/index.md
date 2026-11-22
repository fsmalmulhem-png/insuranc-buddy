# Saudi Enaya — sources checked

All checks on **11 November 2026**.

## First: the domain you were given does not exist

| Domain | Result |
|---|---|
| `saudi-enaya.com` (supplied URL) | **No DNS record.** `getent hosts` returns nothing; curl fails with "Could not resolve host" |
| `enaya.com.sa` | Resolves and loads — but it is **دقة العناية**, a Riyadh cleaning and event-services company. Not an insurer. |
| **`saudienaya.com`** | ✅ **The actual company** — Saudi Enaya Cooperative Insurance |

Getting to the right domain took a search for the company name; the insurer's profile points to
`saudienaya.com` (and a `corporate.saudienaya.com` portal). Recorded so nobody repeats the dead
end.

## What was checked on the real site

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://saudienaya.com/` | 200 — 10,510 bytes | Identity, navigation |
| 2 | `https://saudienaya.com/robots.txt` | 200 | Crawlability |
| 3 | `https://saudienaya.com/sitemap.xml` | 200 | Route enumeration; found `network-provider` |
| 4 | `/sme-plan` | 200 — 4,705 bytes | **Primary source**: class table |
| 5 | `/corporate-plan` | 200 — 4,622 bytes | **Primary source**: identical class table |
| 6 | `/policy-benefits` | 200 | Confirms SME + Corporate plan split |
| 7 | `/network-provider` | 200 but **redirects to login** | Proves member gating |
| 8 | `/static/js/main.bd711158.js` | 200 — **1,393,041 bytes** | **Primary source**: three Provider API endpoints |
| 9 | `corporate.saudienaya.com/SEMobileApp/api/…` | Timeout (40s direct; 422 proxied) | Endpoint recorded, not exercised |

## Contact numbers, from the bundle

| Number | Source | Purpose |
|---|---|---|
| **8001240551** | `tel:` link in bundle | Main line |
| **920001177** | `tel:` link in bundle | Contact centre |

## Endpoints found, for the record

```
/Provider/GetNetWorkList
/Provider/GetNetWorkListByFilter
/Provider/GetNetWorkFilterDetails
base: https://corporate.saudienaya.com/SEMobileApp/api
```

Request shape observed in the bundle: `{ Region, ServiceProvider, ServiceOffered, PolicyNo, MemberNo }`
plus `IdentityNo` in the login flow. This is a **per-member** provider query.

## A note on the class table's strength of evidence

The tables on `/sme-plan` and `/corporate-plan` were compared line-by-line and are **identical**
— same classes, same network codes, same limits. That matters because it means the class
structure is the insurer's standard product architecture, not an artefact of one page.

## Nothing from outside saudienaya.com informs this skill

No third-party directory was adopted. The `enaya.com.sa` finding is recorded only to explain the
dead end, and no content from it was used.
