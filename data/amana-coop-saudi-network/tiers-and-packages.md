# Amana — classes, sub-tiers, and benefits

Populated from Amana's own network PDFs (`amana.sa/assets/documents/`), published 21 May 2026.

## The two published lists

| List | File | Pages | Covers |
|---|---|---|---|
| **Full** (existing policies) | `Amana-Full-Network-21-05-2026-Existing-Policies.pdf` | 49 | Policies with this network update in force |
| **SME Basic** | `Amana-SME-Network-Basic-21-05-2026.pdf` | 43 | The Amana Basic Program SME |

The Full PDF states: *"Policies classified as Existing Policies (effective before 14-04-2026)"*.
So these two lists are **versioned by policy date**, not one universal list — a detail worth
keeping, because a 2026 policy may sit on a different network than these.

## Full network — class × sub-tier matrix

| Class | Sub-tiers |
|---|---|
| VIP | Advance · Elite · Standard |
| A | Advance · Elite · Standard |
| B | Advance · Elite · Standard |
| C0222 | Advance · Elite · Standard |
| C | CVT · 0333 · 0444 |

Fourteen network columns in total:
`VIP Advance, VIP Elite, VIP Standard, A Advance, A Elite, A Standard, B Advance, B Elite,
B Standard, C0222 Advance, C0222 Elite, C0222 Standard, C-CVT, C0333, C0444`.

## SME network

| Network | Codename |
|---|---|
| SME VIP | — |
| SME A | — |
| SME B | — |
| SME X | 0444 |
| SME R | 0555 |

So an SME member is on one of five networks, and "SME A" / "SME B" again line up with the
card's A/B wording.

## Row columns in the source

`Region · City · TYPE · NPCODE · Provider name · Owner · Classification (MPN/OCN/OHN) ·
[network ticks] · MOH classification · Google X/Y · Expiry · Phone · District · Arabic fields · Registry no.`

- **Owner** is typically `Private` or `MOH`. MOH facilities are public hospitals, which matters:
  they may accept any class, and the PDF notes some as *"All Classes as Direct Access / As per
  circular 11"*.
- **Classification** is `MPN`, `OCN` or `OHN` — the same three co-payment categories Saudi Enaya
  publishes. Amana assigns one per provider row.
- **Expiry Date as CCHI** appears per provider, which is a useful freshness marker.

## What cannot be recovered

The sub-tier tick row. Each provider row contains between **13 and 21** tick/ dash symbols,
varying by page — not a consistent 14-column grid in the extracted text. Mapping ticks to the 14
named networks positionally would therefore be guessing, and the skill does not do it.

**Consequence:** the skill knows a provider is in Amana's published network(s), and which of the
two lists, but not which sub-tier. Reported honestly rather than filled in.

## MOH exemption note

Some MOH rows carry the text **"All Classes as Direct Access / As per circular 11"** — meaning
that facility is accessible at any class by regulation, not by Amana's choice. Where that text
appears, it is a genuine class-level fact and may be stated, citing the PDF.
