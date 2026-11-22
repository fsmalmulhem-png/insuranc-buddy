---
name: alsagr-saudi-network
description: Al Sagr Cooperative Insurance (الصقر للتأمين / alsagr.com) health insurance — its network is administered by TCS, and Al Sagr publishes exactly how a member checks it. Read only when the user's company is Al Sagr, to route them to TCS or the Alsagr Health app. Holds no provider names — never name a hospital.
---

# Al Sagr — health insurance, and the one company that says who holds the network

## Status

**Products and the verification route are known. No provider list.** Al Sagr sells health
insurance, and — uniquely among the seven companies checked — **states publicly that its
medical network is administered by a third party, TCS**, and gives the exact steps a member
takes to look up their own network.

Exactly how to check is published. The list itself is not. **No hospital may be named from
this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Al Sagr** and still not accept the member's class. This skill never
answers at company level. It holds no provider names, so its only correct provider answer is
**"I cannot confirm this"** — but unlike the other skills, it can hand the member a *working
lookup that returns a real answer*.

> *"Do you bill Al Sagr Class [A/B] directly?"*

---

## Why this company is different — the finding

Al Sagr's own FAQ asks and answers: **"How do I enquire about the medical network?"** The
published answer is that the network is managed by **TCS (the medical claims administrator)**,
and the member may check it three ways. Quoted from Al Sagr's site:

| Route | Detail |
|---|---|
| **Call TCS** | **8003037858** or **920012493**, 24/7 |
| **Alsagr Health app** | Android and iOS, linked from the FAQ |
| **TCS web portal** | `tcs-ksa.net:1192` — enter National ID and year of birth |

That is a complete, published, member-facing route to a class-specific answer. It is the only
one of the seven that spells out the mechanism rather than gesturing at "a wide network".

**But note what it still is not:** a list. It is a lookup that answers for *one member at one
hospital*, and it requires the member's National ID. The advisor cannot run it on someone's
behalf, and it cannot be converted into city tables. So the skill's job is to hand the member
the route, not to answer for them.

## What Al Sagr sells

Al Sagr advertises "over 48 diverse insurance products". Its retail e-commerce portal offers
only: Motor, Travel, Property, and **Medical Malpractice** (professional liability for
practitioners — not member treatment). Health insurance and the domestic-worker/visit-visa
lines sit behind claims and sales routes rather than the retail portal.

Health appears in the FAQ as a full product — with questions about medical cost, network
enquiry and policy cancellation (cancellations handled at
`Cancellation.Medical@alsagr.com`).

## Classes

| Aspect | Published? |
|---|---|
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |
| Which providers are in a class | **No** — but TCS can tell the member |

The class question is answered the same way: TCS knows, the advisory skill does not.

---

## What the agent must do for an Al Sagr user

1. Confirm the company is Al Sagr (Arabic: الصقر للتأمين). If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.**
5. Give them the route Al Sagr itself publishes — this is the strongest answer available for any
   company in this project:
   - **Call TCS on 8003037858 or 920012493 (24/7)** and ask whether a named hospital is in
     Al Sagr's network for their class.
   - **Or use the Alsagr Health app** — shows the member's own network.
   - **Or** the TCS portal `tcs-ksa.net:1192` with National ID and birth year.
   - **Al Sagr sales, if they are buying:** 920001043 (WhatsApp available); central line 8003040114.
6. Still give the hospital question, because the answer must ultimately come from the provider:
   *"Do you bill Al Sagr Class [A/B] directly?"*
7. State that coverage and networks change, so confirm before travelling.

**Do not tell the user their coverage is confirmed** just because TCS lists a hospital. TCS
answers for the network; the bill at the desk is still the hospital's call.

---


### The answer block — use this shape every time

1. **What they hold:** Al Sagr medical policy.
2. **Class:** ask for Class A / Class B; Al Sagr publishes no tier names.
3. **What to do next:** call **TCS on 8003037858 or 920012493** (24/7), use the **Alsagr Health**
   app, or the portal at `tcs-ksa.net:1192`.
4. **Always ask the hospital:** *"Do you bill Al Sagr Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the TCS finding, products, and the agent procedure. |
| `tiers-and-packages.md` | Al Sagr's health product, the class gap, and who holds the data. |
| `network/README.md` | The published lookup routes in full, and why they are not a file. |
| `sources/index.md` | Every URL checked and its result. |

---

## Change log

- 2026-11-11 — skill created. Al Sagr's FAQ published the TCS network route; captured in full.
  Retail portal checked (no health product for individuals). No provider names held.
