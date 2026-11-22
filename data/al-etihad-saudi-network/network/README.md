# Al Etihad Insurance — network

## There is nothing, because there is no website

`aletihad.com.sa` answers with a page reading **"Comming soon"**. That is the entire site:
13 bytes of body text, no navigation, no product pages, no contact block, no robots file, no
sitemap. The domain is live and the server responds — it simply has no content behind it.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `https://www.aletihad.com.sa/` | 200 — **"Comming soon"**, 13 bytes of body |
| 2 | `https://www.aletihad.com.sa/robots.txt` | 404 — no robots file exists |
| 3 | `https://www.aletihad.com.sa/sitemap.xml` | 404 — no sitemap exists |
| 4 | Wayback availability API | One "closest" snapshot, 2025-04-16 |
| 5 | Wayback CDX index for the whole domain | **Only three captures ever**: the homepage, `robots.txt`, and `favicon.ico` — no product, health, or document pages |
| 6 | Wayback replay of the 2025 snapshot | 200 — **"Comming soon"**, 13 bytes, identical to live |

Attempt 5 is the informative one. If the site had ever had product pages, the archive would
hold captures of them. It holds only the homepage, and the homepage has said the same thing
since at least **November 2021**. The company has never had a public website with content.

## What this rules out

- No tier names.
- No class list.
- No provider names, in any city.
- No downloadable file.
- **No published phone number either.** The skills must not invent one; the member's card or
  policy carries it.

## What a member has instead

1. **Their own card / policy pack** — carries the insurer's number and the policy number.
2. **CCHI's insurance-status service** (`eservices.chi.gov.sa`) — confirms the policy is active.
   It does not list providers, but it is a real, regulator-run check the member can do.
3. **The hospital's reception desk** — the fallback the project is built around.

## If Al Etihad builds a site later

Revisit this skill. The check is cheap: load the homepage and see whether it still says
"Coming soon". If content appears, convert it the way Bupa's files were converted, and record
the date taken.
