# Arabian Shield — network files

## There are none

Arabian Shield does not publish a provider list in any format. No city files exist in this
skill.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `der3.com/robots.txt` | 200 — crawlable, no restrictions |
| 2 | `der3.com/sitemap.xml` | 200 — large route index | Enumerated; **no network, hospital, provider or download route** |
| 3 | Homepage (Arabic) | 200 — full content | Found the single health product and the contact block |
| 4 | Homepage (`/en`, English) | 200 — full content | Confirms one product, "wide and distinctive network", no list |
| 5 | `der3.com/programs` | 200 — 202 bytes, empty | Not a content page |
| 6 | `der3.com/product-category` | 200 — 123 bytes, empty | Not a content page |
| 7 | `der3.com/contact-us` | 200 — 117 bytes, empty | Not a content page |
| 8 | `der3.com/medical` | 200 — 201 bytes, empty | Route guess; no content |
| 9 | Medical Portal link (`apps.der3.com/customer/auth/login`) | Flutter app shell behind login | Member services, **not** a provider directory |
| 10 | `direct.der3.com/home` and `/cl` | Flutter app shell | Client platforms for home/liability; not a directory |
| 11 | Sitemap scan for `download`, `pdf`, `xlsx`, `network`, `hospital` | The only PDFs are the Health Insurance Beneficiaries' Rights document and mandate links | No network file |

## The one PDF on the site

`/Resources/6/Health-Insurance-Beneficiaries-Rights.pdf` — this is the **CCHI beneficiaries'
rights regulation**, not a provider list. It is the regulator's document restated, and it says
what a member is entitled to, not which hospital will treat them. Do not confuse it with a
network list, and do not convert it as one.

## Why the statement "wide and distinctive network" is not usable

Marketing language of that kind says a network exists and is large. It carries no hospital
name, no city, and no class dimension. Converting it into a list would require inventing the
list, which is precisely what this skill must never do.

## What would legitimately fill this skill

1. **Call the medical insurance line** — 8001 240 240 — and ask for the current network for a
   named class. Arabian Shield will send it to a policyholder.
2. **A member's policy pack**, which typically includes a network booklet.
3. **The Medical Portal**, if a member grants access — it may show in-network providers for
   their policy.

## What the agent does instead

Gives the member the medical line and the exact question to ask the hospital. See `../SKILL.md`.
