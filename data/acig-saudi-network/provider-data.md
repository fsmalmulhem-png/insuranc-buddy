# Acig — provider data at a glance

## How many providers

Unknown — not published.

## Where the network data lives

Inside the **Toshfa** member portal at `medonline.acig.com.sa/MemberPortal/`, behind ACIG's authentication guard.

## Why it is not in this skill

The provider routes carry `canActivate` (ACIG's auth guard). A member sees their own network; nobody else can read, cite or convert it.

## Can this skill name a hospital?

**No.**

---

This file exists so every skill in the set has the same shape. The four skills with full
hospital tables — **GIG**, **Amana**, **Bupa** and **Gulf General** — carry city files under
`network/`. The rest cannot, because the underlying data was never published, is member-locked,
or is out of date.

Absence here is a finding, not a gap in the work. See `network/README.md` and
`sources/index.md` for the evidence behind each statement.
