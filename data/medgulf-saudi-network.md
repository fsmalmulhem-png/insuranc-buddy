---
name: medgulf-saudi-network
description: MEDGULF (MedGulf / شركة المتوسط والخليج للتأمين) health plan tiers — RIADI Basic, Advance, Premier, Executive, Elite — with their published provider counts. Read this only when the user's company is MEDGULF, and only to explain tiers and provider-count order of magnitude, never to name a hospital.
---

# MEDGULF — health tiers and what is published

## Status

**Tiers loaded. Provider list NOT available.** MEDGULF publishes its health plan tiers and the
number of providers in each tier, but publishes **no provider list** — no hospital names, no
city breakdown, no file. No hospital may be named for a MEDGULF member from this skill.

Verified on 11 November 2026. See `sources/index.md` for exactly what was checked.

---

## The rule this skill exists to protect

A hospital may accept **MEDGULF** and still not accept the member's tier. This skill never
answers at company level. Since it holds no provider names, it cannot answer at tier level
either — so its only correct provider answer is **"I cannot confirm this"**, plus the
hospital's phone number and the exact question:

> *"Do you bill MEDGULF [tier] directly?"*

---

## MEDGULF's tiers — verified from its own site

MEDGULF sells health insurance through **RIADI**, its SME product (up to 250 employees).
RIADI has **five categories**, named and priced on MEDGULF's public page. Each category
states the size of its provider network.

| Tier | MEDGULF's own description | Providers it states | Starting price (SAR, inc. VAT) |
|---|---|---|---|
| **Riadi Basic** | Budget Friendly | + 300 | 220 |
| **Riadi Advance** | Budget Friendly + | + 1,017 | 400 |
| **Riadi Premier** | Custom Plan & Wide Network | + 1,551 | 550 |
| **Riadi Executive** | Suits Your Executive Team | + 1,659 | 1,000 |
| **Riadi Elite** | VIP Network | + 1,776 | 1,500 |

Source: `https://www.medgulf.com.sa/home/riadi-sme-health-insurance` (also served at
`/home/napd-program`), read 11 November 2026. Prices are per-employee starting prices as
presented; see `sources/index.md` for the caveat.

### What this table is good for — and what it is not

**Good for:** explaining to a member that MEDGULF tiers are nested — Elite's network is the
largest, Basic's the smallest, and a hospital in Basic is very likely in Elite but not the
reverse. That ordering is useful when a member is choosing between tiers at renewal.

**Not good for:** naming a hospital. Note especially:

- **"Nested" is an assumption, not a published fact.** The provider *counts* rise with tier
  and the descriptions imply increasing breadth ("Wide Network", "VIP Network"), but MEDGULF
  does not state that a higher tier contains a lower one. Do not tell a user "if they take
  Basic they certainly take Elite". Say the counts, and say the list is not published.
- **A count is not a list.** "+ 300 Providers" tells a member nothing about whether *their*
  hospital is one of them.
- **No city dimension.** The counts are totals. Whether a provider is in Riyadh or Jazan is
  not stated anywhere public.

---

## The Class A / Class B problem — unchanged

Cards in Saudi Arabia commonly print Class A or Class B. MEDGULF's public pages do not use
either term. They publish **RIADI tier names**, which is a different vocabulary again.

| Card wording | MEDGULF's public wording | Mapping published? |
|---|---|---|
| Class A | Riadi Basic / Advance / Premier / Executive / Elite | **No** |
| Class B | (same five tier names) | **No** |

So a MEDGULF user who says "Class B" cannot be placed into a RIADI tier from public
information. Do not guess that Class A = Elite or any other pairing. Nothing supports it.

## Beyond RIADI

MEDGULF also sells **group health for large companies** (the RIADI page links onward to it)
and individual products (domestic workers health, visit visa, medical malpractice). None of
those publishes a tier table or a provider list on the public site. If a user is on a large
employer plan rather than RIADI, this skill knows nothing about their network either.

---

## What the agent must do for a MEDGULF user

1. Confirm the company is MEDGULF. If not, do not use this skill.
2. Establish what they hold: a RIADI tier name (Basic / Advance / Premier / Executive /
   Elite), or just Class A / Class B, or "my employer's plan".
3. **If they name a RIADI tier:** you may say which tier that is and how large its published
   provider network is, in relative terms. You still may not name a hospital.
4. **If they only know Class A / Class B:** say no mapping to MEDGULF tiers is published, and
   do not guess one.
5. **Do not name a hospital.** MEDGULF's provider list is not in this skill.
6. Give them what does work:
   - **Call MEDGULF health customer care — 8001188555 (24/7)** — and ask which hospitals are
     in their tier's network.
   - **Ask the hospital directly:** *"Do you bill MEDGULF [tier] directly?"*
7. State that coverage and networks change, and that an employer's contract can alter the
   network, so confirm before travelling.

MEDGULF contact details verified on the site: health customer care **8001188555** (24/7),
sales **920024292**, email `Customer-Service@medgulf.com.sa`.

---


### The answer block — use this shape every time

1. **What they hold:** MEDGULF medical policy — a RIADI tier if SME.
2. **Class:** RIADI Basic, Advance, Premier, Executive or Elite. Cards printing Class A/B cannot be
   mapped to a RIADI tier.
3. **What to say about the class:** quote the published provider counts — Basic +300 up to Elite
   +1,776. Do not treat the tiers as nested; MEDGULF never states that.
4. **What to do next:** call **8001188555** (24/7) or **920024292**.
5. **Always ask the hospital:** *"Do you bill MEDGULF [tier] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the five tiers, and the exact procedure for a MEDGULF user. |
| `tiers-and-packages.md` | The RIADI tier table in detail, plus what else MEDGULF sells. |
| `network/README.md` | Why there are no city files, what was checked, what would close it. |
| `sources/index.md` | Every URL checked and its result. |

---

## Change log

- 2026-11-11 — skill created. RIADI's five tiers, provider counts and starting prices
  captured from MEDGULF's public page. No provider list exists publicly; skill refuses to
  name hospitals.
