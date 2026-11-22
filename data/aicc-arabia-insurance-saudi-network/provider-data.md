# Aicc Arabia Insurance — provider data at a glance

## How many providers

**2,524 corporate-network rows, 2,550 Iqama rows, 935 SME rows, 336 C0666 rows** — all with per-class status.

## Where the network data lives

Four published network PDFs on `aicc.com.sa/products`, dated 8 Nov 2026 (three of them).

## Why it is not in this skill

Provider **names are Arabic-only** and extraction produced address-contaminated strings. Publishing them would present wrong hospital names as authoritative.

## Can this skill name a hospital?

**No.** Class-level coverage status *is* available — see `tiers-and-packages.md`.

---

This file exists so every skill in the set has the same shape. The four skills with full
hospital tables — **GIG**, **Amana**, **Bupa** and **Gulf General** — carry city files under
`network/`. The rest cannot, because the underlying data was never published, is member-locked,
or is out of date.

Absence here is a finding, not a gap in the work. See `network/README.md` and
`sources/index.md` for the evidence behind each statement.
