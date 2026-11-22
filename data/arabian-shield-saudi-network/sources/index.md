# Arabian Shield — sources checked

All reading done on **11 November 2026**. The live site was reachable throughout.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.der3.com/robots.txt` | 200 — crawlable | Confirming no restrictions on reading |
| 2 | `https://www.der3.com/sitemap.xml` | 200 — full route index | **Proving no network/download route exists** |
| 3 | `https://www.der3.com/` (Arabic) | 200 — full content | **Primary source**: products, health description, contact numbers |
| 4 | `https://www.der3.com/en` (English) | 200 — full content | **Primary source**: English wording of the SME medical product |
| 5 | `https://www.der3.com/programs` | 200 — 202 bytes | Empty; no content |
| 6 | `https://www.der3.com/product-category` | 200 — 123 bytes | Empty |
| 7 | `https://www.der3.com/contact-us` | 200 — 117 bytes | Empty |
| 8 | `https://apps.der3.com/customer/auth/login` | Flutter shell | Member platform, gatekept |
| 9 | `https://direct.der3.com/home`, `/cl` | Flutter shell | Client platforms, not directories |
| 10 | `https://www.der3.com/Resources/6/Health-Insurance-Beneficiaries-Rights.pdf` | Linked, not converted | CCHI rights document — **not** a provider list |

## Contact numbers, as printed on the Arabic homepage

| Purpose | Number |
|---|---|
| Medical insurance (التأمين الطبي) | **8001 240 240** |
| Customer service centre (مركز خدمة العملاء) | 8001 247 247 |

These are taken verbatim from the `tel:` links in the site footer's "تواصل معنا" block, so they
are Arabian Shield's own published numbers rather than a directory listing.

## Site structure note

The site's navigation links many products to `https://www.der3.com/` — the homepage — rather
than to individual product pages. That is why there is no dedicated health page to read: the
health content lives as a section on the homepage, and the menu entry is not a link to
anything deeper. Recorded so nobody later assumes a page was missed.

## Nothing from outside der3.com informs this skill

No third-party list was consulted or adopted. The only external links on the site are
regulator and mandate portals (IA, CCHI, MOI, IDC) plus a TCS claim-submission endpoint —
none of which carries a provider list.
