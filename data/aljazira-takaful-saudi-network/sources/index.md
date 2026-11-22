# Aljazira Takaful — sources checked

All checks on **11 November 2026**.

## The supplied domain is dead

| # | URL | Result |
|---|---|---|
| 1 | `https://www.ajt.com.sa/` | **Connection timeout (25s)** |
| 2 | `https://www.ajt.com.sa/robots.txt` | Timeout via proxy (422) |
| 3 | DNS for `ajt.com.sa` | Resolves to **37.99.173.14** — registered, not serving |
| 4 | Wayback availability API | Closest capture **2022-03-03** — over four years stale |

So `ajt.com.sa` is a parked or retired host. The company still uses it as an **email domain**
(`info@ajt.com.sa`), which is why the abbreviation AJT circulates.

**The live site is `www.aljaziratakaful.com.sa`** — found by searching the company name, not by
guessing.

## The live site

| # | URL | Result | Used for |
|---|---|---|---|
| 5 | `https://www.aljaziratakaful.com.sa/` | 200 — 11,318 bytes | **Full product menus** |
| 6 | `/robots.txt`, `/sitemap.xml` | Returned page content, no usable sitemap | Enumerated routes from page links instead |
| 7 | `/IndividualProducts/Medical` | 200 — 8,784 bytes | Individual medical |
| 8 | `/CorporateProducts/Medical` | 200 — 8,750 bytes | Corporate medical |
| 9 | `/CustomerCare/DownloadCenter` | 200 — 19,926 bytes | **The TCS phone extension and app** |
| 10 | `/CustomerCare/Faqs` | 200 — 11,767 bytes | Motor/visa FAQs only |
| 11 | `doc.aljaziratakaful.com.sa/…terms_and_conditions.pdf` | Linked, checked | Terms only, no network |

## Route inventory

46 distinct URLs gathered from the site's own links. All paths:

`/` · `/About/*` (6) · `/Contact/*` (2) · `/CorporateProducts/*` (8) · `/CustomerCare/*` (8) ·
`/IndividualProducts/*` (9) · `/InsureNow/MedicalMalpractice` ·
`/MedicalDomesticH_InsureNow/IPMedicalDomesticHelper`

**No `Network`, `Hospitals`, `Providers` or `Find` route exists.**

## Contact details, verified from the site

| Channel | Value | Note |
|---|---|---|
| **Medical services** | **8003040400, extension 2** | "available 24/7" |
| Unified / claims | 8003040400 | — |
| International | +966 12 6688877 | — |
| Email | `info@ajt.com.sa` | Dead domain, live mailbox |

## The app, as linked by Aljazira Takaful

| Platform | Identifier |
|---|---|
| iOS | `apps.apple.com/sa/app/total-care-saudi/id1587870212` |
| Android | `play.google.com/store/apps/details?id=com.chatilaah.tc` |

**"Total Care Saudi"** with package `com.chatilaah.tc` — a TCS application. Aljazira Takaful's own
media folder also carries `Content/media/TCS_Footer.jpg`, i.e. TCS branding in the insurer's
footer.

## Note on method

Aljazira Takaful runs a server-rendered ASP.NET-style site with conventional
`/Area/Action` routes — no bundle reading required, unlike ACIG or Gulf Union. Routes were
collected from the rendered pages, which is sufficient here because every menu item appears in the
HTML.

## Nothing from outside aljaziratakaful.com.sa informs this skill

No third-party directory was used. The TCS comparison draws on the Al Sagr and Buruj skills in
this same set, each built from its own insurer's publication.
