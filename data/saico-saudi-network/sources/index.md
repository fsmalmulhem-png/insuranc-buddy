# SAICO — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.saico.com.sa/robots.txt` | 200 — WordPress default; sitemap at `/wp-sitemap.xml` | Finding the real sitemap |
| 2 | `https://www.saico.com.sa/sitemap.xml` | 200 → `/wp-sitemap.xml` (index, 4 sub-sitemaps) | Enumerating everything |
| 3 | `…/wp-sitemap-posts-service-1.xml` | 200 — **20 service pages** | **Decisive**: no network page among them |
| 4 | `…/wp-sitemap-posts-page-1.xml` | 200 | No network page among the general pages |
| 5 | `https://www.saico.com.sa/service/medical/` | 200 — SME medical | Product content |
| 6 | `https://www.saico.com.sa/service/medical-2/` | 200 — corporate medical | Product content |
| 7 | `https://www.saico.com.sa/faqs/` | 200 — 7,334 bytes | **The "category and network" sentence**; contact hours |
| 8 | `https://www.saico.com.sa/contact-new/` | 200 — 7,940 bytes | Contact numbers |
| 9 | `https://www.saico.com.sa/e-services/` | 200 — 4,777 bytes | Digital services list |
| 10 | `https://digital.saico.com.sa/` | Proxy timeout (422) | E-services portal; form-based, not enumerated |

## Contact numbers, as published

| Number | Source | Purpose |
|---|---|---|
| **920000563** | Contact page + site header | Main line; page states *"All Services: 8:00 AM – 4:00 PM, **Medical Services: 24/7**"* |
| **8001242002** | Contact page | Call center |
| **920013380** | Contact page | WhatsApp |

All three are SAICO's own published values, not a directory listing.

## The FAQ sentence — exact wording

From `/faqs/`, medical cash-reimbursement section:

> "The policyholder shall be compensated by the insurance company for the reimbursement expenses
> according to the prevailing rates for the **category and network** of the customer within a
> period not exceeding 15 working days…"

and, earlier in the same section:

> "For non-emergency cases, **prior approval from SAICO is required**."

Both are quoted verbatim in `tiers-and-packages.md` because they are the strongest single
evidence in the project that coverage is category- and network-specific.

## Site type

WordPress, server-rendered, real XML sitemap. The sitemaps were read directly; the HTML pages
through a rendering proxy (they render cleanly, with no timeout). This is one of the most
permissive sites in the set — so the absence of a network file is a publication choice with no
technical excuse, unlike Malath (unreachable host) or Al Rajhi Takaful (403 to non-browser
clients).

## Nothing from outside saico.com.sa informs this skill

No third-party directory was consulted or adopted.
