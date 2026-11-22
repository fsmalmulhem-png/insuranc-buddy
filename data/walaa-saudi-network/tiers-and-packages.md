# Walaa — plans, classes, and what is publicly known

Populated from Walaa's own site (`walaa.com`) and its application bundle, read 11 November 2026.

## Who they are

**شركة ولاء للتأمين التعاوني** — Walaa Cooperative Insurance. A Saudi listed insurer offering
motor, travel, home, medical, protection & savings, and business lines.

## Health products — from Walaa's own product map

The app bundle carries an explicit product-code → label mapping. Extracted verbatim:

| Code | Label |
|---|---|
| `medical` | **Medical** |
| `medical_sme` | **Medical SME** |
| `domestic` | **Domestic** (domestic workers, including health) |
| `visitor` | **Visitor Visa** |
| `travel` | Travel |
| `motor` | Motor |
| `home` | Home |
| `protection` | Protection & Savings |
| `motor_sme` | Motor SME |
| `retailshop` | Retail Shop Insurance |

A second map in the bundle labels the same set formally:
`MEDICAL:"Medical", TRVL:"Travel", DOMESTIC:"Domestic", VISITOR:"Visitor Visa", PROTECTION:"Protection & Savings", SME_MEDICAL:"Medical SME", SME_MOTOR:"Motor SME", RETAILSHOP:"Retail Shop Insurance"`.
Market segments: `SME:"SME"`, `corporate:"CORP"`.

So Walaa sells medical to **individuals, SMEs and corporates** — a broad footprint.

## Classes — nothing published

| Aspect | Published? |
|---|---|
| Number of classes | **No** |
| Class names | **No** |
| Class A / Class B mapping | **No** |
| Benefits per class | **No** |
| Class → provider mapping | **No** |
| Provider list | **No** |
| Public lookup | **No** |

## Where Walaa sits among the ten

| Company | Provider list | Public self-service lookup |
|---|---|---|
| Bupa | **Yes (1,181)** | App |
| Al Rajhi Takaful | No | **Yes — public locator** |
| Tawuniya | No | Yes — search box |
| Al Sagr | No | No (TCS route, named) |
| ACIG | No | No (member portal, login) |
| MedGulf | No | No |
| Malath | Dead 2018 PDF | No |
| Arabian Shield | No | No |
| **Walaa** | **No** | **No** |
| Al Etihad | No | No (placeholder site) |

Walaa is in the "nothing published" group — but unlike Al Etihad, its site works and its
products are documented. The gap is a publication choice, not an unbuilt site.

## A trap worth recording

Walaa has a **Branch Locator** and a **Document Library**. Neither is a medical network:

- The Branch Locator finds **Walaa's own offices**.
- The Document Library is a CMS-driven list of policy documents, with no network file in the app
  code.

This is the same pattern as Tawuniya, whose "network coverage" page defaulted to showing branch
offices. A locator page is not a provider list until it names hospitals.
