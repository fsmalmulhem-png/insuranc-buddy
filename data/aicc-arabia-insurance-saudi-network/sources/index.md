# Arabia Insurance (AICC) — sources checked

All checks on **11 November 2026**.

## The URL given points at the wrong entity

| Domain | What it is |
|---|---|
| `www.arabiainsurance.com` (supplied) | **Arabia Insurance Company** — the regional group (est. 1944, 8 countries, ADGM holding). Corporate brochure: no products, no network, `/sitemap.xml` 404s |
| **`www.aicc.com.sa`** | ✅ **Arabia Insurance Cooperative Company** — the Saudi licensed entity, with the network PDFs |

Found by searching the company name. The group site is not an insurer you can hold a card with
in Saudi Arabia.

**Separately: not Arabian Shield.** Arabian Shield (الدرع العربي, `der3.com`) is a different
insurer with its own skill in this set. Two similarly-named companies, two different skills.

## On aicc.com.sa

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.aicc.com.sa/` | 200 — long homepage | Company identity, network PDF links |
| 2 | `https://www.aicc.com.sa/products` | 200 | **All four network PDFs**, plus contact numbers |
| 3 | `https://www.aicc.com.sa/contact` | 200 | Unified / toll-free / medical lines |
| 4 | `https://www.aicc.com.sa/robots.txt` | 200 | Crawlability |
| 5 | `https://www.aicc.com.sa/sitemap.xml` | 200 | Route check |

## The four PDFs

Base path: `https://www.aicc.com.sa/Images/MedicalNetwork/`

| File | Pages |
|---|---|
| `AICC CORPORATE NETWORK  08-11-2026 pdf.pdf` | 54 |
| `AICC Unique Iqama  NETWORK  08-11-2026 pdf.pdf` | 57 |
| `Aicc Insurance  ELITE SME Network  business   08-11-2026 pdf.pdf` | 43 |
| `Aicc Insurance ELITE  SME C0666  07-04-2026 PDF.pdf` | 10 |

All downloaded and parsed. Every PDF's internal title shows it was produced from an `.xlsx`
(e.g. `AICC Unique Iqama  NETWORK  08-11-2026 pdf.xlsx`), which is why rows are cleanly tabular.

## Contacts, from `/contact`

| Arabic label | Number |
|---|---|
| الرقم الموحد (unified) | **920005002** |
| الرقم المجاني (toll-free) | **8001288888** |
| الموافقات والمطالبات الطبية (medical approvals & claims) | **920002013** — WhatsApp `wa.me/966920002013` |

All three taken from `tel:` links on AICC's own contact page.

## Product line

AICC's products page carries a **التأمين الصحي** (health insurance) tab, so health is a genuine
product line — sold to corporates and SMEs, matching the four network names (Corporate, Unique
Iqama, SME Elite, SME C0666).

## Nothing from outside aicc.com.sa informs this skill

No third-party directory was used, despite search surfacing an "Arabia Insurance Cooperative
hospital list" page on a non-official site. It was not opened for content and contributed
nothing.
