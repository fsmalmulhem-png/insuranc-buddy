---
name: saudi-enaya-saudi-network
description: Saudi Enaya Cooperative Insurance (العناية السعودية / saudienaya.com) health insurance — the ONE company in this set that publishes a real Class A/B/C mapping: A-Gold→SE_A, B-Silver→SE_B, with named network codes. Read when the user's company is Saudi Enaya, to state their class's network by name. Does not hold provider names — never name a hospital.
---

# Saudi Enaya — the one company that publishes Class A / Class B

## Status

**Class mapping published. Provider names NOT available.** Saudi Enaya publishes a full
benefits table per class, and each class carries a **named network code**: Class A-Gold →
`SE_A`, Class B-Silver → `SE_B`, Class C-Bronze → `SE_C+`, and VIP → `SE_VIP`.

That is the **first and only** company in this whole set (twelve checked) that bridges the
Class A / Class B wording on a card to something concrete. Every other insurer left that gap
open.

The provider *names* inside each network are still not published — the provider lookup requires
a member login. **No hospital may be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Saudi Enaya** and still not accept the member's class. This skill
answers at **class level** — which is exactly what the project requires — and stops short of
naming hospitals, because the network membership is not published.

---

## The class table — verified from Saudi Enaya's own site

Saudi Enaya publishes this on **both** its SME page and its Corporate page (the tables are
identical):

| Class | Network code | Room type | Max annual limit | Geographical coverage |
|---|---|---|---|---|
| **VIP** | `SE_VIP` | Suite | SAR 1,000,000 | World Wide 2 (or World Wide 1) |
| **A-Gold** | `SE_A` | Private | SAR 1,000,000 | World Wide 2 |
| **B-Silver** | `SE_B` | Semi-Private | SAR 1,000,000 | KSA & Home Country |
| **C-Bronze** | `SE_C+` `SE_C` `SE_C LTD` `SE_CR` | Shared | SAR 1,000,000 | KSA |

Within each class there are also benefit **options**: Option 1 / 2 / 3, and "Enhanced" or "Nil"
variants that change the co-payment on out-of-network treatment.

### What this means for a user — the answer this skill CAN give

This is the first skill that can say something real at class level:

> **"You hold Class B — in Saudi Enaya's published table that is B-Silver, which operates on
> the SE_B network, semi-private room, and coverage inside KSA and your home country."**

That is a genuine, sourced, class-level answer. It is not a hospital name, but it removes the
guesswork about what the card means — which no other insurer in this set allows.

## What is still missing

| Aspect | Published by Saudi Enaya? |
|---|---|
| Class names and mapping | **YES** ✅ |
| Network code per class | **YES** ✅ |
| Benefits, limits, co-pay per class | **YES** ✅ |
| **Which hospitals are in SE_A / SE_B** | **No** — needs member login |
| Provider list as a file | **No** |

The network-provider page (`/network-provider`) redirects to the login screen. The app bundle
reveals the mechanism: a POST to
`corporate.saudienaya.com/SEMobileApp/api/Provider/GetNetWorkList`, carrying `PolicyNo`,
`MemberNo` and `IdentityNo` — i.e. **the list is fetched for one identified member**, not for
the public.

---

## What the agent must do for a Saudi Enaya user

1. Confirm the company is Saudi Enaya (Arabic: العناية السعودية). If not, do not use this skill.
2. Ask the class on their card — **now this genuinely matters**, because Saudi Enaya's classes
   are real and named. Class A → A-Gold, Class B → B-Silver. If they don't know, say where to look.
3. **Tell them what their class means** from the table above: network code, room type, area.
   This is the skill's real value — say it.
4. Ask the city and the service.
5. **Do not name a hospital.** Say plainly that Saudi Enaya does not publish which hospitals sit
   in each network; that requires the member login.
6. Give them what does work:
   - **Log in to saudienaya.com** and open the **Network Provider** section — it lists the
     network for their own policy.
   - **Call 8001240551** or **920001177**.
   - **Ask the hospital directly:** *"Do you bill Saudi Enaya Class [A/B] under SE_[code] directly?"*
     — naming the network code is useful here, because the hospital's billing desk works from it.
7. State that coverage and networks change, so confirm before travelling.

---


### The answer block — use this shape every time

1. **What they hold:** Saudi Enaya medical policy.
2. **Class:** VIP, A-Gold (`SE_A`), B-Silver (`SE_B`) or C-Bronze (`SE_C+`/`SE_C`/`SE_C LTD`/`SE_CR`).
   This is one of the few companies where a card's A/B maps to a named network.
3. **What to say about the class:** state the network code and the room type from
   `tiers-and-packages.md`. Do not name a hospital — the provider list is member-only.
4. **What to do next:** log in at saudienaya.com → **Network Provider**, or call **8001240551** /
   **920001177**.
5. **Always ask the hospital:** *"Do you bill Saudi Enaya Class [A/B] under SE_[code] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the class table, and the agent procedure. |
| `tiers-and-packages.md` | Full class and benefit detail, options, co-payment structure. |
| `network/README.md` | The provider API, why membership is not public. |
| `sources/index.md` | Every URL and result, including the wrong-domain finding. |

---

## A note on the domain you were given

`saudi-enaya.com` (the URL supplied) **has no DNS record** — it does not exist. Two neighbouring
domains are also wrong: `enaya.com.sa` is a Riyadh cleaning company, and the insurer is at
**`saudienaya.com`**. See `sources/index.md`; this is recorded so nobody repeats the search.

---

## Change log

- 2026-11-11 — skill created. Class mapping, network codes and benefit tables captured. This is
  the first skill in the set with a published Class A/B bridge. Provider names still withheld.
