# Walaa — provider data at a glance

## How many providers

**1,657 provider rows across 138 cities in 13 regions**, from `Walla_Updated_network.xlsx`
(Walaa GMS standard Full Network, header date 07-08-2025).

## Where the network data lives

`classes/` — one Markdown file per city, each row listing the GMS tiers that provider
accepts (VIP, A, B, C, C+, C+ PC).

## Can this skill name a hospital?

**Yes**, for the 138 cities in `classes/`, at the tier named in the row.

## What changed

This folder previously recorded "Walaa publishes no medical provider list in any format" —
that was true as of the 11 November 2026 website survey (`network/README.md`). The GMS
network spreadsheet states otherwise for the GMS product, with class-level detail. Both
statements are kept: the website still has no public lookup, but the network list exists
and is held here.
