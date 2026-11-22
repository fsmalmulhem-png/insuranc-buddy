# Saudi Enaya — classes, networks, and benefits

Populated from Saudi Enaya's own site (`saudienaya.com`), read 11 November 2026. The **SME**
(`/sme-plan`) and **Corporate** (`/corporate-plan`) pages carry **identical** class tables.

## The class table — the one thing no other insurer gave us

| Class | Network code | Room type | Max annual limit | Geographical coverage |
|---|---|---|---|---|
| **VIP** | `SE_VIP` | Suite | SAR 1,000,000 | World Wide 2 / World Wide 1 |
| **A-Gold** | `SE_A` | Private | SAR 1,000,000 | World Wide 2 |
| **B-Silver** | `SE_B` | Semi-Private | SAR 1,000,000 | KSA & Home Country |
| **C-Bronze** | `SE_C+` / `SE_C` / `SE_C LTD` / `SE_CR` | Shared | SAR 1,000,000 | KSA |

**This is the bridge.** A member holding a card that says "Class A" or "Class B" can be placed:
A = A-Gold on `SE_A`, B = B-Silver on `SE_B`. Until this company, the whole project could only
say that no insurer publishes a mapping.

### The caution still required

"Saudi Enaya's A-Gold is the A class" is a reasonable reading of a table that literally says
**Class: A-Gold**. But Saudi Enaya does not print the sentence *"Class A on your card = A-Gold"*.
If a user's card says only "A", the agent should present A-Gold as the class of that name and
let them confirm against the card. Do not overstate it as a certified mapping.

## Benefit options within each class

Each class has numbered **options**, and some have **Enhanced** / **Nil** variants. The option
changes co-payment, not the network — the network code stays fixed per class.

| Class | Options offered |
|---|---|
| VIP | Option 1, 1-Enhanced, 1-Nil, 2, 2-Enhanced, 2-Nil, 3, 3-Enhanced, 3-Nil |
| A-Gold | Option 1, 1-Enhanced, 2, 2-Enhanced |
| B-Silver | Option 1, 1-Enhanced, 2, 2-Enhanced |
| C-Bronze / C-Classic | C+, C, C LTD, CR |

**"Nil"** in the option name corresponds to **Nil** co-payment on out-of-network treatment —
i.e. the option where Minimum Provider Network, Outside Hospital Network and Outside Clinic
Network copays are all Nil. That is a genuine product distinction, not a formatting quirk.

## Benefit lines per class (as published)

Every class lists: Table of Benefits, Network, Room Type, Max Annual Limit, Geographical
Coverage, Dental Limit, Optical Limit, Maternity Limit, **Minimum Provider Network (MPN)**,
**Outside Hospital Network (OHN)**, **Outside Clinic Network (OCN)**, Generic Medication and
Branded Medication.

### Those three acronyms matter most

- **MPN — Minimum Provider Network**: the copay when using a provider at the minimum end of the
  network.
- **OHN — Outside Hospital Network**: the copay for hospital care outside the network.
- **OCN — Outside Clinic Network**: the same for clinics.

Published values across classes are typically **20% Max 75** (MPN), **20% Max 300 / 20% Max 100**
(OHN), **20% Max 100** (OCN), with **Nil** variants. Medication: **20% copayment capped at SAR 30**
for generic, **50% uncapped** for branded.

So the insurer publishes not only which network a class uses, but **what leaving that network
costs** — a level of disclosure no other company in the set approaches.

## Dental / optical / maternity limits by class

| Class | Dental | Optical | Maternity |
|---|---|---|---|
| VIP | 2,000 / 4,000 / 5,000 | 400 / 1,000 / 2,000 | 15,000 / 20,000 / 25,000 |
| A-Gold | 2,000 / 3,000 | 400 / 1,000 | 15,000 / 20,000 |
| B-Silver | 2,000 / 2,500 | 400 / 750 | 15,000 |
| C-Bronze | 2,000 | 400 | 15,000 |

Values shown are the published SAR limits per option; ranges reflect the options available.

## Products

| Product | Page | Notes |
|---|---|---|
| **SME Plans** | `/sme-plan` | Same class table as corporate |
| **Corporate Plans** | `/corporate-plan` | Same class table |
| **Visit visa** | `/visa-services` | Separate short-term product |
| Network provider | `/network-provider` | **Requires login** |

## What is still not public

The **names of the providers inside SE_A, SE_B** etc. The network-provider page is member-gated,
and the app fetches the list per member (see `network/README.md`). So: class-level yes,
hospital-level no.
