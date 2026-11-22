# Aljazira Takaful — network files

## None published — TCS holds it

Aljazira Takaful publishes no provider list in any format. No city files exist in this skill.

What it does publish is the **route** to the network, and it names the administrator by
implication at every point.

## The published route

| Channel | Detail |
|---|---|
| **Phone** | **8003040400, extension 2** — "Medical Services available 24/7" |
| **App** | **Total Care Saudi** (TCS) — iOS `total-care-saudi`, Android `com.chatilaah.tc` |
| International | +966 12 6688877 |
| Email | `info@ajt.com.sa` |
| General/claims | 8003040400 |

The extension matters: 8003040400 is Aljazira Takaful's main unified number, and **option 2** is
the medical-services branch. Saying "call 8003040400" without the extension risks the member
landing on a general queue.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `ajt.com.sa` (supplied) — DNS | Resolves: 37.99.173.14 |
| 2 | `ajt.com.sa` — direct request | **Connection timeout (25s)** |
| 3 | `ajt.com.sa` — via text proxy | **422 timeout** |
| 4 | Wayback for `ajt.com.sa` | Last capture **March 2022** — long dead |
| 5 | `aljaziratakaful.com.sa` | 200 — live, 11 KB |
| 6 | `/robots.txt`, `/sitemap.xml` | Returned the page, no usable policy |
| 7 | Route enumeration (46 URLs found) | **No `/Network`, `/Hospitals` or provider route** |
| 8 | `/IndividualProducts/Medical`, `/CorporateProducts/Medical` | Marketing copy only |
| 9 | `/CustomerCare/DownloadCenter` | **The TCS route and app** |
| 10 | `/CustomerCare/Faqs` | Motor/visit-visa FAQs; no network list |
| 11 | All `*.pdf` links found | Only `ajtweb_terms_and_conditions.pdf` on `doc.` subdomain |

Attempts 7 and 11 are decisive: the site's route list is complete and contains no provider page,
and the only PDF it publishes is the terms document.

## The `doc.` subdomain

`doc.aljaziratakaful.com.sa` hosts the terms-and-conditions PDF. It was checked and contains no
network data. It is worth knowing the insurer separates documents onto that host — if a network
file were ever published, that is where it would most likely live.

## What would legitimately fill this skill

1. **A member's own network** from the Total Care Saudi app, for a named class.
2. **A call to 8003040400 ext. 2** asking which hospitals are in the network for a class.
3. **TCS directly**, since TCS administers for multiple insurers and could confirm per policy.

## What the agent does instead

Hands the member the extension-2 number and the app, and gives the hospital question. See
`../SKILL.md`.
