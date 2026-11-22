# Gulf General (GGCI) — how the city files were built

## Source

One file: **`SME_Network_GI_KSA.pdf`**, 13 pages, dated **14 September 2025**, linked from GGCI's
corporate health product page.

URL: `https://www.ggi-sa.com/uploads/20250914044040-453242834-SME_Network_GI_KSA_temp.pdf`

## Extraction

The PDF renders as text. Rows follow:

```
Provider Name  CCHI No  DD-Mon-YYYY  class-mark  /  telephone  [Arabic name]
```

A regular expression captured: provider name, CCHI number, expiry date, class mark and phone.
**423 rows** were recovered across **59 cities**.

City came from the section heading above each block of rows (`# RIYADH`, `# DAMMAM`, …), which
the file uses to group providers geographically.

## Known losses

1. **Arabic provider names are not carried.** They exist in the file but extract in presentation
   form with RTL disorder. The English name is complete and is the key used.
2. **Telephone is often missing.** Many rows show `—`; the phone column in this file is sparsely
   populated, unlike Bupa's.
3. **Class marks are preserved, not interpreted.** See `../tiers-and-packages.md`.
4. **Rows outside the regex are absent.** Anything whose columns did not match is not in the
   tables. Treat absence as unknown.

## Why every row carries an expiry date and a validity flag

Because **421 of the 423 accreditations have lapsed**. Presenting this list as current coverage
would be actively harmful, so each row states when its accreditation ended, and each file
declares how many rows remain valid.

The sort order puts **still-valid providers first** in every city file, so the usable subset is
what the reader sees first.

## A caution for whoever re-runs this

GGCI may have republished the file since. Check the filename on the product page — the current
one is `...20250914044040-...`, i.e. 14 Sep 2025. If a newer date appears, re-convert and this
skill's warning may no longer apply.

Also note the filename contains `temp` — it may be a placeholder rather than the settled
publication. Worth asking GGCI directly whether this is their current network document.
