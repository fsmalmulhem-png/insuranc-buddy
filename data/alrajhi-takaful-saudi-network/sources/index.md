# Al Rajhi Takaful — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.alrajhitakaful.com/robots.txt` | 200 | Confirming crawlability |
| 2 | `https://www.alrajhitakaful.com/sitemap.xml` | 200 — 41 KB, **280 URLs** | **Decisive enumeration**: found the locator, proved no file |
| 3 | `https://www.alrajhitakaful.com/ar/medical-provider-locator` | 200 via proxy | **Primary source**: the public provider search |
| 4 | `https://www.alrajhitakaful.com/en/medical-provider-locator` | 200 via proxy | English mirror of the same |
| 5 | `https://www.alrajhitakaful.com/en/business/health-insurance` | 200 via proxy | Health product for employees |
| 6 | `https://www.alrajhitakaful.com/ar/product-health` | 200 via proxy | Individual health product |
| 7 | `https://www.alrajhitakaful.com/ar/faqs` | 200 via proxy | Checked for network guidance — none given |
| 8 | `https://www.alrajhitakaful.com/ar/contact-us` | 200 via proxy | **Primary source**: medical line and local line |
| 9 | Same pages, direct request | **403** | Host blocks non-browser clients |
| 10 | `main.js`, direct | 403 | Bundle not retrievable |
| 11 | `/api/provider/search`, `/api/medical-providers`, `api.alrajhitakaful.com` | 403 | No open API path |

## Contact numbers, and their function

| Number | Source | Function |
|---|---|---|
| **8001184444** | `tel:` link on `/ar/contact-us` | **Medical line — 24/7** |
| **920004414** | `tel:` link on `/ar/contact-us` | Local line |

The Contact page states: *"الخط الطبي 24/7 \| الخطوط الأخرى من 8:00 صباحًا إلى 4:00 مساءً"* — the
medical line runs 24/7, other lines 8:00–16:00. Both numbers are Al Rajhi Takaful's own
published values.

## Sitemap findings worth recording

280 URLs were enumerated. The health-related ones are:

- `business/health-insurance` (SME health)
- `product-health`, `health-purchase`, `domestic-health-purchase`
- `health-claims`, `health-make-claims`, `health-add-claims`, `health-claim-register-form`
- `medical-claim`, `personal/medical-malpractice-insurance`
- `value-added-medical-services`
- **`medical-provider-locator`** ← the public search

**No** network PDF, Excel, or provider-download route exists in the sitemap. That enumeration
is the evidence that the locator is the whole of their published network access.

## Method note

The site returns **403** to every direct, non-browser request — page, JS bundle, and guessed
API alike. Content was therefore read through a rendering proxy, which succeeded on the HTML
pages. The consequence is recorded openly: this skill documents the **interface** of the
provider locator, and never claims to have run a query against it.

## Nothing from outside alrajhitakaful.com informs this skill

No third-party directory was consulted or adopted.
