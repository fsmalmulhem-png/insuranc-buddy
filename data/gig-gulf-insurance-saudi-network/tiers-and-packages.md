# GIG — networks, tiers, and benefit structure

Populated from Gulf Insurance Group's own site (`gig.sa`), read 11 November 2026.

## Who they are

**Gulf Insurance Group** — مجموعة الخليج للتأمين. Not to be confused with **GGCI** (Gulf General
Cooperative Insurance, `ggi-sa.com`, الخليجية العامة), which is a different insurer also in this
set.

## Products

| Product | Route |
|---|---|
| **Group healthcare** (employees) | `/business/employee/group-healthcare-insurance/` |
| Healthcare quote | `/healthcare-quote/` |
| **Provider locator** | `/provider-locator/` |
| Individual: Motor · Travel · Home · Motorcycle | under `/ar/الأفراد/…` |

Health is sold as **group healthcare for employees** — employer-facing.

## The network tiers

GIG's locator tags every provider with a network code. Distribution across the 3,437 providers:

| Network | Providers | Share |
|---|---|---|
| **E** | 2,648 | **77.0%** |
| **VIP** | 339 | 9.9% |
| **C** | 144 | 4.2% |
| **B** | 121 | 3.5% |
| **D** | 97 | 2.8% |
| **A** | 60 | 1.7% |
| **A+** | 21 | 0.6% |
| **B+** | 6 | 0.2% |
| **VVIP** | 1 | 0.03% |

### Why this distribution matters

**77% of the entire published network is tier E.** Only 339 providers are on VIP across the whole
Kingdom, and exactly **one** is on VVIP.

For a member, this is the single most consequential fact in the file: the difference between an E
policy and a VIP policy is not a nuance, it is the difference between a network of 2,648 and a
network of 339. Any advisor answering "is my hospital covered" must know which side of that line
the member is on.

### Provider types across the network

| Type | Count |
|---|---|
| Pharmacy | 2,073 |
| Medical Centre | 584 |
| **Hospital** | **404** |
| Optical Provider | 322 |
| Dental Provider | 52 |
| Physiotherapy Center | 1 |
| Diagnostic Center | 1 |

**Note for anyone quoting a number:** the 3,437 total is dominated by pharmacies (60%). If a user
asks "how many hospitals does GIG have?", the answer from this data is **404**, not 3,437. The city
files show type per row so this distinction is always visible.

### Hospital tiers specifically

Among the 404 hospitals:

| Network | Hospitals |
|---|---|
| VIP | 213 |
| E | 52 |
| C | 45 |
| D | 41 |
| A | 18 |
| A+ | 18 |
| B | 12 |
| B+ | 5 |

So hospitals skew toward VIP much more than pharmacies do — a member on E has 52 hospitals
nationally, while a VIP member has 213.

## The published benefit tables

GIG publishes named networks with full benefits. Sample rows from the group-healthcare page:

| Network | Area of cover | Room & Board | Maternity | Deductible | Generic coinsurance |
|---|---|---|---|---|---|
| **VVIP 1** | Regional | Suite | 20,000 SAR | Nil | Nil |
| **VVIP 3** | KSA only | Suite | 20,000 SAR | 10% max 50 SAR | 20% max 30 SAR |
| **VIP 1** | KSA only | Suite | 15,000 SAR | 20% max 50 SAR | 20% max 30 SAR |
| **VIP 2** | Regional | Suite | 20,000 SAR | Nil | Nil |
| **VIP 3** | KSA only | Suite | 20,000 SAR | 10% max 50 SAR | 20% max 30 SAR |
| **VIP 4** | KSA only | Suite | 15,000 SAR | 20% max 50 SAR | 20% max 30 SAR |
| **VIP 5** | Regional | Suite | 15,000 SAR | 10% max 50 SAR | 20% max 30 SAR |
| **VVIP2** | KSA only | Suite | 15,000 SAR | 10% max 50 SAR | 20% max 30 SAR |

Each row is also qualified by **innovative-drug coinsurance** (typically 50% with no cap), dental
corrective limits (1,200–2,400 SAR), RCT/emergency dental (800–1,600 SAR), optical care (400–1,200
SAR) and IEMA.

### The suffix discrepancy — handle carefully

The benefit table uses **numbered** networks (`VVIP 1`, `VIP 3`), while the provider locator tags
providers with the **base** tier (`VIP`).

The skill therefore treats a locator tag of `VIP` as **"the VIP family"** and does not assume which
numbered variant a member holds. A member's schedule names the exact variant; the locator names the
family. Do not silently conflate them.

## Classes vs tiers

| Card wording | GIG wording |
|---|---|
| Class A / Class B | VVIP · A+ · A · B+ · B · C · D · E |

GIG does not use "Class A / Class B". A member whose card says that must check their policy schedule
for the GIG network name. The skill must not guess a mapping.
