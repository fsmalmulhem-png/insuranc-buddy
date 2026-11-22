# Amana — sources checked

All checks on **11 November 2026**.

## First: neither domain you gave works

| Domain | Result |
|---|---|
| `amana-coop.com.sa` (supplied) | **No DNS record** — `getent hosts` returns nothing |
| `amana.com.sa` | Resolves, but is a **Riyadh accounting firm** (audit, zakat, tax advisory) — not an insurer |
| **`amana.sa`** | ✅ **The insurer** — "Amana Cooperative Insurance", with the network PDFs on its homepage |
| `www.amanainsurance.com` | Also Amana (English site), older design; no network files |

Found by searching the company name. Two thirds of the URLs involved in this request pointed
somewhere else, so the record matters.

## The published network files

| File | URL | Pages | Date |
|---|---|---|---|
| Full network | `https://amana.sa/assets/documents/Amana-Full-Network-21-05-2026-Existing-Policies.pdf` | 49 | 21-05-2026 |
| SME Basic | `https://amana.sa/assets/documents/Amana-SME-Network-Basic-21-05-2026.pdf` | 43 | 21-05-2026 |

Both linked directly from the `amana.sa` homepage under **"Network List"** and
**"SME Network Basic"**. Both were downloaded and converted; both are text PDFs, not scans.

## Contact numbers, from the homepage

| Number | Purpose |
|---|---|
| **8001240242** | Inside the Kingdom |
| **+966114847800** | Outside the Kingdom |
| **920002039** | **Medical Approvals** |

The last one is worth keeping: it is the line a member uses before non-emergency treatment.

## Homepage structure found

```
Individual → Motor · Travel · Personal Accident
Corporate  → Healthcare · Marine · Engineering · Property · Workmen · Money · Fidelity · General
```

Note that **healthcare is a Corporate product** — there is no individual health entry on the
homepage menu. So Amana's medical cover is employer-based, which is consistent with the two
network lists being "policies" and "SME Basic".

## Extraction notes

- PDFs were fetched through a text-rendering proxy, which returns the PDF as Markdown with pages
  preserved (`Number of Pages: 49` / `43` confirmed).
- Rows were split on two-or-more spaces; fields are tabular in the source.
- Provider codes (`H`, `C`, `O`, `P`, `D` prefixes) were used to validate the split — a row is only
  accepted when a code matching `[A-Z]\d{3,6}` is found.

## Nothing from outside amana.sa informs this skill

No third-party directory was used. The two PDFs are Amana's own publication, which is what makes
this one of the two skills in the set with real provider data.
