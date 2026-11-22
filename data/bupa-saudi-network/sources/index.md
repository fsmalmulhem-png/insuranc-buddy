# Bupa — source files

Files taken from Bupa Arabia's own website. Every provider row in `network/` traces to one
of these.

| # | Original file | Format | Covers | Taken from Bupa site on | Converted to | Losses / notes |
|---|---|---|---|---|---|---|
| 1 | `saudi-parent-network.xlsx` | Excel, 3 sheets | Bupa Parents, levels NW7+ / NW6 / NW5 | 2026-11-10 (site states file dated 20 Oct 2026) | `network/<city>.md` | See "Known conversion losses" below |
| 2 | `Household-help-network.xlsx` | Excel, 2 sheets | Bupa Helpers, levels NWS / NWM | 2026-11-10 | `network/<city>.md` | See "Known conversion losses" below |

Direct URLs:

- `https://buy.bupa.com.sa/docs/default-source/bupaproviders/saudi-parent-network.xlsx`
- `https://buy.bupa.com.sa/docs/default-source/bupaproviders/Household-help-network.xlsx`

Both links appear on Bupa Arabia's own product pages:

- Bupa Parents — `https://www.bupa.com.sa/en/personal/bupaparents`
- Bupa Helpers — `https://www.bupa.com.sa/en/personal/bupahelpers`

## Source structure recovered

Both files are spreadsheets with one sheet per network level. Each sheet carries a title
block (`Bupa Parents` / `Bupa Helpers`), then a two-line header, then one row per provider.

Columns, as published:

`Provider Code · Provider Name · NW Level · Practice Type · Province · City · Address · Telephone · [Arabic address] · [Arabic city] · [Arabic province] · [Arabic provider name] · District · [Arabic district] · Type of Service · [Arabic service type]`

The Arabic columns duplicate the English ones. They were not carried into the Markdown
tables, because the English columns are complete for every row; this is the one deliberate
omission and it is recorded here rather than silently dropped.

## Known conversion losses

1. **The Arabic columns are not in the city tables.** English name, city, province,
   district source and service type are. If a user reads Arabic only and gives an Arabic
   hospital name, matching will be by transliteration, not exact string.
2. **District is not a separate column.** The address field mixes district, street and
   Arabic text without reliable delimiters in some rows, so a district column would have been
   guesswork. The provider name plus city is the reliable key.
3. **Unparsed rows.** The automatic split of the publisher's single-line rows into columns
   left some rows without a recognised province: NW7+ 117, NW6 73, NW5 67, NWS 10, NWM 4.
   Those rows are **not** in the city tables. They are not deleted — they are just not
   published here. Treat their absence as "unknown", never as "not in network". This is the
   single largest gap in the conversion and should be closed in a follow-up pass.
4. **`Type of Service` / `Direct` flag.** The "Direct" marker (direct billing) appears in the
   source but only reliably in some sheets, so it is not a column in the city tables.
5. **Telephone.** Taken as the first long digit run in the address tail. A handful of rows
   have malformed numbers (7 digits, or a group number); those show as given, not corrected.
6. **City transliteration.** Bupa's city strings are inconsistent across rows (`Ad Dammam`
   / `Dammam`, `Al Hufuf` / `Al Ahsa`, `At Taif` / `Taif`, `Al Khubar` / `Al Khobar`). City
   files are named after the common English spelling and the variants are folded together;
   the mapping is in `../tiers-and-packages.md` notes and in the generator.

## What Bupa does NOT publish as a file

- **No Class A / Class B network file.** See the naming-traps table in `../tiers-and-packages.md`.
- **No corporate or Munshaat network file** on the public product pages.
- **No Bupa Family network file** on `https://www.bupa.com.sa/en/personal/bupafamily`.
- Bupa's own FAQ states the provider list is viewable **in the Bupa app** ("Explore All
  Hospitals"), i.e. delivered behind login, per member. That is the in-person/app gap the
  interviews described.
