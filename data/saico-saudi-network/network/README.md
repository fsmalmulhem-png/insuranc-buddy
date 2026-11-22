# SAICO — network files

## There are none

SAICO publishes no medical provider list in any format, and has no public provider search. No
city files exist in this skill.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `saico.com.sa/robots.txt` | 200 — WordPress; sitemap at `/wp-sitemap.xml` |
| 2 | `/sitemap.xml` → `/wp-sitemap.xml` | 200 — 4 sub-sitemaps (pages, services, projects, team) |
| 3 | Enumerated the **services** sitemap | **All 20 service pages listed.** Health: `service/medical` and `service/medical-2`, plus medical malpractice. **No network, hospital or provider page** |
| 4 | Enumerated the **pages** sitemap | About, branches, careers, claims, complaints, contact, e-services, FAQ, fraud, products, mission, policies. **No network page** |
| 5 | `/service/medical/` | 200 — SME medical, marketing copy only |
| 6 | `/service/medical-2/` | 200 — corporate medical, marketing copy only |
| 7 | `/faqs/` | 200 — the "category and network" sentence (see `tiers.md`), but no list |
| 8 | `/contact-new/`, `/e-services/` | 200 — contact numbers, no network |
| 9 | `digital.saico.com.sa` | Proxy timeout (422); e-services portal is form-based |

Attempt 3 is decisive: the complete service list of a WordPress site is short and enumerable,
and it contains no provider page. A network cannot hide in a page that does not exist.

## Site type note

Unlike the SPA-heavy insurers earlier in this set, SAICO runs an ordinary **WordPress** site:
pages are server-rendered, the sitemap is real, and content reads directly. That makes this
finding unusually firm — there is no client-side data that could be hiding a list. What is in
the sitemap is all there is.

## What would legitimately fill this skill

1. **A member's own category and network** — SAICO confirms both exist; a member's policy
   documents or a call to 920000563 would name them.
2. **A policy pack** — may include a network booklet.
3. **A prior-approval request** — SAICO requires approval for non-emergency care (stated in its
   own FAQ), so the approval process will name approved providers. This is a route a member can
   use without asking SAICO for a list.

## What the agent does instead

Gives the medical line, the call centre, and the hospital question. See `../SKILL.md`.
