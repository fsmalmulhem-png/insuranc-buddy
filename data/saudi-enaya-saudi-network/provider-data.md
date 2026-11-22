# Saudi Enaya — provider data at a glance

## How many providers

Unknown — member-scoped.

## Where the network data lives

Per-member API: `corporate.saudienaya.com/SEMobileApp/api/Provider/GetNetWorkList`, carrying `PolicyNo`, `MemberNo`, `IdentityNo`.

## Why it is not in this skill

The host times out from here and the call requires one identified member's credentials.

## Can this skill name a hospital?

**No.** Class→network codes *are* published — see `tiers-and-packages.md`.

---

This file exists so every skill in the set has the same shape. The four skills with full
hospital tables — **GIG**, **Amana**, **Bupa** and **Gulf General** — carry city files under
`network/`. The rest cannot, because the underlying data was never published, is member-locked,
or is out of date.

Absence here is a finding, not a gap in the work. See `network/README.md` and
`sources/index.md` for the evidence behind each statement.
