# Amana — how the city files were built

## Source of every row

Both files are Amana's own, published on `amana.sa` and dated **21 May 2026**:

1. `Amana-Full-Network-21-05-2026-Existing-Policies.pdf` — 49 pages
2. `Amana-SME-Network-Basic-21-05-2026.pdf` — 43 pages

## Conversion method

Both PDFs render as text (not scans), so each provider occupies one long row:

```
Region  City  TYPE  NPCODE  Provider name  Owner  Classification  [ticks]  …  Phone  District  [Arabic]  Registry
```

Columns were split on runs of two or more spaces, which is how the source separates fields.
`NPCODE` prefixes indicate type: `H` hospital, `C` clinic, `O` optical, `P` pharmacy, `D` dental.

**Yield:** 1,805 rows from the Full file, 1,850 from the SME file; after de-duplicating on
**provider code + city**, **1,851 unique providers across 159 cities**.

A provider appearing in both files is shown once, with both lists named.

## Known conversion losses — read before trusting a row

1. **Sub-tier (Advance / Elite / Standard) is not captured.** The PDFs mark membership with a row
   of tick marks across 14 network columns, but the extracted rows contain **13–21** such symbols
   depending on page. A positional mapping would be invention, so it is not attempted. The
   **Network list** column therefore names which *PDF* the row came from — not which sub-tier.
   Do not describe it as a class column.

2. **District and Arabic fields are not separate columns.** They are mixed into the row text with
   inconsistent delimiters. Provider name + city + code is the reliable key.

3. **Telephone** is captured where it matches an Saudi landline pattern (`0XX-XXXXXXX`). Rows
   without one show `—`. Some MOH rows genuinely publish no number.

4. **City spelling is Amana's.** The PDFs use inconsistent casing and spelling
   (`BURAIDAH`, `Ihsaa`, `Madina`, `Khobar`, `KHAMIS MUSHAIT`). These are normalised to the
   common English form so one city is one file; the original string is not retained per row.

5. **Rows that failed the column split are absent.** A row whose fields were not separated by
   two spaces could not be parsed and is not in the tables. Treat absence as "unknown", not as
   "not in network".

## What to say, and not say

**Say:** "[Provider] is listed in Amana's published network for [city], in the [Full / SME Basic]
list, published 21 May 2026."

**Do not say:** "this provider is on the Amana Elite network" — unless the member's own policy
says so. The skill cannot establish it.

**Do say, where the PDF does:** MOH facilities carrying *"All Classes as Direct Access / As per
circular 11"* are accessible at any class by regulation.
