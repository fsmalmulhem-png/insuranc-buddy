# "Integrated Insurance" — sources checked

All checks on **11 November 2026**.

## The domain does not exist

| # | Check | Result |
|---|---|---|
| 1 | `getent hosts integratedinsurance.com.sa` | **No output** — no DNS record |
| 2 | `getent hosts www.integratedinsurance.com.sa` | **No output** |
| 3 | Direct `curl` | `curl: (6) Could not resolve host` |
| 4 | Text proxy | **422** |
| 5 | `archive.org/wayback/available?url=integratedinsurance.com.sa` | `{"archived_snapshots": {}}` |
| 6 | Wayback CDX, `integratedinsurance.com.sa*` | **0 bytes of results** |

A domain with **no DNS and no archive captures in either direction** was never a live site. This is
not a case of a site being down, blocked, or retired — there is nothing to find.

## What the search returned

Query: `"Integrated Insurance" Saudi Arabia company`

Result: **exactly one match**, `nib.com.sa`, with the snippet:

> "The National Insurance Brokerage is a licensed Saudi company providing **integrated insurance**
> solutions for individuals and businesses: vehicle, medical and marine insurance and more."

So the phrase in the request is NIB's **descriptive copy**, not a company name. No company called
"Integrated Insurance" appears in the Saudi market in this search.

## NIB — what its own site states

| # | URL | Result | Used for |
|---|---|---|---|
| 7 | `https://www.nib.com.sa/en` | 200 — 3,187 bytes | **Broker identity and claims** |
| 8 | `https://www.nib.com.sa/sitemap.xml` | 200 — 12 routes | Confirming no network page |
| 9 | `https://www.nib.com.sa/en/products` | **404** — page does not exist | Confirming no product/network listing |

### Verbatim claims

> "A licensed Saudi **insurance brokerage** company providing customized insurance coverage for
> companies in Saudi Arabia at competitive prices"

> "Licensed by the **Insurance Authority**"

> "We work with more than **20** leading insurance companies"

> "over **15** years of experience in the Saudi insurance market"

> "selecting the appropriate insurance coverage … through most licensed insurance companies in the
> Saudi market"

## Sitemap — the full 12 routes

`/` · `/about` · `/contact` · `/en` · `/en/about` · `/en/contact` · `/en/faq` · 
`/en/news/company-transformation` · `/en/news/digital-platform` · `/en/news/partnership` · 
`/en/privacy` · `/en/regulations`

**No products page, no provider page, no network page.** Consistent with a broker that arranges
cover rather than holding a network.

## Contact

**8001240284** — from NIB's site.

## Method note

This entry differed from every other in the set: the work was **disproving a URL** rather than
reading one. Two independent null results (DNS and Wayback) plus one positive identification (NIB)
were needed before it was safe to say the domain never existed — rather than that it was merely
blocked from this environment, which has been the case for several other companies.

## Nothing from outside the cited sources informs this skill

No third-party directory was used. The broker-versus-insurer distinction is definitional, not
sourced from any single vendor.
