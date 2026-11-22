# Al Rajhi Takaful — the locator, and why there are no city files

## There is a real public lookup. There is no file.

Al Rajhi Takaful publishes a **medical provider locator** that requires no login:

- English: `https://www.alrajhitakaful.com/en/medical-provider-locator`
- Arabic: `https://www.alrajhitakaful.com/ar/medical-provider-locator`

It is linked from the site footer under "روابط مفيدة" (useful links) as **"شبكة مقدمي الخدمات
الصحية"** — "healthcare providers network".

## What the page actually contains

From the rendered page:

- a **search box** with live type-ahead ("ستظهر النتائج هنا أثناء الكتابة في البحث" — *results
  will appear here as you type in the search*)
- a **"بالقرب مني" / "near me"** control
- a **Google Maps pane** (the page loads the Maps JS API)
- an initial state of **"0 نتائج" / "0 results"**

So it is a genuine search over a provider dataset, not a static brochure. That is a real
capability, and it is the first unauthenticated provider search in this set.

## Why it still cannot produce city files

| Reason | Detail |
|---|---|
| **Results are client-side** | Queries are answered by a browser-side API call. The page HTML carries the *interface*, not the data. |
| **The host refuses non-browser requests** | Direct requests to the page, to `main.js`, and to guessed API paths (`/api/provider/search`, `/api/medical-providers`) all return **403** with a ~5 KB block page. |
| **No export, no bulk route** | No download control, no CSV/PDF link, no paginated list URL appears anywhere on the page or in the sitemap. |
| **Result behaviour untested** | Because the site blocks scripted access, this skill never ran an actual query. It documents the interface, not the results. |

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `robots.txt` | 200 — crawlable |
| 2 | `sitemap.xml` | 200 — **280 URLs** enumerated |
| 3 | Sitemap scan for `network`, `provider`, `hospital`, `pdf`, `xlsx`, `download` | Found **`medical-provider-locator`** — the locator — and no file |
| 4 | `/ar/medical-provider-locator` (proxied) | 200 — interface rendered, "0 results", near-me control, Maps pane |
| 5 | `/en/medical-provider-locator` (proxied) | 200 — same, English |
| 6 | Same pages, direct request | **403** |
| 7 | `/main.js`, direct | **403** |
| 8 | Guessed API paths | **403** |
| 9 | Site footer links | Points back to the locator as the network answer — **no PDF anywhere** |

## Contact route

Al Rajhi Takaful's Contact page publishes:

| Line | Number | Hours |
|---|---|---|
| **Medical line** | **8001184444** | **24/7** |
| Local line | 920004414 | 8:00–16:00 (medical line exempt) |
| International | listed on the page | — |

Taken from real `tel:` links on `/ar/contact-us`.

## What would legitimately fill this skill

1. **A member running locator searches** for specific hospitals, reported back — one hospital
   per query.
2. **A policy pack** — may include a network booklet.
3. **A call to the medical line (8001184444)** asking for the class's network.

## What the agent does instead

Hands the user the locator URL and the medical line, and still gives the hospital question.
See `../SKILL.md`.
