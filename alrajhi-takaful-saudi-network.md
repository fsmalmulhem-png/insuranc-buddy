---
name: alrajhi-takaful-saudi-network
description: Al Rajhi Takaful (تكافل الراجحي / alrajhitakaful.com) health insurance — runs a public medical provider locator search but publishes no downloadable network file. Read only when the user's company is Al Rajhi Takaful, to point them at the locator and the medical line. Holds no provider names — never name a hospital.
---

# Al Rajhi Takaful — a public provider locator, no file

## Status

**Products known. A public provider search exists. No downloadable list.** Al Rajhi Takaful
runs a **public, no-login medical provider locator** at
`alrajhitakaful.com/en/medical-provider-locator` — the first company in this set with a
genuinely open, unauthenticated lookup that is not gated behind a member account.

But it returns results only interactively (type-ahead + "near me"), with no bulk export and no
file. So the advisor cannot read a city's provider list ahead of a question. **No hospital may
be named from this skill.**

Verified 11 November 2026. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept **Al Rajhi Takaful** and still not accept the member's class. This skill
never answers at company level. It holds no provider names, so its only correct provider answer
is **"I cannot confirm this"** — plus a working lookup and the hospital question:

> *"Do you bill Al Rajhi Takaful Class [A/B] directly?"*

---

## What Al Rajhi Takaful publishes — verified

| What | Detail |
|---|---|
| Health — business | `alrajhitakaful.com/en/business/health-insurance` — SME health insurance |
| Health — individual | `product-health`, `health-purchase`, `domestic-health-purchase` |
| **Provider locator** | **`/en/medical-provider-locator` — PUBLIC, no login** |
| Related | `value-added-medical-services`, health claims, medical malpractice |
| Downloadable network file | **None** |

### The locator — what it does and does not give us

The page loads a live search: a text box, a "near me" control, and a Google-Maps result pane.
On first load it reads **"0 results"** and *"results will appear here as you type."* So it is a
genuine search over a provider dataset.

**What this means in practice:**

- A **user** can search a hospital name and see whether it is in the network — this is the
  single most useful self-service route of the nine companies checked.
- An **advisor** cannot: the results come from a client-side API call that requires a browser
  session. The site returns **403** to any non-browser request, and the result data is not in
  the page HTML.

So the skill's job is to hand over the locator, not to answer from it.

## Classes

| Aspect | Published? |
|---|---|
| Tier/class names | **No** |
| Class A / Class B mapping | **No** |
| Class → provider mapping | **No** |
| Provider list as a file | **No** |
| **Public per-hospital lookup** | **Yes — the locator** |

Like every other company checked, Al Rajhi Takaful publishes no A/B mapping. Unlike any
before it except Tawuniya, it does publish a way for a user to get a per-hospital answer without
calling anyone.

---

## What the agent must do for an Al Rajhi Takaful user

1. Confirm the company is Al Rajhi Takaful (Arabic: تكافل الراجحي). If not, do not use this skill.
2. Ask the class on their card (Class A / Class B). If they do not know, say where to look and wait.
3. Ask the city and the service.
4. **Do not name a hospital.** Say plainly that the network is not published as a list.
5. Give them the working route — this is the strongest self-service answer in the set:
   - **Search the locator:** `alrajhitakaful.com/en/medical-provider-locator`
     (Arabic: `/ar/medical-provider-locator`). Type the hospital name, or use "near me".
   - **Medical line, 24/7: 8001184444.** Other lines are 8:00–16:00; local number **920004414**.
   - **Ask the hospital directly:** *"Do you bill Al Rajhi Takaful Class [A/B] directly?"*
6. State that coverage and networks change, so confirm before travelling.

**Do not describe what the locator returns.** The skill knows the locator's interface, not its
data. A member must run the search themselves.

---


### The answer block — use this shape every time

1. **What they hold:** Al Rajhi Takaful medical policy.
2. **Class:** ask for Class A / Class B; no A/B mapping is published.
3. **What to do next:** search the hospital at
   `alrajhitakaful.com/en/medical-provider-locator`, or call the medical line **8001184444** (24/7).
4. **Always ask the hospital:** *"Do you bill Al Rajhi Takaful Class [A/B] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the locator finding, and the agent procedure. |
| `tiers-and-packages.md` | Health products and the class gap. |
| `network/README.md` | The locator in detail, why it is not a file, what was checked. |
| `sources/index.md` | Every URL and its result. |

---

## Change log

- 2026-11-11 — skill created. Al Rajhi Takaful's public provider locator identified and
  documented. Contact numbers captured. No provider names held.
