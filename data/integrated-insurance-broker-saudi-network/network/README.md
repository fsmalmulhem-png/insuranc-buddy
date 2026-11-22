# "Integrated Insurance" — network files

## There is no network, and no domain to read it from

Two independent reasons:

1. **`integratedinsurance.com.sa` does not exist** — no DNS record, zero Wayback captures.
2. **The entity behind the phrase is a broker**, and a broker holds no provider network.

No city files exist in this skill.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | DNS for `integratedinsurance.com.sa` | **No record** |
| 2 | DNS for `www.` variant | **No record** |
| 3 | Direct HTTP request | `Could not resolve host` |
| 4 | Text-proxy fetch | 422 |
| 5 | Wayback availability API | `archived_snapshots: {}` |
| 6 | Wayback CDX index | **0 rows** — never captured |
| 7 | Search for the company name | One match: **NIB, National Insurance Brokerage** |
| 8 | `nib.com.sa/en` | 200 — broker description, contacts |
| 9 | `nib.com.sa/sitemap.xml` | 12 routes — **no provider or network page** |

Attempts 5 and 6 together are conclusive: the domain was never published, so there is nothing
historical to recover either.

## Why a broker cannot supply a network

A broker places business with insurers. NIB states it works with **more than 20** partner insurers.

So for any given member:

- the **network** is whichever insurer underwrote the policy;
- the **class** is set in that insurer's schedule;
- the **card** names that insurer.

NIB cannot answer "which hospitals", because NIB does not know which of 20+ networks applies until
the policy is identified — and when it is, the answer belongs to that insurer's publication, which
this project documents in that insurer's own skill.

## What the agent does instead

Asks for the **insurer named on the card**, then uses that insurer's skill. See `../SKILL.md`.

## Contacts

**8001240284** — NIB's published number, for confirming which insurer a policy was placed with.
