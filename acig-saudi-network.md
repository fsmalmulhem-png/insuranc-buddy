---
name: acig-saudi-network
description: ACIG / المجموعة المتحدة للتأمين التعاوني (أسيج / acig.com.sa) health insurance — it sells medical cover and runs a member portal called Toshfa, but publishes no provider list and no network-check route. Read only when the user's company is ACIG, to hand them the contact route. Holds no provider names — never name a hospital.
---

# ACIG (أسيج) — health insurance, and a member portal that is not a directory

## Status

**Products known. No provider list. No published network-check route.** ACIG sells medical
insurance and operates a member portal ("Toshfa") which does contain a provider lookup — but
that lookup sits **behind a login**, so it cannot answer for anyone who is not already a
signed-in member, and it cannot be converted into city tables.

Unlike Al Sagr, ACIG does **not** publish a "how to check your network" answer anywhere on
its public site. **No hospital may be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **ACIG** and still not accept the member's class. This skill never
answers at company level. It holds no provider names, so its only correct provider answer is
**"I cannot confirm this"**, plus the hospital's phone number and the exact question:

> *"Do you bill ACIG Class [A/B] directly?"*

---

## What ACIG publishes — verified

ACIG is **المجموعة المتحدة للتأمين التعاوني (أسيج)** — United Cooperative Assurance. Its site
describes itself as selling motor, **health (تأمين صحي)**, travel and domestic-worker cover.

| What | Detail |
|---|---|
| Public routes | `products`, `all-products`, `individuals-insurance`, `company-insurance`, `business`, `download-center`, `frequently-asked-questions`, `customer-service`, `contact-us`, `requirements` |
| Health product | Present — `MedicalInsurance`, `medicalOnlineProductIds = [82, 83]` (two online medical products) |
| Cancellation | `cancel-medical-insurance` route exists |
| Member portal | **Toshfa** at `medonline.acig.com.sa/MemberPortal/` |
| Public network list | **None** |
| Public network-check instructions | **None** |

### The Toshfa portal — what it is and is not

ACIG's member portal is a separate Angular application titled **"Toshfa"**. Its bundle
contains provider-related code — `Provider`, `ProviderOnline`, `ProviderGroup_GroupName`,
`ProviderBindInfo`, `ProviderEndoDetails`, `fa-hospital-o` — so it plainly has a provider
lookup.

**But every one of those routes is behind `canActivate`**, ACIG's authentication guard. Calling
the route without a session returns 404, and the guard redirects unauthenticated users. So:

- A **member** can see their own network in Toshfa.
- **Nobody else can**, and the advisor cannot read it, cite it, or convert it.

This is the key contrast with Al Sagr: both outsource/member-gate their network, but Al Sagr
tells you publicly *that the network is run by TCS and here are the numbers*, while ACIG
publishes no equivalent sentence. The capability exists; the instruction does not.

## Classes

| Aspect | Published by ACIG? |
|---|---|
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |
| Class → provider mapping | **No** |
| Provider list (any format) | **No** — only behind the member login |
| How a member checks their network | **No public instruction** |

---

## What the agent must do for an ACIG user

1. Confirm the company is ACIG / أسيج. If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that ACIG does not publish its network list.
5. Give them what does work:
   - **If they are a member:** log in to the **Toshfa member portal**
     (`medonline.acig.com.sa/MemberPortal/`) — provider search is there once signed in.
   - **By phone:** ACIG support **8001246999**, or WhatsApp **920012331**.
   - **Ask the hospital directly:** *"Do you bill ACIG Class [A/B] directly?"*
6. State that coverage and networks change, so confirm before travelling.

**Do not claim the Toshfa portal works without an account**, and do not describe its contents
as if you had seen them — the skill only knows the route names from the app bundle, not what
they display.

---


### The answer block — use this shape every time

1. **What they hold:** ACIG medical policy — individual or corporate.
2. **Class:** ask for Class A / Class B; ACIG publishes no tier names or A/B mapping.
3. **What to do next:** if they are a member, log in to **Toshfa** and open Service Providers.
   Otherwise call **8001246999** or WhatsApp **920012331**.
4. **Always ask the hospital:** *"Do you bill ACIG Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the Toshfa finding, products, and the agent procedure. |
| `tiers-and-packages.md` | ACIG's health products and the class gap. |
| `network/README.md` | The portal, why it is not a file, and what was checked. |
| `sources/index.md` | Every URL and its result. |

---

## Change log

- 2026-11-11 — skill created. ACIG's site and app bundle inspected; health products and contact
  numbers captured, member portal identified, no public network data exists.
