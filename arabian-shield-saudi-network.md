---
name: arabian-shield-saudi-network
description: Arabian Shield Cooperative Insurance (الدرع العربي / der3.com) health products — it sells SME medical insurance only, with no published tiers and no provider list. Read only when the user's company is Arabian Shield, to hand them the verification route. Holds no provider names — never name a hospital.
---

# Arabian Shield — what it sells, and what it publishes

## Status

**Products known. No tiers, no provider list.** Arabian Shield offers an **SME medical
insurance** product and states it works through "a wide and distinguished network of
hospitals" — but publishes no tier names, no class list, and no provider file of any kind.

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Arabian Shield** and still not accept the member's class. This skill
never answers at company level. Since it holds no provider names, its only correct provider
answer is **"I cannot confirm this"**, plus the hospital's phone number and the exact
question:

> *"Do you bill Arabian Shield Class [A/B] directly?"*

---

## What Arabian Shield publishes — verified

Its product menu (Arabic and English) lists: motor, travel, personal accident, medical
malpractice, artisans, home, and **health insurance**. Only one health product is described:

| Product | Arabian Shield's own words | Tiers published? | Network published? |
|---|---|---|---|
| **SME Medical Insurance** ("تأمين صحي — وثيقة التأمين الخاصة بالمنشآت/الشركات الصغيرة") | "seeks to provide a healthy environment and guarantees the right of insured to receive full treatment and health care he needs through a **wide and distinctive network of hospitals**" | **No** | **No** |
| Medical Malpractice | For doctors, not member treatment | — | — |

That is the entire published description of their health product. One sentence about a wide
network, with nothing behind it.

## What is absent — all of it

| Question a member has | Published? |
|---|---|
| What tiers/classes exist? | **No** |
| What is each class called? | **No** |
| Is my class A or B? | **No** |
| Which hospitals are in my class's network? | **No** |
| Which hospitals are in the network at all? | **No** — only the phrase "wide and distinctive" |
| Any city breakdown? | **No** |
| Any downloadable file? | **No** — checked sitemap, products, programs, downloads |

### The "Medical Portal"

Arabian Shield links a **Medical Portal** tile on its site. It is not a provider directory —
it is a member-services platform (`apps.der3.com/customer`, a Flutter app shell behind a
login). Reaching it needs a member account. It does not publish a network, so it cannot be
converted into a list.

## Scale note, worth recording

Arabian Shield is a smaller insurer than Bupa or Tawuniya. Its public website carries fewer
products and, for health, one SME product. That is consistent with a smaller member base —
but this skill does not claim that, because nothing published states it. What is verifiable
is narrower: **it publishes less**.

---

## What the agent must do for an Arabian Shield user

1. Confirm the company is Arabian Shield (Arabic: الدرع العربي; website `der3.com`). If not,
   do not use this skill.
2. Ask the class shown on the card (Class A / Class B). If they do not know, say where to look
   and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that Arabian Shield does not publish its network.
5. Give them what does work:
   - **Call Arabian Shield medical insurance line — 8001 240 240** (Arabic site lists this
     under "التأمين الطبي"; customer service is 8001 247 247). Ask which hospitals are in their
     class's network.
   - **Ask the hospital directly:** *"Do you bill Arabian Shield Class [A/B] directly?"*
6. State that coverage and networks change, so confirm before travelling.

---


### The answer block — use this shape every time

1. **What they hold:** Arabian Shield SME medical policy.
2. **Class:** ask for Class A / Class B; none published.
3. **What to do next:** call the medical line **8001 240 240**, or customer service **8001 247 247**.
4. **Always ask the hospital:** *"Do you bill Arabian Shield Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, products, and the agent procedure. |
| `tiers-and-packages.md` | The one health product and what is absent. |
| `network/README.md` | What was checked, why no city files exist. |
| `sources/index.md` | Every URL and its result. |

---

## Change log

- 2026-11-11 — skill created. Arabian Shield's public site read; one SME health product, no
  tiers, no provider list. Skill holds no provider data and refuses to name hospitals.
