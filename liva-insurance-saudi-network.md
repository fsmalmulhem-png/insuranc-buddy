---
name: liva-insurance-saudi-network
description: Liva Insurance (ليفا للتأمين / livainsurance.sa, formerly Al Alamiya) — a motor/home/travel insurer; it does NOT sell domestic health insurance, only a visitor-visa medical network whose accreditations have all expired. Read when the user's company is Liva / Al Alamiya, to establish what they actually hold and redirect.
---

# Liva Insurance — motor, home and travel, not health

## Status — two separate cautions

**1. Liva does not sell domestic health insurance.** Its product menu is **car, travel and home**
for individuals, plus business lines. Health is listed only as a **future ambition** in its own FAQ,
not a product on sale.

**2. The one medical network it publishes is visitor-only and fully expired.** Liva publishes a
*Visitor Visa Medical Service Providers Network* PDF — but it covers **visitors**, not residents,
and **all 244 provider accreditations in it had expired by August 2026**.

Verified 11 November 2026. See `sources/index.md`.

---

## Who they are

**Liva Insurance Company** — ليفا للتأمين. **Formerly Al Alamiya for Cooperative Insurance**
(العلامية), rebranded on **7 November 2023**. Saudi joint stock company established 2009, capital
SAR 400 million. Founding shareholders included **Royal & Sun Alliance Insurance (Middle East)**
(50.07%) and **Riyad Bank** (19.92%).

**A user may still say "Al Alamiya"** — it is the same company. The FAQ states existing products
continue unchanged, and documents are rebranded to Liva on renewal.

## The product range — no health

### Individual
Car · Travel · Home

### Business
Engineering · General Accident · Liability · Life · Marine Cargo · Motor Fleet · Property ·
Small & Medium Business · Workmen's Compensation

**Neither list contains a medical or health product.** A full sitemap enumeration confirms no
`medical-insurance` or `health-insurance` page exists — both URL guesses return **404**.

### The health reference, in Liva's own FAQ

> "We will continuously work on exploring new and innovative ways to expand our products and service
> offerings to include a full suite of life, **health**, personal, and commercial insurance products"

That is a **statement of intent**, not a product. Liva is telling customers it plans to add health.
As of the check, it has not.

**This is different from Chubb and Wataniya** — those are established P&C insurers with no health
line either. Liva is a smaller insurer that has publicly named health as a future direction. The
agent must not read that sentence as "Liva offers health."

## The visitor-visa medical network — real, but expired and visitor-only

Liva does publish one provider network:

| Property | Value |
|---|---|
| Document | `Visitor Visa_Medical Service Providers Network_1.PDF` |
| Pages | 15 |
| Dated | **9 January 2025** |
| Providers | **244** across **45 cities** |
| Network types | `Direct` (192) · `Emergency and referral` (52) |
| Cities | Riyadh 54 · Jeddah 36 · Makkah 15 · Dammam 14 · Jubail 8 · Buraydah 7 · Qatif 7 · Abha 7 … |

### Two reasons it cannot be used as a health network

**It is visitor-only.** The document is the network for **visitor visa** medical cover — the
mandatory short-term insurance a visitor needs to enter Saudi Arabia. It is not the network for a
resident's health policy, because Liva does not sell those.

**Every accreditation has expired.** Parsing the file's own `ExpiryDate` column:

| | Count |
|---|---|
| Providers listed | 244 |
| Valid on 11 Nov 2026 | **0** |
| Latest expiry in the file | **11 August 2026** |
| Earliest | 13 January 2025 |

So even for a visitor, this list is out of date. It is preserved in this skill as evidence of what
Liva published — not as a live network.

---

## What the agent must do when someone says "Liva" or "Al Alamiya"

1. **Confirm the company** — Liva, or its former name **Al Alamiya**. Same insurer.
2. **Establish what product they actually hold.** Ask them to read the policy type off their
   document. If they say "health", that is unlikely to be correct.
3. **If they hold car, travel or home** — that is what Liva sells. Answer accordingly, and note this
   skill covers health questions only.
4. **If they believe they hold Liva health insurance:**
   - say plainly that **Liva does not currently sell domestic health insurance** — its own FAQ lists
     health only as a planned addition;
   - suggest they check the policy document for the actual insurer, since a health policy is very
     unlikely to be Liva;
   - if they are a **visitor** holding visitor-visa medical cover, explain that the published
     provider network is from January 2025 and every accreditation in it has expired, so they must
     confirm with Liva before relying on it.
5. **Do not name a hospital.** Even for the visitor network, naming one from an expired list would
   mislead.
6. Contacts: **8002444481** (call centre, WhatsApp on the same number). For travel emergencies,
   Liva's assistance centre is **+971 4 601 8777**, 24/7.

### The answer block — use this shape every time

1. **What they hold:** Liva (or Al Alamiya) policy, product unknown — likely car, travel or home.
2. **Class:** not applicable — Liva sells no domestic health, so there is no Liva health class.
3. **What to do next:** read the policy type off the document. If they hold visitor-visa medical
   cover, note the published network is from January 2025 and fully expired. For resident health
   cover they need a different insurer.
4. **Always ask the hospital:** *"Do you bill Liva Class [A/B] directly?"* — and if the card names
   another insurer, ask it with that name instead.


---

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | Status, the rebrand, product range, the expired visitor network, procedure. |
| `tiers-and-packages.md` | Products, sitemap evidence, the health-as-intent quote. |
| `network/README.md` | The visitor network in detail, why it is unusable, what was parsed. |
| `sources/index.md` | Every URL and result. |

---

## Change log

- 2026-11-11 — skill created. Confirmed no domestic health product; visitor-visa network parsed
  (244 providers, 45 cities) and found fully expired. Skill redirects rather than answering.

