# Liva — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.livainsurance.sa/` | 200 → `/ar/home` | Identity, homepage products |
| 2 | `https://www.livainsurance.sa/robots.txt` | 200 — crawl-delay 10, sitemap declared | Crawlability |
| 3 | `https://www.livainsurance.sa/en/home` | 200 — 5,515 bytes | Individual product menu, contacts |
| 4 | `https://www.livainsurance.sa/en/about-us` | 200 — 3,033 bytes | **Company history, rebrand, licensed scope** |
| 5 | `https://www.livainsurance.sa/en/sitemap` | 200 — **29 routes enumerated** | Proving no health product page |
| 6 | `https://www.livainsurance.sa/en/frequently-asked-questions-faqs` | 200 — 55,056 bytes | **The "future health products" quote** |
| 7 | `https://www.livainsurance.sa/en/documents` | 200 | **Found the visitor-visa network PDF** |
| 8 | `…/Visitor Visa_Medical Service Providers Network_1.PDF` | 200 — 15 pages | The network document |
| 9 | `/en/medical-insurance`, `/en/health-insurance` | **404** | Confirmed no such product page |

## The rebrand

> "Liva is the new brand identity of **Alalamiya**"

> "On **07 November 2023**, the new name of the company was announced as Liva Insurance Company."

So "Al Alamiya" and "Liva" are the same insurer. Worth knowing because a user may hold an older
document.

## The licensed-scope line — and why it is not a product list

From `/en/about-us`:

> "providing insurance products that meet their needs in the areas of Property; Marine; Motor;
> **Medical**; General Accident and Engineering"

This is what the company is **licensed** to underwrite. It is not the list of what it sells. The
product menu and sitemap show no medical product, and both guessed medical URLs 404. The skill
records this distinction explicitly so the quote is not misread.

## The health-as-intent quote

From the FAQ:

> "We will continuously work on exploring new and innovative ways to expand our products and service
> offerings to include a full suite of life, **health**, personal, and commercial insurance products"

A future ambition, not a current offering.

## The network PDF

| Property | Value |
|---|---|
| Filename | `Visitor Visa_Medical Service Providers Network_1.PDF` |
| Published | 14 January 2025 (file dated 2025-01-09) |
| Pages | 15 |
| Rows parsed | **244** |
| Cities | 45 |
| Valid accreditations on 11 Nov 2026 | **0** |
| Latest expiry in file | **11 August 2026** |

## Contacts, from the site

| Channel | Value |
|---|---|
| Call centre | **8002444481** |
| WhatsApp | `wa.me/9668002444481` |
| Travel assistance (24/7) | **+971 4 601 8777** |

## Method note

Liva runs a Drupal-style site (`sites/default/files/…` paths, `/ar/` and `/en/` trees). Content
rendered cleanly through a text proxy; the sitemap is real XML. The network PDF was found **only** by
reading the `/en/documents` page — it is not in the sitemap and not under a predictable path, which
is a reminder to check document indexes rather than only route lists.

## Nothing from outside livainsurance.sa informs this skill

No third-party directory was used.
