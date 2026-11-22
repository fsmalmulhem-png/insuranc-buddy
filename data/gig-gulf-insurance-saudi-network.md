---
name: gig-gulf-insurance-saudi-network
description: Gulf Insurance Group (GIG / gig.sa) — the most complete disclosure in this set: a public provider locator with 3,437 named providers across 365 cities, each tagged with its network (VVIP/VIP/A+/A/B+/B/C/D/E), plus full published benefit tables per network. Read when the user's company is GIG, to name a provider from the city tables and state its network tier.
---

# Gulf Insurance Group (GIG) — 3,437 named providers, tagged by network

## Status

**The most complete disclosure found in this entire project.** GIG publishes:

1. A **public provider locator** — no login — containing **3,437 named providers** across **365
   cities**, each carrying its **network tier** (VVIP, VIP, A+, A, B+, B, C, D, E), type, address
   and telephone.
2. **Full benefit tables per network**, with room type, maternity limit, deductible, coinsurance
   and dental/optical limits.

Converted into **365 city files**. Nothing has been filtered or inferred.

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept GIG and still not accept the member's network. **GIG is the one company where
this skill can answer at provider + network level from published data** — so it does, and states
the source.

But **Class A / Class B is still not the vocabulary GIG uses.** Its tiers are VVIP/VIP/A/B/C/D/E.
A card saying "Class B" must be checked against the policy for its GIG network name.

---

## The network tiers — verified

GIG's provider locator tags every provider with one of these:

| Network | Providers tagged |
|---|---|
| **E** | 2,648 |
| **VIP** | 339 |
| **C** | 144 |
| **B** | 121 |
| **D** | 97 |
| **A** | 60 |
| **A+** | 21 |
| **B+** | 6 |
| **VVIP** | 1 |

The distribution is the finding: **2,648 of 3,437 providers (77%) are on network E**, and only 339
sit on VIP. A member on a higher tier gets a far wider choice; the bulk of the locator is the
entry tier.

## The benefit structure — published

GIG publishes named networks with their benefits. Sample from the group-healthcare page:

| Network | Area of cover | Room & Board | Maternity | Deductible |
|---|---|---|---|---|
| **VVIP 1** | Regional | Suite | 20,000 SAR | Nil |
| **VVIP 3** | KSA only | Suite | 20,000 SAR | 10% max 50 SAR |
| **VIP 1** | KSA only | Suite | 15,000 SAR | 20% max 50 SAR |
| **VIP 2** | Regional | Suite | 20,000 SAR | Nil |
| **VIP 3** | KSA only | Suite | 20,000 SAR | 10% max 50 SAR |
| **VIP 4** | KSA only | Suite | 15,000 SAR | 20% max 50 SAR |
| **VIP 5** | Regional | Suite | 15,000 SAR | 10% max 50 SAR |
| **VVIP2** | KSA only | Suite | 15,000 SAR | 10% max 50 SAR |

Each row is then further qualified by coinsurance on generic and innovative drugs, dental
limits, RCT/emergency dental, optical care and IEMA.

**Note the numeric suffixes** — `VVIP 1`, `VIP 3` etc. The locator tags providers with the base
tier (`VIP`), while the benefit table lists numbered variants. The skill treats a locator tag of
`VIP` as "the VIP family" and does not assume which numbered variant a member holds.

## Products

| Product | Route |
|---|---|
| **Group healthcare** (employees) | `/business/employee/group-healthcare-insurance/` |
| Healthcare quote | `/healthcare-quote/` |
| Provider locator | `/provider-locator/` |
| Individual lines | Motor · Travel · Home · Motorcycle |

Health is sold as **group healthcare for employees** — an employer product.

## What the agent must do for a GIG user

1. Confirm the company is **Gulf Insurance Group (GIG)** — Arabic مجموعة الخليج للتأمين.
   Note: *GIG* is **not** *GGCI* (Gulf General) which is also in this set.
2. Ask **which network** is on their card or policy — VVIP, VIP, A+, A, B+, B, C, D or E. If they
   only know "Class A / Class B", say GIG's published tiers use these names and they should check
   the policy schedule.
3. Ask the city and the service.
4. **Look the provider up in `network/<city>.md`** and name it with:
   - its **network tag** — the authoritative fact,
   - its type, address and telephone.
5. If the provider's tag does not match the user's network, say so plainly.
6. If the provider is not in the city file, say **"I cannot confirm this"** and give the hospital
   question.
7. Contacts: **8001160020**.

---

## The GIG / GGCI collision — flag it

This set contains **two** similarly abbreviated Gulf insurers:

| | **GIG** | **GGCI** |
|---|---|---|
| Full name | Gulf Insurance Group | Gulf General Cooperative Insurance |
| Arabic | مجموعة الخليج للتأمين | الخليجية العامة |
| Domain | gig.sa | ggi-sa.com |
| Provider data | **3,437 providers** | 423, expired |

Do not mix them. If a user says "Gulf Insurance", ask which.

---


### The answer block — use this shape every time

1. **What they hold:** GIG group health policy.
2. **Class:** the GIG **network** — VVIP, VIP, A+, A, B+, B, C, D or E. Cards printing Class A/B
   should be checked against the policy schedule.
3. **What to do next:** look the provider up in `network/<city>.md` and name it with its network tag,
   type, address and telephone. If the tag does not match their network, say so.
4. **Always ask the hospital:** *"Do you bill GIG [network] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, networks, procedure. |
| `tiers-and-packages.md` | Full tier distribution and benefit tables. |
| `network/<city>.md` | **365 city files**, 3,437 providers with network tags. |
| `network/README.md` | Extraction method. |
| `sources/index.md` | Every URL and result. |

---

## Change log

- 2026-11-11 — skill created. Provider locator parsed in full: 3,437 providers, 365 cities, network
  tags preserved. Benefit tables captured. Largest dataset in the set.
