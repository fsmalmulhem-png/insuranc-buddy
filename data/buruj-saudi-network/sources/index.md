# Buruj — sources checked

All checks on **11 November 2026**.

## The domain is dead

| # | URL | Result |
|---|---|---|
| 1 | `https://www.burujinsurance.com/` | **Connection timeout (25s)** |
| 2 | `https://www.burujinsurance.com/robots.txt` | Timeout |
| 3 | `https://www.burujinsurance.com/sitemap.xml` | Timeout |
| 4 | All three via text-rendering proxy | **422** — `page.goto: Timeout` |

**DNS still resolves**, so the domain is registered and pointed somewhere:

```
burujinsurance.com       212.12.182.211
www.burujinsurance.com   88.85.240.36
```

Nothing is served. Consistent with the merger having retired the brand.

## The authoritative source: MEDGULF's merger FAQ

| # | URL | Result |
|---|---|---|
| 5 | `https://www.medgulf.com.sa/home/buruj-faqs` | 200 — 13,738 bytes, **full content** |

This is where the facts in this skill come from. MEDGULF hosts a dedicated **Merger FAQs** page
covering General, Vehicle, Health, Domestic Worker and Medical Malpractice inquiries.

### Key quotes, verbatim

> "We are pleased to announce that the merger between Buruj and MEDGULF was officially completed
> on **October 26, 2025**, unifying efforts under the MEDGULF name to form a stronger and more
> efficient insurance entity."

> "The issuance of policies through Buruj has been stopped. If your policy expires, you can renew
> it through MEDGULF, which will continue providing policy issuance and renewal services."

> "We assure you that all your current services and policies, as well as support channels, will
> continue as usual without any changes."

> "There will be no changes to the insurance terms, and they will remain fully compliant with the
> requirements of the Insurance Authority."

> "Currently the MEDGULF app does not support Buruj policies."

> "For Health and Life Insurance: MEDGULF Clients via Toll-Free Number: **8001188555** (24/7);
> **Buruj Clients** (including approvals, claims, complaints, and more), available 24/7 at
> **920014001**"

> "Member level: (TCS) **920014001** - 24/7"

## Wayback Machine

A snapshot of `burujinsurance.com` exists, closest capture **2023-11-29** — before the merger. It
was not used for content: pre-merger data would be actively misleading for a member asking today.

## Corroboration

A trade-press article surfaced in search ("Two Saudi insurers MEDGULF and Buruj finalise merger
deal", Global Reinsurance) consistent with the MEDGULF statement. Not relied on for facts — the
insurer's own FAQ is the source of everything above.

## Contact routes, all from the MEDGULF FAQ

| Route | Value | Scope |
|---|---|---|
| **TCS** | **920014001** (24/7) | **Medical member level** — approvals, claims, complaints |
| MEDGULF toll-free | 8004414442 | Motor/general, Sun–Thu 8:00–16:00 |
| MEDGULF health (own clients) | 8001188555 (24/7) | For MEDGULF-original clients |
| Buruj client email | `M-CSC@medgulf.com.sa` | Buruj clients |
| Claim status | `forms.burujinsurance.com/claims/...` | Still live on the subdomain |

## Why this skill has no provider data

Buruj's network is now MEDGULF's. Duplicating pre-merger Buruj data would be stale by definition.
The MEDGULF skill in this set documents what MEDGULF publishes (tier names, provider counts, no
hospital list); this skill exists only to get a Buruj member to the right door.
