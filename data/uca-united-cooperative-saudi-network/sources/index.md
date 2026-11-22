# UCA — sources checked

All checks on **11 November 2026**.

## The site is unreachable

| # | URL | Result |
|---|---|---|
| 1 | `https://www.uca.com.sa/` — text proxy | **422** — `page.goto: Timeout` |
| 2 | `https://www.uca.com.sa/robots.txt` — text proxy | 422 |
| 3 | `https://www.uca.com.sa/` — direct | **Connection timeout (25s)** |
| 4 | `https://uca.com.sa/` — direct | Connection timeout (20s) |
| 5 | `http://uca.com.sa/` — direct | Connection timeout (20s) |
| 6 | DNS | Resolves: **5.149.133.230** (apex and www) |

So the domain is registered and pointed, but nothing is served. Recorded rather than worked
around.

## What the archive holds

| # | URL | Result | Used for |
|---|---|---|---|
| 7 | Wayback availability API | Closest capture **2025-02-14** | Confirming snapshots exist |
| 8 | Archived `/products/` | 200 — 155,437 bytes | **The Medical product description** |
| 9 | Archived `/company/` | 200 — 167,491 bytes | **Company profile, licensed lines** |
| 10 | Archived `/faqs/` | 404 — not captured | — |
| 11 | Wayback CDX, `uca.com.sa*`, 500 rows | Only `MedicalInsurance.js` + `medical.png` icons | **Proving no network file exists** |

## The two decisive quotations

**Licensed lines** (from `/company/`):

> "The services offered by the company covers all insurance lines that the company is licensed for
> by the Insurance Authority which includes Property, Casualty and Accident, Liability, **Medical**,
> Marine Cargo and Hull, Aviation, Engineering and Energy Insurances."

**The network statement** (from `/products/`):

> "This insurance provides cover for the costs of providing Healthcare to the insured persons to the
> extent and in **the network of medical services providers appointed by the Company**."

## Contact, from the archived header

**800 244 4442** — presented site-wide as "Call Us".

## Company facts

- Saudi joint stock company, established **May 2008**
- Underwriting since **January 2009**
- Paid capital **SAR 400 million**
- Head office **Riyadh**, branches across the Kingdom
- Inherited the portfolio of **UCA Insurance Company** (35+ years in the Saudi market)

## Method note — and its limits

This is the **second** skill in the set whose evidence comes from the archive rather than the live
site (the first was Malath). That has a specific consequence worth stating: **the content is UCA's
own publication, but its vintage is early 2025.** If UCA has since published a network file, this
skill would not see it.

The skill says so in its own body rather than burying it, so a future reader knows to re-check if
the site returns.

## The disambiguation is deliberate

UCA (الشركة المتحدة) and ACIG (المجموعة المتحدة / أسيج) are separate companies with similar Arabic
names. Both have skills in this set. `sources` for ACIG are in its own skill, not merged here.
