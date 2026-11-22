# MEDGULF — network files

## There are none

MEDGULF publishes the **size** of each RIADI tier's network but not the **contents**. No city
files exist in this skill because MEDGULF publishes no provider names, in any format.

This is different from Tawuniya, which at least offers a per-hospital lookup. MEDGULF offers
counts.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `robots.txt` | Allow-all; points to the real sitemap at `/home/sitemap.xml` |
| 2 | `/home/sitemap.xml` — enumerated all **50** routes | Succeeded. Health routes are only: `group-health`, `riadi-sme-health-insurance`, `napd-program`, `visit-visa`. **No network, hospital, provider or download route exists** |
| 3 | `/home/riadi-sme-health-insurance` | Succeeded. Five tiers, provider **counts**, starting prices. No names |
| 4 | `/home/napd-program` | Redirects to the RIADI page — same content, same counts |
| 5 | `/home/group-health` | Loads only navigation and footer furniture; no health content, no tier table |
| 6 | `/home/faqs` | Succeeded. Gives contact numbers only; no network answer |
| 7 | `/home/mobile-application` | Succeeded. Describes the app; no provider list, no manual file reference |
| 8 | `/home/network`, `/home/hospitals`, `/home/medical-network`, `/home/provider-network` | All return the SPA shell — these routes **do not exist**; the server answers every unknown path with the app frame |
| 9 | Raw HTML of the RIADI page | 37 KB Angular shell; contains no `.pdf`, `.xlsx`, `.csv` links at all |
| 10 | Compiled app bundle `main.bc094c72e1aaa88a.js` (2.2 MB) — searched for API and route strings | Found the API host `mg-prodapi.medgulf.com.sa` and its motor/client endpoints. **No network, provider, hospital or clinic endpoint exists in the bundle** |
| 11 | Sitemap-wide scan for `download`, `document`, `file`, `brochure` | No document hub route exists |

Attempt 10 is the decisive one: if the site had a provider lookup, the client bundle would have
to call an endpoint for it. There is none. MEDGULF's public web presence has no provider search.

## Why the counts were still kept

"+ 300 Providers" is not a list, but it is a real published fact about MEDGULF's tiers, and
it is the only published fact that distinguishes one tier from another in network terms.
Keeping it lets the agent say something true and useful — that Elite's network is stated as
roughly six times the size of Basic's — without ever implying it knows which hospitals.

## What would legitimately fill this skill

1. **A MEDGULF member's tier-specific network** — obtained from MEDGULF directly (they issue it
   with the policy), by phone, or via the app.
2. **A contracted-provider feed** — MEDGULF is a large insurer; provider directories are
   sometimes supplied to contracted hospitals.
3. **A voice-agent call** — the future-work idea already scoped for this project is the exact
   fallback this skill hands to the user today.

## What the agent does instead

Gives the member MEDGULF health customer care on **8001188555 (24/7)** and the exact question
to ask the hospital. See `../SKILL.md`.
