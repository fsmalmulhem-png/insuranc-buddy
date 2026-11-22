---
name: aicc-arabia-insurance-saudi-network
description: Arabia Insurance Cooperative Company / شركة التأمين العربية التعاونية (AICC / aicc.com.sa) — the ONLY company in this set publishing per-provider, per-class coverage status (Direct Access / Emergency / NOT COVERED) across Arabia VIP, A, B and C networks. Read when the user's company is Arabia Insurance / AICC, to state what their class allows.
---

# Arabia Insurance (AICC) — per-provider, per-class coverage

## Status

**Every other company in this set says which network a hospital is in. AICC says what happens
at each class, provider by provider.**

That is the strongest class-level publication found in this project, and it is current — the
main documents are dated **8 November 2026**.

Verified 11 November 2026. See `sources/index.md`.

---

## A different company from Arabian Shield

**Do not confuse these two.** `arabiainsurance.com` (the URL supplied) is **Arabia Insurance
Company**, the regional group. The Saudi licensed entity is **Arabia Insurance Cooperative
Company (AICC / شركة التأمين العربية التعاونية)** at **`aicc.com.sa`**. Arabian Shield
(الدرع العربي, der3.com) is a separate insurer with its own skill.

`arabiainsurance.com` is a corporate group site with no products and no network — its only use
here is pointing to AICC.

---

## The published network documents — four of them

| Network | Classes | Pages | Dated |
|---|---|---|---|
| **Corporate** | Arabia **VIP · A · B · C 0222** | 54 | 08-11-2026 |
| **Unique Iqama** | Arabia **VIP · A · C 0222** | 57 | 08-11-2026 |
| **Elite SME — business** | SME **VIP · A · B · C+ · C5+** | 43 | 08-11-2026 |
| **Elite SME — C0666** | Arabia SME C (0666) | 10 | 07-04-2026 |

All four are linked from `aicc.com.sa/products` under **"شبكات الرعاية الطبية"** (medical care
networks).

## The three status values — this is the finding

Each provider row carries one status **per class**:

| Status | Meaning |
|---|---|
| **`Direct Access`** | Member may attend without prior approval |
| **`Emergency & Ref`** | Emergency and referral only |
| **`NOT COVERED`** | Not available at that class |

### Corporate network — 2,524 providers, 4 classes

| VIP | A | B | C 0222 | Providers |
|---|---|---|---|---|
| Direct Access | Direct Access | **NOT COVERED** | NOT COVERED | **1,119** |
| Direct Access | Direct Access | Direct Access | Direct Access | 990 |
| Direct Access | Direct Access | Direct Access | **NOT COVERED** | 190 |
| Direct Access | **NOT COVERED** | NOT COVERED | NOT COVERED | 98 |
| Direct Access | Direct Access | **NOT COVERED** | Emergency & Ref | 82 |
| Direct Access | Direct Access | Direct Access | Emergency & Ref | 45 |

**1,119 of 2,524 corporate providers are open to VIP and A, and closed to B and C.** That is
44% of the corporate network unavailable at Class B — a fact a member cannot discover anywhere
else, from any other insurer.

### Unique Iqama network — 2,550 providers, 3 classes

| VIP | A | C 0222 | Providers |
|---|---|---|---|
| Direct Access | Direct Access | **NOT COVERED** | 1,309 |
| Direct Access | Direct Access | Direct Access | 990 |
| Direct Access | Direct Access | Emergency & Ref | 153 |
| Direct Access | **NOT COVERED** | NOT COVERED | 98 |

### Elite SME business — 935 providers, 5 classes

| VIP | A | B | C+ | C5+ | Providers |
|---|---|---|---|---|---|
| Access | Access | Access | **NOT COVERED** | NOT COVERED | 431 |
| Access | Access | Access | Access | Access | 268 |
| Access | Access | Access | Emergency & Ref | NOT COVERED | 151 |
| Access | Access | Access | Access | NOT COVERED | 85 |

## What this skill cannot do — stated plainly

**It cannot name a hospital.** Provider names in all four PDFs are **Arabic-only**, embedded in
a right-to-left run mixed with address, district and column headers. Extraction produced
partially correct and address-contaminated strings. Publishing those would put wrong hospital
names in front of a user, which is worse than naming none.

So this skill carries **the class structure and coverage statistics** — which is the more
valuable half — and refuses at the provider-name level.

## What the agent must do for an Arabia Insurance / AICC user

1. Confirm the company is Arabia Insurance / AICC (Arabic: شركة التأمين العربية التعاونية), **not**
   Arabian Shield. If it is Arabian Shield, use that skill instead.
2. Ask the class on their card: **VIP, A, B or C** (and whether it is Corporate, Unique Iqama, or
   SME — the four documents differ).
3. **Explain what their class means from the tables above** — this is the skill's real value. For
   example: *"In AICC's corporate network, Class B is excluded from the largest single block —
   1,119 of 2,524 providers are Direct Access on VIP and A but not covered on B or C."*
4. **Do not name a hospital** — see above.
5. Direct them to the published network PDF and the contact lines:
   - **Medical approvals and claims: 920002013** (WhatsApp available on the same number)
   - **8001288888** — main line
   - **920005002** — additional line found on the contact page
   - Open `aicc.com.sa/products` → **شبكات الرعاية الطبية** for the four PDFs
6. Still give the hospital question: *"Do you bill Arabia Insurance Class [X] directly?"*

---


### The answer block — use this shape every time

1. **What they hold:** Arabia Insurance / AICC policy. Establish which of the four networks applies
   — Corporate, Unique Iqama, or one of the two SME sets.
2. **Class:** VIP, A, B or C 0222 (Corporate); SME VIP/A/B/C+/C5+ for SME.
3. **What to say about the class:** this is the one company where per-provider, per-class status is
   published. Quote the pattern from `tiers-and-packages.md` — for the corporate network, 1,119 of
   2,524 providers are open on VIP and A but **not covered on B or C**.
4. **Always ask the hospital:** *"Do you bill Arabia Insurance Class [X] directly?"*

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the three status values, the coverage tables, procedure. |
| `tiers-and-packages.md` | All four networks, full statistics. |
| `network/README.md` | The four PDFs, the Arabic-name limitation, what was parsed. |
| `sources/index.md` | Every URL, including the arabiainsurance.com → aicc.com.sa redirect trail. |

---

## Change log

- 2026-11-11 — skill created. Four network PDFs found (three at 08-11-2026), parsed for class
  status across 6,000+ rows. Provider names not published due to Arabic-extraction quality.
