# GIG — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.gig.sa/` | 200 — 41,711 bytes → `/ar/` | Identity, nav, contact 8001160020 |
| 2 | `https://www.gig.sa/robots.txt` | 200 — 247 bytes | Crawlability |
| 3 | `https://www.gig.sa/sitemap.xml` | 200 — 17,766 bytes | **Route enumeration; found `provider-locator`** |
| 4 | `https://www.gig.sa/provider-locator/` | 200 — **3,269,646 bytes** | **All 3,437 providers embedded in HTML** |
| 5 | `https://www.gig.sa/business/employee/group-healthcare-insurance/` | 200 — 27,189 bytes | **Network benefit tables** |
| 6 | `https://www.gig.sa/healthcare-quote/` | 200 | Quote flow, exists |

## The locator page — why this worked

The page is **3.27 MB** and contains **3,437 hidden provider blocks** in its markup:

```
class="providerEntry hidden"  →  3,437 occurrences
```

Each carries `data-city`, `data-network`, `data-providertype`, plus name, group, address and
telephone. The locator's own JavaScript filters these client-side by city, network and provider
type — but the full dataset ships with the page, which is why it could be extracted without an API.

That is unusual and worth recording: most locators fetch per query. GIG ships everything at once.

## Site structure

WordPress-based, Arabic-first (`/ar/`), with English at the root. URLs for individual products use
Arabic slugs (`/ar/الأفراد/تأمين-المركبات/`). The sitemap is real XML and lists both language trees.

## Contact

**8001160020** — from the header `tel:` link, site-wide.

## Sitemap findings

The sitemap's health-related entries:

- `/business/employee/group-healthcare-insurance/`
- `/healthcare-quote/`
- **`/provider-locator/`**

Three health-related routes, one of which is the complete provider directory.

## Nothing from outside gig.sa informs this skill

No third-party directory was used or needed. The provider data is GIG's own publication, which is
what makes this the strongest dataset in the set.
