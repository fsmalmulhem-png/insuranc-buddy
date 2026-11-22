# Buruj — network files

## None, and the website is dead

`burujinsurance.com` **does not respond**. DNS resolves (212.12.182.211 / 88.85.240.36), but every
connection attempt times out — direct request, `robots.txt`, `sitemap.xml`, and via a rendering
proxy. There is no site to read.

That is consistent with the merger: policies stopped issuing under the Buruj name on
**26 October 2025**.

## Where a Buruj member's network comes from now

From **MEDGULF**, and specifically from **TCS**, which handles member-level medical services:

| Route | Detail |
|---|---|
| **TCS — medical member level** | **920014001**, 24/7 |
| MEDGULF policy level (motor/general/medical) | 8004414442, Sun–Thu 8:00–16:00 |
| Buruj client email | `M-CSC@medgulf.com.sa` |
| Claim status portal | `forms.burujinsurance.com/claims/claim-status/services.php` |

Note that the claim-status portal is still on a `burujinsurance.com` **subdomain**
(`forms.`), even though the main domain is dead. MEDGULF's FAQ links to it, so the forms host has
been kept alive while the website was retired. Worth knowing — a member following an old bookmark
to the main site will fail, but the forms link still works.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `https://www.burujinsurance.com/` | Connection timeout (25s) |
| 2 | `robots.txt` | Timeout |
| 3 | `sitemap.xml` | Timeout |
| 4 | Same three via text proxy | 422 — page.goto timeout |
| 5 | DNS lookup | Resolves: 212.12.182.211 (apex), 88.85.240.36 (www) — so the domain is registered, just not serving |
| 6 | Wayback availability | Snapshot exists from **2023-11-29** — i.e. the last capture predates the merger |
| 7 | MEDGULF merger FAQ | **The authoritative source** — confirms completion and gives current routes |

## Why no city files

There is no current Buruj network. Whatever Buruj published before the merger is superseded, and
the surviving MEDGULF network is documented (with its own limits) in the
`medgulf-saudi-network` skill. Duplicating stale Buruj data here would mislead.

## What the agent does instead

Tells the member about the merger, reassures them their policy continues, and gives the TCS
number — which is the only route that answers a medical network question for them.
