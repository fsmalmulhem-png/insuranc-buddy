# Bupa — tiers, packages, and what each covers

Populated from the two Bupa Arabia network spreadsheets listed in `sources/index.md`.
Every row here is traceable to a sheet in one of those files.

## What the source files actually publish

Bupa Arabia publishes its individual/family network as a spreadsheet **per level**, where
each sheet is named with the level plus its commercial package name. That is the only
tier vocabulary Bupa puts in the network files. It is **not** the Class A / Class B wording
that most member cards print.

| Level code | Package name as published | Product | Sheet name in source file | File | Providers in sheet |
|---|---|---|---|---|---|
| `NW7+` | Saudi Parent — VIP (Black) | Bupa Parents | `NW7+ - Saudi Parent -VIP(Black)` | `saudi-parent-network.xlsx` | 1,294 rows |
| `NW6` | Saudi Parent — Gold | Bupa Parents | `NW6 - Saudi Parent - Gold` | `saudi-parent-network.xlsx` | 1,168 rows |
| `NW5` | Saudi Parent — Silver | Bupa Parents | `NW5 - Saudi Parent Silver` | `saudi-parent-network.xlsx` | 1,080 rows |
| `NWS` | Classic (Blue) | Bupa Helpers | `NWS - Classic ( Blue)` | `Household-help-network.xlsx` | 571 rows |
| `NWM` | Basic (Blue) | Bupa Helpers | `NWM - Basic (Blue)` | `Household-help-network.xlsx` | 272 rows |

Two families of level codes appear: `NW1`–`NW7` numeric levels, and the letter levels
`NWS` / `NWM` / `NWR` which appear *inside* every sheet as a per-provider attribute (see
"How levels work" below). `NWM` and `NWS` are also the level names of the two Bupa Helpers
sheets, which is a genuine ambiguity in Bupa's own naming — recorded, not resolved.

## How levels work — important

The numeric level code in the **sheet name** is the plan level the sheet is published for.
The level code in each **provider row** is that provider's own network tier inside that
plan. A provider on the VIP sheet can carry `NWS` (its own tier), which does not mean it is
a Helpers provider.

So a provider's presence in a plan is decided by **which sheet it appears on**, and the row
label is a separate attribute. Both are kept in the city tables: "Tiers accepted" is the
set of plan levels whose sheet listed the provider.

Distribution across the 1,181 unique provider records (provider code + city) after conversion:

| Plan levels the provider appears under | Providers |
|---|---|
| NW7+, NW6, NW5 | 456 |
| NW7+, NW6, NW5, NWS | 289 |
| NW7+, NW6, NW5, NWS, NWM | 268 |
| NW7+, NW6 | 82 |
| NW7+ only | 82 |
| NWS only | 4 |

The parent levels nest: everything on NW5 also appears on NW6 and NW7+. The two Helpers
levels do not nest the same way — `NWS` (Classic) is the higher of the two and its 571 rows
are a superset of the 272 `NWM` rows, while 268 providers carry all five labels because
Bupa Parents and Bupa Helpers overlap heavily. That nesting is a property of these two files
as published; it is not a guarantee about Bupa's network in general, and it must not be used
to infer an unlisted provider is covered.

## Naming traps — the gap this skill exists to surface

| Bupa label | Market label on cards | Stated in source? | Source file |
|---|---|---|---|
| `NW7+` Saudi Parent VIP (Black) | Class A or Class B — **not stated** | No | `saudi-parent-network.xlsx` |
| `NW6` Saudi Parent Gold | Class A or Class B — **not stated** | No | `saudi-parent-network.xlsx` |
| `NW5` Saudi Parent Silver | Class A or Class B — **not stated** | No | `saudi-parent-network.xlsx` |
| `NWS` Classic (Blue) | Class A or Class B — **not stated** | No | `Household-help-network.xlsx` |
| `NWM` Basic (Blue) | Class A or Class B — **not stated** | No | `Household-help-network.xlsx` |

**This is the finding, not a failure of the conversion.** Bupa's published network never
maps its level codes to the Class A / Class B printed on member cards. The two files give a
complete provider list per Bupa level, and no bridge to the wording the member actually
holds. So:

- If the user can name their Bupa level or package → use the city tables, answer at that level.
- If the user only knows "Class A" or "Class B" → the skill **cannot** place them in a level.
  It must say so, and give the hospital's number with the exact question.
- A card does not carry a package name either; the policy schedule or an employer HR letter does.

## Levels not covered by these files

These files cover the **individual / family** products only (Bupa Parents, Bupa Helpers).
They do **not** cover:

- **Bupa Corporate** — employer group plans, which is where most Class A / Class B cards come from.
- **Bupa Munshaat** — SME plans, ≤ 200 employees.
- **Bupa Family** — the direct-to-consumer family product; no network file was published on the product page.
- **Aramco Family**.
- Any employer-customised network, which Bupa can modify per contract.

For those, this skill must say it cannot confirm, and cannot name a hospital.
