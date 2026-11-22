---
name: walaa-saudi-network
description: Walaa Cooperative Insurance (ولاء للتأمين التعاوني / walaa.com) health insurance — sells medical and medical-SME cover but publishes no provider list and no network lookup. Read only when the user's company is Walaa, to hand them the contact route. Holds no provider names — never name a hospital.
---

# Walaa (ولاء) — health insurance, no published network

## Status

**Products known. No provider list, no public network lookup.** Walaa sells **Medical**,
**Medical SME**, domestic-worker health and medical malpractice cover, but publishes no hospital
list and no way for a user to search one. **No hospital may be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Walaa** and still not accept the member's class. This skill never
answers at company level. It holds no provider names, so its only correct provider answer is
**"I cannot confirm this"**, plus the hospital's phone number and the exact question:

> *"Do you bill Walaa Class [A/B] directly?"*

---

## What Walaa publishes — verified

Walaa is **شركة ولاء للتأمين التعاوني** — Walaa Cooperative Insurance. Its site is a React
application; the product list is enumerable from the app itself.

| Health product (internal code → label) | |
|---|---|
| `medical` → **Medical** | Individual / group medical |
| `medical_sme` → **Medical SME** | SME medical |
| `domestic` → **Domestic** | Domestic workers |
| `visitor` → **Visitor Visa** | Visitors |
| medical malpractice | Professional liability (not member treatment) |

Walaa's own label mapping, taken from its bundle:
`MEDICAL:"Medical", DOMESTIC:"Domestic", VISITOR:"Visitor Visa", PROTECTION:"Protection & Savings", SME_MEDICAL:"Medical SME"`.

### What is absent

| Aspect | Published by Walaa? |
|---|---|
| Provider list (any format) | **No** |
| Public provider/network lookup | **No** |
| City-level network | **No** |
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |

### The Branch Locator is not a provider search

Walaa has a **Branch Locator** page (`/pages/Branch-Locator/`). This finds **Walaa's own
offices**, not hospitals in its medical network — the same trap as Tawuniya's network page,
which defaulted to showing branch offices. Do not present it as a network search.

Walaa also has a **Document Library** page and a **FAQ** page. Both are client-rendered from a
CMS (`apicoregcp.walaa.com/cms/`), and neither exposes a network file in the app code. The
pages were opened; they returned only the application shell, with content fetched at runtime.

---

## Classes

Walaa publishes no class or tier names and no A/B mapping — the same gap as all nine other
companies checked. **Class A / Class B from a card cannot be mapped to anything in this skill.**

---

## What the agent must do for a Walaa user

1. Confirm the company is Walaa (Arabic: ولاء للتأمين التعاوني). If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that Walaa does not publish its medical network.
5. Give them what does work:
   - **Walaa's Contact page** — `walaa.com/contact-walaa` — carries the current phone and email.
     **The skill does not hold a Walaa phone number**, because none could be read from the site;
     do not invent one. Point the user at the Contact page.
   - **The Walaa app / member dashboard** — for a signed-in member.
   - **Ask the hospital directly:** *"Do you bill Walaa Class [A/B] directly?"*
6. State that coverage and networks change, so confirm before travelling.

**Do not present the Branch Locator as a hospital search.** It lists Walaa offices.

---


### The answer block — use this shape every time

1. **What they hold:** Walaa medical or medical-SME policy.
2. **Class:** ask for Class A / Class B; no tiers published.
3. **What to do next:** use the number on **`walaa.com/contact-walaa`** — this skill holds no Walaa
   number because none could be read from the site. Do not invent one.
4. **Always ask the hospital:** *"Do you bill Walaa Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, products, and the agent procedure. |
| `tiers-and-packages.md` | Products and the class gap. |
| `network/README.md` | What was checked, why no city files exist, the Branch Locator trap. |
| `sources/index.md` | Every URL and result, including the build-output method. |

---

## Change log

- 2026-11-11 — skill created. Walaa's React app inspected; products enumerated, no network
  route exists. No provider names held. No phone number asserted, because none was readable.
