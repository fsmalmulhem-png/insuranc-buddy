# Tawuniya — network files

## There are now city files. This entry was wrong, and here is why.

This folder previously stated that Tawuniya publishes nothing and that no city
files could exist. That was **incorrect**. The data exists; it is simply not
reachable by an automated fetch.

## What changed

A policy holder supplied a **Tawuniya Class A network list** downloaded from
the Tawuniya mobile app: 154 pages, 1,345 providers across 36 cities. The app
exposes a provider list and a downloadable PDF that the public website does not.

That file has been parsed into `network/<city>.md`, one table per city, in the
same shape as the GIG, Bupa and Amana tables.

| City | Providers |
|---|---|
| Riyadh | 422 |
| Jeddah | 167 |
| Dammam | 81 |
| Al Khobar | 58 |
| Al Qatif | 54 |
| Mecca | 49 |
| Al Ahsa | 48 |
| Tabuk | 47 |

Full list: 36 city files, 1,345 providers.

## Why the automated checks failed

The earlier investigation was not careless — it tried and was blocked at every
turn. Recorded here so the mistake is not repeated:

| # | Attempt | Result |
|---|---|---|
| 1 | Public sitemap (`/sitemap.xml`) | Succeeded, but **no network file route exists** |
| 2 | `/en/individuals/customer-service/network-coverage` | A JS map/search showing branch offices and car-repair workshops, not hospitals |
| 3 | `/download-center` | 404 / application error |
| 4 | Arabic mirror of the download center | Same 404 |
| 5 | Direct requests to `/docs/...` paths | 403 — the host rejects non-browser requests |
| 6 | Guessed bulk endpoints (`/api/network/...`) | 403 |
| 7 | Web search for a Tawuniya network PDF/XLSX | Only third-party mirrors and old Scribd uploads of single employer contracts |

The mistake was concluding **"it does not exist"** from **"I cannot fetch it."**
The data was behind an authenticated mobile app, which no automated check was
going to reach. A person with a policy had it in ten seconds.

## What this file now says

**Yes** — Tawuniya publishes a Class A network, and the advisor may name
hospitals from it.

## Limitations of this source

- **Class A only.** The supplied PDF covers the Class A network. Other classes
  are not in this data, and the advisor must not name a hospital for them.
- **No telephone numbers.** The source lists none, so none are given. The
  advisor must not invent one.
- **Undated.** The PDF does not state when the network was captured. Treat the
  tables as accurate at the time of the interview, not today.
- **A single snapshot.** Networks change; this is one moment, not a live feed.
