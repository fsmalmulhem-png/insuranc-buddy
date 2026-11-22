# Tawuniya — sources checked

Every URL below was opened on **10 November 2026**. The result column is what happened, not
what was hoped for.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.tawuniya.com/sitemap.xml` | 200 — full route list | Enumerating every health route; confirming no network file route |
| 2 | `https://www.tawuniya.com/en/individuals/customer-service/network-coverage` | 200 via text proxy; 403 direct | Confirmed interactive lookup; **no downloadable list** |
| 3 | `https://www.tawuniya.com/ar/individuals/customer-service/network-coverage` | 200 via text proxy | Arabic mirror, same finding |
| 4 | `https://www.tawuniya.com/download-center` | Page errors / 404 | Confirmed no document hub is working |
| 5 | `https://www.tawuniya.com/ar/download-center` | 404 "page not found" | Same |
| 6 | `https://www.tawuniya.com/corporate` | Application error (JS chunk fails) | No network file |
| 7 | `https://www.tawuniya.com/medicalsme` | Renders shell, no data | No network file |
| 8 | `https://www.tawuniya.com/services/primary-providers` | Marketing page | No network file |
| 9 | `https://www.tawuniya.com/robots.txt` | Redirects to homepage | No sitemap hints |
| 10 | `https://www.tawuniya.com/docs/…` (direct file paths) | 403 | Host blocks non-browser requests |

## Redirect note

`www.tawuniya.com.sa` (the URL supplied in the task) redirects to `www.tawuniya.com`. All
work above was done against the canonical host.

## Third-party documents rejected

| Source | Why rejected |
|---|---|
| Scribd uploads titled "Tawuniya provider list" | One employer's contract network, undated, unverifiable |
| SA doctor insurance directory (`sa.doctor`) | Aggregator listing 155 facilities "accepting Tawuniya" — no plan/class dimension, no source cited |
| Arabic blog posts listing Tawuniya hospitals | Editorial summaries, no primary source, no date |

These were **not** used to build any table. Recording them here so the decision is
inspectable: the material existed, and was rejected for being unverifiable rather than
authoritative.
