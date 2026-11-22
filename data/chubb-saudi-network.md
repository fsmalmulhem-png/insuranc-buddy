---
name: chubb-saudi-network
description: Chubb Arabia Cooperative Insurance (chubb.com.sa) — a property & casualty insurer in Saudi Arabia; it sells commercial P&C, motor, travel, personal accident and group life, but NO medical/health insurance. If a user says they hold Chubb health in KSA, that is almost certainly wrong. Read only to establish that, then redirect.
---

# Chubb Arabia — a P&C insurer with no health product in Saudi Arabia

## Status

**No health insurance.** Chubb Arabia Cooperative Insurance Company describes itself as a
*"multi-line property and casualty insurer"* and lists its portfolio as *"commercial property and
casualty insurance, personal accident coverage, and group life insurance."*

Its published product menu — **17 products** — contains no medical or health line.

So a person in Saudi Arabia cannot hold "Chubb health insurance." If someone says they do, the
card is from another company, or they mean **group life** or **personal accident** (both of which
are often confused with health), or they hold a Chubb policy from another country.

Verified 11 November 2026. See `sources/index.md`.

---

## Do not confuse these three

A user saying "Chubb health" could mean any of the following, and they are **not** the same thing:

| What they may mean | What it is | Covered by this skill? |
|---|---|---|
| **Chubb Arabia medical/health** | **Does not exist** in KSA | — |
| **Group life** | Pays a sum on death; not treatment | No hospital network |
| **Personal accident** | Pays for accidental injury/death | Not routine care |
| **Travel insurance** | Emergency medical *while travelling* | Not domestic treatment |
| **Chubb in another country** | Chubb has health products in some markets | Outside KSA — this skill cannot speak to it |

**The travel-insurance trap is the most likely.** Chubb Arabia does sell travel insurance, and
travel policies routinely include emergency medical cover. A traveller may reasonably say "I have
Chubb medical" when they mean their travel policy. That is not a domestic health network and
cannot be used at a Saudi hospital for routine care.

---

## What Chubb Arabia publishes — verified

**Chubb Arabia Cooperative Insurance Company** — part of the global Chubb Group. Offices in
**Khobar, Riyadh and Jeddah**.

### The complete product list (17)

Casualty · Civil Liability for Populated Areas & High-Risk Activities · Contractors Plant &
Machinery · Cyber Security · Directors & Officers Liability · Engineering · Fidelity Guarantee ·
Financial Lines · Jewellers Block · Marine · Money Insurance · **Motor** · Professional Indemnity ·
Property & Business Interruption · Sabotage & Terrorism · **Travel Insurance** ·
Workmen's Compensation / Employer Liability

**No medical, no health, no group medical.**

### What the About page states outright

> "Chubb Arabia Cooperative Insurance Company is a leading **multi-line property and casualty
> insurer** operating across the Kingdom of Saudi Arabia."

> "Chubb Arabia offers a broad portfolio of products, including **commercial property and casualty
> insurance, personal accident coverage, and group life insurance**."

That sentence is the authoritative statement: P&C, personal accident, group life. Medical is
absent by design, not by omission.

## Classes and networks

Not applicable — there is no health product, so there are no tiers, no provider network and no
Class A / Class B.

## Where Chubb sits in this set

| Company | Has a health product? |
|---|---|
| Wataniya | **No** — P&C, travel, malpractice |
| **Chubb Arabia** | **No** — P&C, travel, personal accident, group life |
| All other 18 | Yes |

Chubb is the **second** company checked with no health product at all. Both are important
negatives: they guard against a user assuming a large global brand must sell health locally.

---

## What the agent must do for someone who says "Chubb"

1. **Ask them to read the product name and company name off their card or policy.** Do not proceed
   on the spoken name.
2. **If it says Chubb Arabia and they believe it is medical cover**, tell them plainly: Chubb Arabia
   does not sell health insurance in Saudi Arabia. It sells P&C, motor, travel, personal accident
   and group life.
3. **Check for the travel-insurance confusion.** If they are a traveller, their Chubb policy may be
   travel insurance with emergency medical cover. Explain that it covers emergencies abroad or
   while travelling, not routine or elective treatment at a Saudi hospital.
4. **Check for group life confusion.** Group life is a death benefit, not a treatment benefit.
5. **If it emerges the policy is from Chubb in another country**, say plainly that this skill covers
   Saudi Arabia only and you cannot confirm that policy.
6. **Do not name a hospital.** There is no Chubb Arabia health network to name one from.
7. Contacts, if they need to confirm directly with Chubb Arabia: **8001160038** (toll-free IN KSA),
   **920024429** (outside KSA / WhatsApp).

### The answer block — use this shape every time

1. **What they hold:** Chubb Arabia policy, product unknown — likely travel, group life or P&C.
2. **Class:** not applicable — Chubb sells no health, so there is no Chubb health class.
3. **What to do next:** read the product name off the policy. Travel cover pays emergency medical
   abroad; group life is a death benefit; neither is domestic health. For Saudi health cover they
   need a different insurer.
4. **Always ask the hospital:** *"Do you bill Chubb Class [A/B] directly?"* — then explain that a
   Chubb Arabia policy is unlikely to cover routine treatment, whatever the answer.


---

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the confusion table, what Chubb actually sells, procedure. |
| `tiers-and-packages.md` | Product list and the personal-accident / group-life distinction. |
| `network/README.md` | Why there is no network — no health product. |
| `sources/index.md` | Every URL, including the `/sa` redirect problem. |

---

## Note on the URL supplied

`chubb.com/sa` (the URL given) **redirects to an ad-tracking pixel**, returning no page content.
`chubb.com/sa/en` also fails. The working Saudi site is the country domain
**`chubb.com.sa`**. See `sources/index.md`.

---

## Change log

- 2026-11-11 — skill created. All 17 Chubb Arabia products enumerated; **no health product
  exists**. Skill resolves the travel/group-life confusions and redirects.

