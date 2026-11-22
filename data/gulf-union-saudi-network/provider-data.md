# Gulf Union — provider data at a glance

## How many providers

Unknown — member-scoped.

## Where the network data lives

`/health/health-services-providers` inside the customer portal, fetched as `PointedProviders(MemberId=…)`.

## Why it is not in this skill

The call needs a signed-in member's ID; the answer differs per policy.

## Can this skill name a hospital?

**No.**

---

This file exists so every skill in the set has the same shape. The four skills with full
hospital tables — **GIG**, **Amana**, **Bupa** and **Gulf General** — carry city files under
`network/`. The rest cannot, because the underlying data was never published, is member-locked,
or is out of date.

Absence here is a finding, not a gap in the work. See `network/README.md` and
`sources/index.md` for the evidence behind each statement.
