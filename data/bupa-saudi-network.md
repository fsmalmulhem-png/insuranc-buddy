---
name: bupa-saudi-network
description: Bupa Arabia (Bupa) network levels, package names, and their published provider lists in Saudi Arabia, by city. Read this only when the user's company is Bupa, and only to name a provider that appears in the city tables, always stating the level it was published under.
---

# Bupa Arabia — levels, packages, and published network

## Status

**Loaded.** Two published Bupa Arabia network spreadsheets were converted on 10 November
2026 and are in this skill: Bupa Parents (levels `NW7+`, `NW6`, `NW5`) and Bupa Helpers
(levels `NWS`, `NWM`). 1,181 unique provider records across 100 cities.

Not loaded: Bupa Corporate, Bupa Munshaat, Bupa Family, Aramco Family, and any
employer-customised network. No network file for those is published on Bupa's public pages.

---

## The rule this skill exists to protect

A hospital may accept **Bupa** and still not accept the user's level or package. This skill
never answers at company level. Any provider it names must be qualified by the level(s) it
was published under, and by the source file.

If a provider is not in `network/<city>.md`, or the file does not list the user's level,
the answer is **"I cannot confirm this"** — followed by the provider's phone number and the
exact question: *"Do you bill Bupa [level/class] directly?"*

---

## Bupa's level model — read this before answering

Bupa publishes one spreadsheet **per network level**, and each sheet is titled with the
level code plus a commercial package name. That is the only tier vocabulary in the
network files.

| Level | Package name | Product |
|---|---|---|
| `NW7+` | Saudi Parent — VIP (Black) | Bupa Parents |
| `NW6` | Saudi Parent — Gold | Bupa Parents |
| `NW5` | Saudi Parent — Silver | Bupa Parents |
| `NWS` | Classic (Blue) | Bupa Helpers |
| `NWM` | Basic (Blue) | Bupa Helpers |

The letters `NWS` / `NWM` / `NWR` also appear **inside** every sheet, as each provider's own
tier attribute — a provider on the VIP sheet can be labelled `NWS` without being a Helpers
provider. **Presence in a plan is decided by which sheet lists the provider, not by the row
label.** The city tables already resolve this: the "Tiers accepted" column is the set of
plan levels whose sheet contained the provider.

Levels nest upward (NW5 ⊂ NW6 ⊂ NW7+, and NWM ⊂ NWS in the two Helpers sheets). **Never use
that nesting to infer that an unlisted provider is covered** — a provider is only in this
skill because a file listed it.

---

## Card → skill lookup

1. Confirm the company is Bupa. If not, do not use this skill.
2. Establish the level. Ask for the level code (`NW7+`, `NW6`, `NW5`, `NWS`, `NWM`) or the
   package name (Saudi Parent Gold, Helpers Classic, …). Cards often print neither — the
   policy schedule or an employer HR letter carries it.
3. **If the user only knows "Class A" or "Class B": stop.** Bupa publishes no mapping from
   its level codes to Class A / Class B. Say you cannot place them at a level, do not guess,
   and give the hospital's number with the exact question. This is the single most likely
   real-world case and the honest answer is "cannot confirm".
4. Confirm the **city** in the same words as a city file. If the city has no file, say so.
5. Look up the provider in `network/<city>.md`. Quote the level set and the source file.
6. If the user's level is not in the provider's level set, say plainly that the provider is
   listed at other levels but not theirs, and give the phone number and the question.

---


### The answer block — use this shape every time

1. **What they hold:** Bupa medical policy — Parents, Helpers, or a corporate plan.
2. **Class:** the Bupa **level** — NW7+, NW6, NW5, NWS or NWM. Cards printing Class A/B cannot be
   mapped to a level; say so.
3. **What to do next:** if they know their level and city, look the provider up in `network/<city>.md`
   and name it with the levels it appears under. Otherwise call Bupa.
4. **Always ask the hospital:** *"Do you bill Bupa [level] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Level model, lookup procedure, refusal rules. |
| `tiers-and-packages.md` | The level table, nesting evidence, the Class A/B naming trap, coverage gaps. |
| `network/<city>.md` | One file per city. Provider table with code, type, levels, telephone, source. |
| `sources/index.md` | The two source files, their direct URLs, structure recovered, and every known conversion loss. |

City files, largest first: `riyadh` (335), `jeddah` (194), `dammam` (64), `al-khubar` (45),
`makkah` (43), `madinah` (41), `jubail` (31), `al-hasa` (32), `buraydah` (24), `taif` (23),
`khamis-mushait` (22), `najran` (20), `qatif`, `yanbu`, `abha`, `tabuk`, `hail`,
and 82 more.

---

## Answer shape

> **[Provider name]** — listed in Bupa's published **[level name] ([level code])** network
> for **[city]**. Source: Bupa Arabia `[file]`, published network, taken 10 Nov 2026.
> Bupa did not publish your level for this provider, so call **[phone]** and ask
> *"Do you bill Bupa [level] directly?"* before you go.

Coverage and networks change; Bupa can alter a network at contract level. Say so.

---

## Change log

- 2026-11-10 — skill created; structure and rules only.
- 2026-11-10 — two Bupa Arabia network spreadsheets downloaded and converted. 1,181 provider
  records, 100 city files, `tiers-and-packages.md` and `sources/index.md` populated.
  271 of 4,385 source rows could not be split into columns and are **not** in the tables —
  see `sources/index.md`, loss 3.
