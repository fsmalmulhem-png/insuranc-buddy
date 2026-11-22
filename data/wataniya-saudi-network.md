---
name: wataniya-saudi-network
description: Wataniya / The National Insurance Company (الشركة الوطنية للتأمين / wataniya.com.sa) — a Saudi insurer that sells NO health insurance at all: its product lines are motor, travel, property, engineering, marine, liability, aviation, life/accident and medical malpractice. If a user says they hold "Wataniya health", the card is almost certainly Tawuniya (التعاونية) and must be checked.
---

# Wataniya (الوطنية للتأمين) — an insurer with no health product

## Status — and a name trap that matters

**Wataniya sells no health insurance.** Its product catalogue is motor, travel, home, property,
engineering, marine cargo, liability, aviation hull, life & personal accident, and **medical
malpractice** — plus SME variants of the corporate lines.

It has **no medical/health product for members at all.** So a person cannot hold "Wataniya
health insurance" — and if someone says they do, they are almost certainly holding a different
company's policy.

**The most likely confusion: Tawuniya (التعاونية).** The two names are one letter apart in English
and are routinely mixed up. They are entirely different insurers:

| | Wataniya | Tawuniya |
|---|---|---|
| Arabic | **الوطنية** للتأمين | **التعاونية** |
| Domain | `wataniya.com.sa` | `tawuniya.com.sa` |
| Sells health? | **No** | Yes |
| Location | Jeddah | Riyadh |

This skill's job is to catch that confusion and send the user to the right skill.

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Wataniya** and still not accept the member's class. But before that
question can be asked, the company has to be the right one.

---

## What Wataniya publishes — verified

**الشركة الوطنية للتأمين** — The National Insurance Company, trading online as *Wataniya*. Based
in Jeddah.

### Individual products
Motor · Travel · Home · **Medical Malpractice**

### Corporate products
Motor · Property · Engineering · Marine Cargo · Liability · Life & Personal Accident ·
Aviation Hull · Other (extended warranty, fine arts, bankers blanket bond, events cancellation,
cyber risk, heritage buildings, domestic labour)

### SME products
Same corporate lines, under a `Segment=SME` filter.

### The health-adjacent line, and why it is not health

Wataniya sells **اخطاء المهن الطبية — Medical Malpractice**:

> "إذا كنت ممارسًا طبيًا يوفر لك هذا التـأمين حماية قانونية... تحميك من أي شكاوى أو اخطاء تتعلق
> بالسهو أثناء مزاولة المهنة"

*If you are a medical practitioner, this insurance provides legal protection... against complaints
or errors relating to negligence while practising the profession.*

That is **professional liability for doctors**, not treatment cover for a patient. A hospital
network is not involved.

## Classes

Not applicable — there is no health product to have classes for. No tiers, no provider list, no
network.

---

## What the agent must do when someone says "Wataniya"

1. **Ask them to read the company name off their card.** Do not proceed on the spoken name alone.
2. **If the card says الوطنية (Wataniya / National Insurance)** and they believe they have health
   cover, tell them plainly: Wataniya does not sell health insurance, so either the product is
   something else (malpractice is the only medical-adjacent line) or the card is from another
   company. Do not guess.
3. **If the card says التعاونية (Tawuniya)** — use the `tawuniya-saudi-network` skill instead.
   Tawuniya does sell health, and that skill explains what it publishes and why it names no
   provider.
4. If they are actually asking about a **medical malpractice** policy (they are a practitioner),
   note that this is liability cover and its claims go to Wataniya, not to a hospital network.
5. Requesting a quote or making a claim at Wataniya: **8001188855** (toll-free, 8:45–16:45),
   WhatsApp **9668001188855** (24h), international **966126013400**.

### The answer block — use this shape every time

1. **What they hold:** Wataniya card, product unknown.
2. **Class:** not applicable — Wataniya sells no health, so there is no Wataniya health class.
3. **What to do next:** read the company name off the card. If it is التعاونية, switch to the
   Tawuniya skill. If it is الوطنية, the policy is non-health, or the card belongs to another insurer.
4. **Always ask the hospital:** *"Do you bill Wataniya Class [A/B] directly?"* — and if the card
   turns out to name a different insurer, ask it with that insurer's name instead.


---

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the Tawuniya confusion, what Wataniya actually sells, procedure. |
| `tiers-and-packages.md` | Full product list and the malpractice distinction. |
| `network/README.md` | Why there is no network — there is no health product. |
| `sources/index.md` | Every URL and result. |

---

## Change log

- 2026-11-11 — skill created. Wataniya's full product menu enumerated; **no health product
  exists**. Skill redirects health queries to the correct company rather than inventing cover.

