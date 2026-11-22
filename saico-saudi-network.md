---
name: saico-saudi-network
description: SAICO / Saudi Arabian Cooperative Insurance (الشركة السعودية للتأمين التعاوني / saico.com.sa) health insurance — sells SME and corporate medical cover but publishes no provider list and no network lookup. Read only when the user's company is SAICO, to hand them the contact route. Holds no provider names — never name a hospital.
---

# SAICO — health insurance, no published network

## Status

**Products known. No provider list, no public lookup.** SAICO sells **Medical for SMEs** and
**Medical for Corporates**, but publishes no hospital list and no way to search one.
**No hospital may be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **SAICO** and still not accept the member's category or class. This skill
never answers at company level. It holds no provider names, so its only correct provider answer
is **"I cannot confirm this"**, plus the hospital's phone number and the exact question:

> *"Do you bill SAICO Class [A/B] directly?"*

---

## What SAICO publishes — verified

SAICO is **الشركة السعودية للتأمين التعاوني** (Saudi Arabian Cooperative Insurance Company). Its
site lists medical alongside motor, travel, property, engineering, marine, liability, cyber and
life.

| Health product | Page |
|---|---|
| **Medical — for SMEs** | `/service/medical/` |
| **Medical — for Corporates** | `/service/medical-2/` |
| Medical Malpractice | `/service/personal-insurance-medical-malpractice/` (professional liability, not member treatment) |
| SME Group Life | `/service/sme-group-life/` (life, not health) |

Both medical pages describe cover in general terms — "hospitalization, consultations,
surgeries, and emergency treatments", plus "dental and optical cover, wellness programs, and
telemedicine" — and then invite the reader to fill in a contact form.

### What is absent

| Aspect | Published by SAICO? |
|---|---|
| Provider list (any format) | **No** |
| Public provider/network lookup | **No** |
| City-level network | **No** |
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |

### A useful clue hidden in the FAQ

SAICO's FAQ mentions, in its medical cash-reimbursement section, that reimbursement is settled
*"according to the prevailing rates for the **category and network** of the customer"*, and that
for non-emergency cases *"prior approval from SAICO is required"*.

Two things follow, and both matter:

1. **SAICO confirms internally that a "category" and a "network" exist** — so coverage really is
   set per member, exactly as the project's interviews found.
2. **Neither the categories nor the network is published.** The FAQ names the concepts and never
   lists them. That is the cleanest possible illustration of the project's thesis: the insurer
   knows the category matters, and still does not tell the member what the categories are.

---

## What the agent must do for a SAICO user

1. Confirm the company is SAICO (Arabic: الشركة السعودية للتأمين التعاوني — Saudi Arabian
   Cooperative Insurance). If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that SAICO does not publish its medical network.
5. Give them what does work:
   - **Medical services line: 920000563 — stated as 24/7.** (SAICO's site: "All Services:
     8:00 AM – 4:00 PM; Medical Services: 24/7".)
   - **Call center 8001242002**, WhatsApp **920013380**.
   - **Ask the hospital directly:** *"Do you bill SAICO Class [A/B] directly?"*
   - Note that for non-emergency treatment SAICO requires prior approval — worth mentioning,
     because it affects what the member should do before attending.
6. State that coverage and networks change, so confirm before travelling.

---


### The answer block — use this shape every time

1. **What they hold:** SAICO medical policy — SME or corporate.
2. **Class:** ask for Class A / Class B. SAICO's FAQ refers to "the category and network of the
   customer" but publishes neither.
3. **What to do next:** call **920000563** (medical services, 24/7), **8001242002**, or WhatsApp
   **920013380**. Note non-emergency care needs prior approval.
4. **Always ask the hospital:** *"Do you bill SAICO Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, products, the FAQ clue, and the agent procedure. |
| `tiers-and-packages.md` | Products, the "category and network" finding, the class gap. |
| `network/README.md` | What was checked, why no city files exist. |
| `sources/index.md` | Every URL and result. |

---

## Change log

- 2026-11-11 — skill created. SAICO's WordPress site enumerated in full; two medical products,
  no network. The FAQ's "category and network" sentence recorded as evidence. No provider names.
