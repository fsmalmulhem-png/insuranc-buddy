# Gulf General (GGCI) — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.ggi-sa.com/` | 200 — 14 KB | Company identity, health product lead |
| 2 | `https://www.ggi-sa.com/robots.txt` | 200 | Crawlability |
| 3 | `https://www.ggi-sa.com/sitemap.xml` | 200 — **41 routes** | Route enumeration |
| 4 | `/ar/detail/corporate/health-care--and-life-insurance` | 200 — 23.6 KB | **Source of the network PDF link** |
| 5 | `/ar/page/Customer_Care` | 200 — 10.3 KB | Contact numbers |
| 6 | `/ar/page/Important_Links` | 200 | Cross-check |
| 7 | `https://www.ggi-sa.com/uploads/20250914044040-453242834-SME_Network_GI_KSA_temp.pdf` | 200 — 615 KB, 13 pages | **The network file** |

## The site

Server-rendered (not an SPA) — content reads directly, sitemap is real XML. 41 routes; **no
network page exists** as a route, but the PDF is linked inline from the health product page as a
PDF icon. That is why route enumeration alone would have missed it: the file lives in `/uploads/`
with a timestamped name, not under a predictable path.

## Contacts, from `/ar/page/Customer_Care`

| Label | Number |
|---|---|
| الرقم الموحد (unified) | **920012654** |
| الرقم المجاني (toll-free) | **8002440054** |
| WhatsApp | `api.whatsapp.com/send?phone=966920012654` |

## The network file — key facts

| Property | Value |
|---|---|
| Filename | `20250914044040-453242834-SME_Network_GI_KSA_temp.pdf` |
| Pages | 13 |
| Publish timestamp in filename | **14 Sep 2025** |
| Rows parsed | **423** |
| Cities | **59** |
| Columns | Provider name (EN/AR) · CCHI No · Expire Date · Class (الفئات) · Telephone |

## The expiry audit

Every row's `Expire Date` was parsed as a date and compared against 11 Nov 2026:

| Result | Count |
|---|---|
| Still valid | **2** |
| Expired | **421** |

The two valid entries:

| Provider | City | Expires |
|---|---|---|
| AL MOUWASAT HOSPITAL – JUBAIL | Jubail | 18-May-2027 |
| AL QUWAYIYAH GENERAL HOSPITAL – AL QUWAYIYAH – (MOH) | Riyadh region | 01-Feb-2027 |

This audit is why the skill leads with a currency warning instead of a provider list.

## Method note — no local PDF tooling

`pdftotext`, `pdfminer` and `fitz` are not available in this environment, and the raw 615 KB PDF
was downloaded but could not be parsed locally. Extraction was done through a text-rendering
proxy, which returns the PDF as Markdown with the tabular rows intact. That path preserved the
English names, CCHI numbers and dates well; Arabic names did not survive and were dropped.

## Nothing from outside ggi-sa.com informs this skill

No third-party directory was used.
