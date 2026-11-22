# Arabia Insurance (AICC) — numbered networks, class by class

Populated from Arabia Insurance Cooperative Company's own published network PDFs, read
11 November 2026. All three are linked from the Arabic homepage.

## The published network documents

| Document | Linked as | Pages | Date in filename |
|---|---|---|---|
| **Corporate network** | شبكة الشركات | 54 | 08-11-2026 |
| **Unique Iqama network** | شبكة الإقامة المميزة | 57 | 08-11-2026 |
| **Elite SME — business** | شبكة المنشآت الصغيرة والمتوسطة | 43 | 08-11-2026 |
| **Elite SME — C0666** | شبكة النخبة للمنشآت الصغيرة والمتوسطة | 10 | 07-04-2026 |

Three are **dated 8 November 2026** — the most current network files found anywhere in this
project.

### Corporate network — 4 classes, 2,524 providers

| Class columns | Arabia **VIP · A · B · C 0222** |
|---|---|

| VIP | A | B | C 0222 | Providers |
|---|---|---|---|---|
| Direct Access | Direct Access | **NOT COVERED** | NOT COVERED | **1,119** |
| Direct Access | Direct Access | Direct Access | Direct Access | 990 |
| Direct Access | Direct Access | Direct Access | **NOT COVERED** | 190 |
| Direct Access | **NOT COVERED** | NOT COVERED | NOT COVERED | 98 |
| Direct Access | Direct Access | **NOT COVERED** | Emergency & Ref | 82 |
| Direct Access | Direct Access | Direct Access | Emergency & Ref | 45 |

**1,119 of 2,524 — 44% — are open on VIP and A but NOT COVERED on B and C.** This is the single
most consequential published fact in the whole project for a Class B holder.

## The class structure — this is the key finding

These PDFs do not merely list providers; they state, **per provider and per class**, whether the
provider is accessible. Three status values are used:

- **`Direct Access`** — the member may go without prior approval
- **`Emergency & Ref`** — emergency and referral only
- **`NOT COVERED`** — not available at that class

### Unique Iqama network — 3 classes

| Class columns | Providers |
|---|---|
| **Arabia VIP · Arabia A · Arabia C 0222** | 2,550 rows |

Observed coverage patterns (from 2,550 parsed rows):

| VIP | A | C 0222 | Providers |
|---|---|---|---|
| Direct Access | Direct Access | **NOT COVERED** | 1,309 |
| Direct Access | Direct Access | Direct Access | 990 |
| Direct Access | Direct Access | Emergency & Ref | 153 |
| Direct Access | **NOT COVERED** | NOT COVERED | 98 |

### Elite SME — business network — 5 classes

| Class columns | Providers |
|---|---|
| **SME VIP · SME A · SME B · SME C+ · SME C5+** | 935 rows |

| VIP | A | B | C+ | C5+ | Providers |
|---|---|---|---|---|---|
| Direct Access | Direct Access | Direct Access | **NOT COVERED** | NOT COVERED | 431 |
| Direct Access | Direct Access | Direct Access | Direct Access | Direct Access | 268 |
| Direct Access | Direct Access | Direct Access | Emergency & Ref | NOT COVERED | 151 |
| Direct Access | Direct Access | Direct Access | Direct Access | NOT COVERED | 85 |

### Elite SME — C0666 network — 1 class

336 rows, marked `√` (covered) or `Emergency & Referral`.

## Why this matters more than a provider list

Every other company in this set tells you *which network* a provider is in. AICC tells you **what
happens at each class, provider by provider** — including the common case where a hospital is
fully available on VIP and A, and **explicitly `NOT COVERED` on C 0222**.

That is the project's thesis, demonstrated in the insurer's own data: 1,309 of 2,550 providers in
the Iqama network are reachable at VIP and A but **not at Class C**.

## What could NOT be extracted reliably

**Provider names are Arabic-only** in all three PDFs, embedded in a right-to-left text run mixed
with the address, district and Arabic column headers. Extraction produced partial and
address-contaminated strings (e.g. `مجمع الهشبول` was correct, but others carried street names).

Rather than publish a table with wrong hospital names, this skill publishes **the class structure
and coverage statistics only**, and states plainly that it cannot name a provider. That is the
honest boundary; a wrong Arabic name is worse than none because it looks authoritative.

## Contacts

Published on the homepage. See `sources/index.md` for what was verified.

## Where AICC sits

| Company | Provider files | Class-level status per provider |
|---|---|---|
| **Bupa** | 100 cities, 1,181 | No |
| **Amana** | 159 cities, 1,851 | Class + sub-tier structure, no per-provider status |
| **Saudi Enaya** | 0 | Class → network code only |
| **Arabia Insurance (AICC)** | 3 PDFs | **YES — Direct Access / Emergency / NOT COVERED per class** |
| Other nine | 0 | No |

AICC is the only company in the set that publishes **per-provider, per-class coverage status**.
