---
name: salama-iaic-saudi-network
description: Salama / Saudi IAIC Cooperative Insurance (سلامة / salama.com.sa) health insurance — sells medical cover for corporates and SMEs (product "Raha"), but publishes no provider list and no network lookup. Read when the user's company is Salama, to hand them the contact route. Holds no provider names — never name a hospital.
---

# Salama (سلامة) — medical cover, no published network

## Status

**Products known. No provider list, no public lookup.** Salama sells medical insurance to
**corporates** and to **SMEs** (under the product name **راحة / Raha**), but publishes no hospital
list and no way for a member to search the network. **No hospital may be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Salama** and still not accept the member's class. This skill never answers
at company level. It holds no provider names, so its only correct provider answer is
**"I cannot confirm this"**, plus the hospital's phone number and the exact question:

> *"Do you bill Salama Class [A/B] directly?"*

---

## What Salama publishes — verified

Salama is **Saudi IAIC Cooperative Insurance Company** (سلامة). The site's medical section has
three routes:

| Route | Product |
|---|---|
| `/products/medical-insurance` | Medical insurance landing + quote request form |
| `/products/medical-insurance/corporate-insurance` | **Corporate / company medical** |
| `/products/medical-insurance/sme-raha-insurance` | **SME medical — "راحة" (Raha)** |

Both product pages are largely a **quote-request form** (persons count, comments, document
upload) rather than a benefits table. There is no tier list, no class list and no provider list.

### The one network reference — and what it actually is

Salama's cash-claim form contains a field:

> **سبب عدم تلقي العلاج ضمن الشبكة الطبية المعتمدة (PPN)**
> *"Reason for not receiving treatment within the approved medical network (PPN)"*

Two things follow, and both are worth recording:

1. **Salama states it has an approved medical network, called a PPN** — Preferred Provider
   Network. So a network exists and has a name.
2. **The PPN is referenced only inside a claim form.** Salama never publishes what is in it —
   no list, no search, no city breakdown. The abbreviation appears once, as a dropdown reason in
   a form a member fills *after* they have already been treated.

That is the same pattern as SAICO's "category and network" sentence: the insurer names the
mechanism and withholds the contents.

## Classes

| Aspect | Published by Salama? |
|---|---|
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |
| Benefits per class | **No** |
| Class → provider mapping | **No** |
| Provider list / PPN contents | **No** |

Salama's public pages carry no tier vocabulary at all — not even a product-name ladder.

---

## What the agent must do for a Salama user

1. Confirm the company is Salama / Saudi IAIC (Arabic: سلامة). If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that Salama does not publish its PPN — the approved
   medical network — and that it is only referenced inside claim forms.
5. Give them what does work:
   - **Call Salama:** unified **920023355** / **8002440002**; WhatsApp **920002061**.
   - **Log in** at `salama.com.sa/login` — a member account may show their network.
   - **Ask the hospital directly:** *"Do you bill Salama Class [A/B] directly?"* — and mention
     **PPN**, since that is the term Salama's own staff use.
6. State that coverage and networks change, so confirm before travelling.

---


### The answer block — use this shape every time

1. **What they hold:** Salama medical policy — corporate or SME (Raha).
2. **Class:** ask for Class A / Class B; no tiers published.
3. **What to do next:** call **920023355** / **8002440002**, or WhatsApp **920002061**. Use Salama's
   own term — the **PPN** — when asking.
4. **Always ask the hospital:** *"Do you bill Salama Class [A/B] PPN directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, products, the PPN finding, procedure. |
| `tiers-and-packages.md` | Products and the class gap. |
| `network/README.md` | The PPN reference, what was checked, why no city files. |
| `sources/index.md` | Every URL and result. |

---

## Change log

- 2026-11-11 — skill created. Medical products and the PPN reference identified; no provider
  data published. No provider names held.
