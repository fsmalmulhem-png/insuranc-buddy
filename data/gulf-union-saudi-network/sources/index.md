# Gulf Union — sources checked

All checks on **11 November 2026**.

## The redirect trail

| URL | Result |
|---|---|
| `https://www.gulfunion.com.sa/` (supplied) | **302 → `https://eservices.gulfunion.com.sa/`** |
| `https://gulfunion.com.sa/` | 200 — 44,753 bytes → same portal |
| `https://www.gulfunion.com.sa/en` | 200 → same portal |
| `https://eservices.gulfunion.com.sa/` | 200 — 44,753 bytes, the portal itself |

There is no separate corporate/brochure site on this domain: everything lands on the Angular
e-services portal.

## What was checked

| # | URL / artefact | Result | Used for |
|---|---|---|---|
| 1 | Portal root (direct) | 200 — Angular shell + F5 `TSPD` bot-protection script | Finding the bundle |
| 2 | Portal root (text proxy) | 200 — 12,270 bytes of rendered nav + products | **Product list, contacts** |
| 3 | `robots.txt` / `sitemap.xml` | Return the app shell — no real files | Confirmed no sitemap route list |
| 4 | `main.0a0a484477a881a0.js` | 200 — **4,343,963 bytes** | **Primary source**: 72 routes, `PointedProviders(MemberId=…)` |
| 5 | `#/health/health-services-providers` | Shell only, no data anonymously | Confirmed member-gated |
| 6 | `#/faqs` | Shell only | No network answer published |

## Contact details, from the portal

| Detail | Value | Source |
|---|---|---|
| Phone | **8003040077** | `tel:` link in portal header and Contact section |
| Email | `customercare@gulfunion-saudi.com` | Contact Information block |

## Health products, as rendered

> **Health Insurance** — "Covers Medical Practices in Terms of Consultation and More"
>
> **Medical SME** — "For Small & Medium Establishments to Be Perfect Health Insurance"
>
> **Medical Malpractice** — "Protects Healthcare Practitioners From the Liabilities of Medical Errors"

Taken verbatim from the portal's product section via the text proxy.

## The member-scoped provider call — exact form

```js
GetAllServiceProviders(t){ this.medicalClaimsService.PointedProviders("MemberId=" + t).subscribe(...) }
```

with `t` from `memberDetails[0].id`, itself read from local session storage. Filtered form adds
`&CityId=` and `&ProviderId=`.

This is the decisive evidence that no public list exists.

## Method notes

- The portal is protected by an F5 anti-automation script and serves no sitemap, so route
  discovery was done by **reading the compiled bundle** rather than crawling.
- The text proxy rendered the public-facing pages well; authenticated pages were not attempted.
- No third-party directory was consulted or adopted.

## Cross-reference

Gulf General (GGCI) — `ggi-sa.com` — is a **different company** with its own skill in this set.
Two Gulf-branded Saudi insurers; do not merge them.
