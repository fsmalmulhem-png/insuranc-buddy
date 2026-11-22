---
name: gulf-union-saudi-network
description: Gulf Union Cooperative Insurance (الاتحاد الخليجي / gulfunion.com.sa) — sells Health Insurance and Medical SME, but the provider list is fetched per member ID inside the logged-in portal. No public network file. Read when the user's company is Gulf Union, to hand them the member-portal route. Holds no provider names — never name a hospital.
---

# Gulf Union Cooperative Insurance — a provider list that exists per member

## Status

**Products known. The provider list exists but is member-scoped.** Gulf Union sells **Health
Insurance** and **Medical SME**, and its customer portal exposes a provider lookup
(`/health/health-services-providers`). But the page is served from a **signed-in session** and the
underlying call takes a **`MemberId`** — it answers for one member, not the public.

No public network file, no downloadable list. **No hospital may be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Gulf Union** and still not accept the member's class. This skill never
answers at company level. It holds no provider names, so its only correct provider answer is
**"I cannot confirm this"**, plus the hospital's phone number and the exact question:

> *"Do you bill Gulf Union Class [A/B] directly?"*

---

## Do not confuse this with GGCI

The set already contains **Gulf General Cooperative Insurance (GGCI)** — `ggi-sa.com`,
"الخليجية العامة". Gulf Union is a **different company**: `gulfunion.com.sa`,
"الاتحاد الخليجي للتأمين". Both are Gulf-branded Saudi insurers and a user may say either name
loosely.

**If the user does not know which one they hold, ask** — and check the card or policy, which
carries the company name. Guessing would send them to the wrong network.

---

## What Gulf Union publishes — verified

The public site now redirects to an e-services portal (`eservices.gulfunion.com.sa`) built as an
Angular app. Its product menu lists:

| Product | Gulf Union's description |
|---|---|
| **Health Insurance** | "Covers Medical Practices in Terms of Consultation and More" |
| **Medical SME** | "For Small & Medium Establishments to Be Perfect Health Insurance" |
| Medical Malpractice | Professional liability for practitioners |
| Plus | Motor, Home, Marine, Engineering, Domestic, Savings |

Note that the individual product menu does **not** list a personal health product — health is
presented as corporate/SME cover, with Medical Malpractice as the individual health-adjacent line.

### The member portal — what it holds and why it is not public

Route `/health/health-services-providers` exists. So does `/health/health-benefits`,
`/health/health-approvals` and `/health-Cash-Claim`. But:

- The portal's pages are reached through `CUSTOMER PORTAL` / `login` and load member data from
  session storage.
- The provider call is `PointedProviders("MemberId=" + memberId)` — explicit in the app.
- Member-scoped means the answer differs per policy, so it cannot become a city table.

**The provider list is real. It is simply locked per member.**

## Classes

| Aspect | Published by Gulf Union? |
|---|---|
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |
| Class → provider mapping | **No** |
| Provider list (public) | **No** — member session only |

The app contains no class vocabulary at all — no VIP/Gold/Silver tiers, no A/B labels. The only
"category" fields are product and profession categories used in claim forms.

---

## What the agent must do for a Gulf Union user

1. **Confirm which Gulf company** they hold — Gulf Union (الاتحاد الخليجي) or Gulf General
   (الخليجية العامة / GGCI). Different companies, different skills.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that Gulf Union's provider list is only viewable
   inside the member portal.
5. Give them what does work:
   - **Log in to the customer portal** at `eservices.gulfunion.com.sa` → **Health** section →
     *Service Providers* — lists the providers available on their own policy.
   - **Call 8003040077**, or email `customercare@gulfunion-saudi.com`.
   - **Ask the hospital directly:** *"Do you bill Gulf Union Class [A/B] directly?"*
6. State that coverage and networks change, so confirm before travelling.

---


### The answer block — use this shape every time

1. **What they hold:** Gulf Union medical or medical-SME policy — and check it is not Gulf General or
   Gulf Insurance Group.
2. **Class:** ask for Class A / Class B; Gulf Union publishes no tier names.
3. **What to do next:** log in at `eservices.gulfunion.com.sa` → Health → **Service Providers**.
   Or call **8003040077**.
4. **Always ask the hospital:** *"Do you bill Gulf Union Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the GGCI disambiguation, the member-scoped finding, procedure. |
| `tiers-and-packages.md` | Products and the class gap. |
| `network/README.md` | The portal, the `MemberId` call, what was checked. |
| `sources/index.md` | Every URL and result, including the redirect trail. |

---

## Change log

- 2026-11-11 — skill created. Public site redirects to an e-services portal; provider lookup
  identified as member-scoped (`MemberId` parameter). No public network data exists.
