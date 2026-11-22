# ACIG — plans, classes, and what is publicly known

Populated from ACIG's own site (`acig.com.sa`) and its application bundles, read 11 November
2026.

## Who ACIG is

**المجموعة المتحدة للتأمين التعاوني (أسيج)** — United Cooperative Assurance. Its own meta
description lists: motor, **health (تأمين صحي)**, travel, domestic labour and more.

## The health products

| Evidence | Detail |
|---|---|
| Site routes | `cancel-medical-insurance` exists as a public route |
| App bundle | A `MedicalInsurance` component exists |
| Online products | `medicalOnlineProductIds = [82, 83]` — **two medical products** purchasable online |
| Product page routes | `individuals-insurance`, `company-insurance`, `business`, `all-products` |

So ACIG sells medical insurance both to individuals (through online purchase) and to
companies. This is a broader health footprint than Arabian Shield, which offers SME cover only.

**What ACIG does not publish:** any benefits table, any tier or class list, any provider list.

## Classes — nothing published

| Aspect | Published by ACIG? |
|---|---|
| Number of classes | **No** |
| Class names | **No** |
| Class A / Class B mapping | **No** |
| Benefits per class | **No** |
| Class → provider mapping | **No** |
| Provider list | **No** — only inside the member portal |
| Public instruction on how to check | **No** |

### The "أسيج" naming point

ACIG's Arabic name and brand is **أسيج**. A user may say either "ACIG", "أسيج" or "United
Cooperative Assurance" — all the same company. The agent should recognise all three.

## Bear in mind: two medical product IDs

`medicalOnlineProductIds = [82, 83]` means the online purchase flow offers two distinct
medical products. That is evidence of a tier structure of some kind, but **not** a published
one — the IDs are internal codes, and the bundle does not expose their names or coverage. Do
not present "two products" as "two classes"; it is a hint, not a mapping.
