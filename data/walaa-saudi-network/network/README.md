# Walaa — network files

## Public lookup: none

Walaa publishes no public medical provider search, and its site carries no network page.
Surveyed 11 November 2026: `robots.txt` allows crawling but the declared sitemap does not
resolve to a real file; of 64 page modules in the app bundle, none is a medical network,
hospital or provider page; `/pages/Branch-Locator/` finds Walaa **offices**, not hospitals.

## But the GMS network list exists

`Walla_Updated_network.xlsx` (GLOBEMED SAUDI, "Walaa GMS standard Full Network") lists 1,657
providers with city and tier detail. It is a member/GMS document, not a public web page.
Per-city tables built from it are in `../classes/`.

## So the honest answer to "can you name a hospital?"

- For a GMS member: **yes**, from `../classes/`, at the tier in the row.
- For someone on a Walaa individual or non-GMS medical plan: **we cannot say** — the file
  covers the GMS network, and whether that matches another product is not established.
