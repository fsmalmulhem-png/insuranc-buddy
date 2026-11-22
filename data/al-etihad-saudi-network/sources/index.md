# Al Etihad — sources checked

All checks done on **11 November 2026**.

| # | URL | Result | Meaning |
|---|---|---|---|
| 1 | `https://www.aletihad.com.sa/` | 200 — body reads **"Comming soon"** (13 bytes) | The live site has no content |
| 2 | `https://www.aletihad.com.sa/robots.txt` | 404 | No robots file |
| 3 | `https://www.aletihad.com.sa/sitemap.xml` | 404 | No sitemap; no routes to enumerate |
| 4 | `http://archive.org/wayback/available?url=aletihad.com.sa` | Closest snapshot `20250416095725` | An archived copy exists |
| 5 | Wayback CDX (`url=aletihad.com.sa*`) | Three captures only: `/`, `/robots.txt`, `/favicon.ico` | **No product or document page has ever been archived** |
| 6 | `http://web.archive.org/web/20250416095725id_/https://aletihad.com.sa/` | 200 — **"Comming soon"** | Archive matches live; site has been a placeholder for years |

## The date range

Oldest capture in the CDX index: **26 November 2021**. Newest: **16 April 2025** (and the live
page on 11 November 2026 reads the same). So the placeholder state spans at least four and a
half years — this is not a temporary outage or a recent migration.

## What was deliberately not done

- **No phone number was invented.** The site publishes none, so the skill must not supply one.
  A fabricated contact number would send a member somewhere wrong.
- **No product names were inferred** from other Saudi insurers, the CCHI register, or industry
  convention. If Al Etihad sells health insurance, this skill cannot say what it is called or
  what it covers, because nothing authoritative was found.
- **No third-party directory was adopted**, for the same reason recorded in the other skills:
  undated, unverifiable, and not the insurer's own publication.

## Note on the search attempts

Bing was queried for Al Etihad's insurance products and returned unrelated results (a US
shopping site among them). No usable second source was found. The finding stands on the
company's own domain, which is the right place for it: if the insurer publishes nothing, the
correct statement is that it publishes nothing.

## What would change this

If `aletihad.com.sa` stops saying "Coming soon", or if the company is identified under a
different domain, this file should be re-run. Both can be checked in under a minute.
