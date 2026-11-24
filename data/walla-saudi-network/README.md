# Walaa GMS provider network (Saudi Arabia)

Source: `Walla_Updated_network.xlsx`, shared 2025-11-24. File header: **Date: 07-08-2025**, sheet `GLOBEMED SAUDI`, network "Walaa GMS standard Full Network".

## What the source says

One row per provider, grouped by region and city. The tier columns are:

| Column | Meaning in this dataset |
|---|---|
| `Walaa GMS NEW VIP` | VIP tier |
| `Walaa GMS NEW A` | A tier |
| `Walaa GMS NEW B` | B tier |
| `Walaa GMS New C0222` | C tier |
| `Walaa GMS NEW C0333` | C+ tier (as labelled in the source) |
| `Walaa GMS NEW 0333 PC` | Extra tier (as labelled in the source) |

A tick means the provider accepts that tier. A dash means it does not. The value **Emergency & Referral** is carried through verbatim and means the provider is limited to emergency and referral cases for that tier - it is not the same as a full acceptance.

`Walaa GMS NEW - GMS minimum network` (MPN / OCN / OHN) is a separate column that was **not** used to build these files. It labels the minimum-network class of the provider, not a card tier. Confirm with Walaa before treating it as coverage information.

## Extracted

- 1657 provider rows
- 138 cities across 13 regions
- One Markdown file per city in `classes/`, named by city slug

## Known issues

- **Tier column labels are guesses in two places.** `C0222` was mapped to C and `C0333` / `0333 PC` were mapped to C+ and Extra, based on the label text only. The source does not define these codes. Verify before using them in the advisor.
- **No address beyond district.** The source has street and district in Arabic; only the English district (`District`) is carried into the files. Telephone is carried as `Phone 1`.
- **Names are as printed**, including typos and inconsistent spacing in the source (e.g. duplicated optical entries). Not cleaned.
- **Dated data.** 07-08-2025. Ambiguous format: could be 7 August 2025 or 8 July 2025. Confirm the intended reading with Walaa.
- **City slugs differ from the MedGulf set.** 100 of the 138 Walaa city slugs do not match a MedGulf filename, because the two sources spell cities differently (e.g. Walla `al-hafouf` vs MedGulf `hafouf`). Reconciliation is a separate task and has not been done.
