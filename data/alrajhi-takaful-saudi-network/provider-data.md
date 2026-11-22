# Alrajhi Takaful — provider data at a glance

## How many providers

Unknown as a file; a **public locator** exists.

## Where the network data lives

`alrajhitakaful.com/en/medical-provider-locator` — a live search with a "near me" control.

## Why it is not in this skill

Results render client-side and the host returns **403** to non-browser requests. The interface is documented; no query was ever run.

## Can this skill name a hospital?

**No.**

---

This file exists so every skill in the set has the same shape. The four skills with full
hospital tables — **GIG**, **Amana**, **Bupa** and **Gulf General** — carry city files under
`network/`. The rest cannot, because the underlying data was never published, is member-locked,
or is out of date.

Absence here is a finding, not a gap in the work. See `network/README.md` and
`sources/index.md` for the evidence behind each statement.
