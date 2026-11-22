# Malath — sources checked

All reading done on **11 November 2026**.

## Important provenance note

The live site `malath.com.sa` **could not be reached** from this environment — connection
timeouts on both resolved IPs, on every path, via both direct request and text proxy. Content
below therefore comes from **Internet Archive snapshots** of Malath's own pages. The domain is
Malath's; the pages are Malath's; the *vintage* is the archive's, not the live site's.

That distinction is recorded openly because it changes how much weight the facts carry.

| # | URL | Route | Result | Used for |
|---|---|---|---|---|
| 1 | `https://www.malath.com.sa/` | direct | Timeout (30s) | — |
| 2 | `https://www.malath.com.sa/robots.txt` | direct | Timeout | — |
| 3 | `https://www.malath.com.sa/sitemap.xml` | direct | Timeout | — |
| 4 | `https://www.malath.com.sa/` | text proxy | 218 bytes, empty body + "page may not be fully loaded" | Nothing |
| 5 | `https://www.malath.com.sa/en` | text proxy | 422 TimeoutError | Nothing |
| 6 | `web.archive.org/cdx/search/cdx?url=malath.com.sa*` | archive index | 200 — HTML snapshots only, no PDFs | Enumerating routes |
| 7 | archived `/en/products` | archive | 200 | **Primary source**: health products, SME "plans and classes" wording |
| 8 | archived `/en/downloads` | archive | 200 | Discovering the medical network PDF link |
| 9 | archived `/en/contact` | archive | 200 | **Primary source**: call centre 9200 15815, offices, email |
| 10 | archived `/en/services`, `/en/companyprofile` | archive | 200 | Confirming no further network content |
| 11 | `…/2018.9.30.12.59.4.947.1927940-Malath_Medical_Network_List_R.pdf` — direct | direct | Timeout | — |
| 12 | same PDF — text proxy | proxy | 422 TimeoutError | — |
| 13 | same PDF — Wayback availability API | archive | `archived_snapshots: {}` | Proving never archived |
| 14 | same PDF — Wayback replay `/web/2024id_/…` | archive | 404 | Same |

## Snapshots used, and their dates

The archived captures viewed were from the 2018–2024 range; the Downloads page listed files
whose newest document is from 2018. Because the archive returns the nearest capture it has,
the **live site may well be newer and different**. Treat every product statement here as
"Malath said this, as of the archived capture", not "Malath says this today".

## What this means for the write-up

This is the one company of the four where a **single downloadable network list** exists as a
publication format — the closest thing to what the project wants. The catch is the age: a 2018
file is not usable for a 2026 advisor, and the site that would carry a current one is not
reachable from here. Both facts belong in the write-up: the format exists, the currency does not.

## Search attempts

Bing and DuckDuckGo were tried for a Malath network PDF. Bing returned unrelated results for
the `site:` query and DuckDuckGo was rate-limited. Neither produced anything usable, and
nothing outside Malath's own domain informs this skill.
