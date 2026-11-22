# Walaa — network files

## There are none, and no public lookup either

Walaa publishes no medical provider list in any format, and has no public provider search. No
city files exist in this skill.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `walaa.com/robots.txt` (direct) | 200 — `Allow: /`, sitemap declared, `/dashboard` and `/myprofile` disallowed |
| 2 | `walaa.com/sitemap.xml` | Serves the SPA, not XML — **the declared sitemap does not resolve to a real file** |
| 3 | Homepage (direct) | 200 — 1,277-byte React shell |
| 4 | `/assets/index-YQjw2Qpg.js` (**1.75 MB**) | **Primary source**: product map, all 64 page modules, all public routes |
| 5 | Enumerated every `/pages/*` module | 64 modules. **No medical-network, hospital or provider page exists** |
| 6 | Enumerated every string route | 25 routes. Medical-related: none beyond product pages |
| 7 | `/pages/Branch-Locator/` | Exists — but finds **Walaa offices**, not hospitals |
| 8 | `/pages/Document-Library/` + its lazy chunk | Exists — CMS-driven document list, no network file |
| 9 | `/pages/Frequently-Asked-Questions/` | Exists — no network answer in the code |
| 10 | CMS API `apicoregcp.walaa.com/cms/` | 404 on every probed path; real endpoints are constructed at runtime |
| 11 | Rendered pages via proxy | Return only the shell (348–723 bytes) — content is fetched client-side |

Attempt 5 is the decisive one: the full module list of the app contains no network page. A
provider lookup cannot be hidden in a route that does not exist.

## The Branch Locator trap

`/pages/Branch-Locator/` sounds like the right page and is not. It carries `branch-card`,
`branch-expand` and a map — for **Walaa's own offices**. Tawuniya's network page had the same
trap: its default results were branch offices. Recorded so nobody later reports that Walaa "has
a locator" as if it were a hospital list.

## What would legitimately fill this skill

1. **A member's own network** from the Walaa dashboard or app, for a named class.
2. **A policy pack** — may include a network booklet.
3. **A call to Walaa** using the number on their Contact page.

## Note: no phone number is recorded here

Walaa's contact details are delivered from its CMS at runtime, and the app bundle contains none.
Rather than assert a number that could not be read from the company's own published content,
this skill directs the user to `walaa.com/contact-walaa` and says no number is held. A wrong
number is worse than a pointer to the right page.
