# Salama — network files

## There are none

Salama publishes no medical provider list in any format, and has no public provider search. No
city files exist in this skill.

## What exists instead: a named network with no contents

Salama's claim form references **الشبكة الطبية المعتمدة (PPN)** — the *approved medical network
(PPN)*. So:

- A network exists and Salama has a name for it.
- Its contents are nowhere on the public site.

This is the SAICO pattern again: the insurer names the mechanism and withholds the list. Recording
it matters because it shows the class-and-network structure is **real and internal**, not absent.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `salama.com.sa/robots.txt` | 200 — crawlable |
| 2 | `salama.com.sa/sitemap.xml` | 200 — **37 routes**, fully enumerated |
| 3 | Route scan for `network`, `hospital`, `provider`, `شبكة` | **No network or provider route exists** |
| 4 | `/products/medical-insurance` | 200 — quote form only |
| 5 | `/products/medical-insurance/sme-raha-insurance` | 200 — quote form only |
| 6 | `/products/medical-insurance/corporate-insurance` | 200 — quote form only |
| 7 | `/claims-services` | 200 — the PPN reference lives here |
| 8 | Page HTML (143 KB) — searched for API hosts and provider endpoints | Only Cloudflare Turnstile; **no Salama provider API** |
| 9 | `/assets/downloads/*` | Governance and consumer-protection PDFs only. **No network file** |

Attempt 2 and 3 are decisive: the sitemap is complete and real (37 routes), and none of them is a
network page.

## Why no city files

There is no list to split. Salama's network is described by name only; the providers inside it are
available to a logged-in member or through the call centre, not as a published dataset.

## What would legitimately fill this skill

1. **A member's own PPN** from a logged-in account or a policy pack.
2. **A call to 920023355** asking which hospitals are in the PPN for a named class.
3. **The cash-claim form's own logic** — it already knows which providers count as in-PPN, so
   Salama's claims team can answer per hospital.

## What the agent does instead

Directs the member to the call centre and login, names the term **PPN** so the member uses Salama's
own vocabulary, and gives the hospital question. See `../SKILL.md`.
