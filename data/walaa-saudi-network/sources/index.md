# Walaa — sources

## 1. The provider list (primary)

- **File:** `Walla_Updated_network.xlsx`
- **Sheet:** `GLOBEMED SAUDI`
- **Network name in file:** "Walaa GMS standard Full Network"
- **Header date in file:** `07-08-2025` — ambiguous between 7 August and 8 July 2025.
  Recorded as printed; not resolved.
- **Held by:** the project team (shared 24 November 2026). Not a public URL.
- **What it contains:** 1,657 provider rows, region + city per row, provider name, type,
  owner, phone, district, and six tier columns.

### Tier columns, as printed

| Column header in file | Tier used in `classes/` |
|---|---|
| `Walaa GMS NEW VIP` | VIP |
| `Walaa GMS NEW A` | A |
| `Walaa GMS NEW B` | B |
| `Walaa GMS New C0222` | C |
| `Walaa GMS NEW C0333` | C+ |
| `Walaa GMS NEW 0333 PC` | C+ PC |

**These parenthetical codes are not defined anywhere in the file.** The mapping above is a
reading of the labels, not something Walaa stated.

### Cell values, as printed

| Value | Meaning recorded |
|---|---|
| `√` | tier accepted |
| `-` | tier not covered |
| `Emergency & Referral` | accepted for emergency and referral cases only — not a normal elective visit |
| `cluse` | appears once in the B column; meaning unknown, treated as not covered |

## 2. Walaa's public website (secondary)

Surveyed 11 November 2026 — see `../network/README.md`. No public provider search and no
class definitions. That remains true; this spreadsheet is not published by Walaa publicly.

## 3. Open question

Walaa's site publishes **no** class definitions (no class A/B/A+ naming, no benefit table).
The tiers here are Walaa's own GMS tier names. **How a GMS tier corresponds to the card class
printed on a member's card is not published** — confirm with Walaa before telling a user
"your class A is covered here".
