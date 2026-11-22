# ACIG — the network, and why there are no city files

## No provider list, and no public way to ask for one

ACIG publishes no network file. It does run a member portal with a provider lookup inside it,
but that lookup is not reachable without an account — so it cannot be read, cited, or
converted.

## The Toshfa member portal

| Fact | Detail |
|---|---|
| URL | `https://medonline.acig.com.sa/MemberPortal/` |
| App title | **Toshfa** |
| What it is | Angular single-page member application |
| Provider code present in bundle | `Provider`, `ProviderOnline`, `ProviderGroup_GroupName`, `ProviderBindInfo`, `ProviderEndoDetails`, `fa-hospital-o` |
| **Access** | Every provider route carries `canActivate` (ACIG's auth guard) |

**What this means in plain terms:** ACIG has built the thing a member needs — a search for
their own providers — and put it behind a login. A member uses it. The advisor does not see it.

Attempting the route directly (`/MemberPortal/Provider`) returns **404**, and the guard sends
unauthenticated users back. So there is no public path in.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `acig.com.sa/robots.txt` | Proxy timeout; no robots file readable |
| 2 | `acig.com.sa/sitemap.xml` | Proxy timeout; **site serves an SPA, not a real sitemap** |
| 3 | `acig.com.sa/` (direct) | 200 — Angular shell; meta description confirms health insurance |
| 4 | `main.js` bundle (740 KB) — extracted every route | Full route list: products, individuals-insurance, company-insurance, download-center, FAQ, contact-us, cancel-medical-insurance. **No network or provider route** |
| 5 | Every public route fetched directly | All return the identical 18,308-byte SPA shell; content is client-rendered, so route-level content is not server-readable |
| 6 | `download-center`, `frequently-asked-questions` via proxy | 422 timeout |
| 7 | Portal bundle (3 MB) — searched for provider code | Found provider components and API base `ToshfaOptimaClientApi/api/` |
| 8 | `/MemberPortal/Provider`, `/MemberPortal/ProviderOnline` | 404 — guarded routes |
| 9 | `medonline.acig.com.sa/` root | 200 — same portal shell |

## Why the member portal could not be harvested

Even setting the login aside, the portal is an Angular SPA whose provider data comes from
`ToshfaOptimaClientApi/api/` — an authenticated API. There is no export, no static file, and no
public endpoint. Nothing to convert.

## What would legitimately fill this skill

1. **A member's Toshfa session** — screenshots or an export of their provider list. That gives
   one policy's real network, convertible into city tables.
2. **A policy pack** — ACIG or its administrator may ship a network booklet.
3. **A call to ACIG support (8001246999)** asking for the current network for a named class.

## What the agent does instead

Hands the member the Toshfa portal, ACIG's support numbers, and the hospital question. See
`../SKILL.md`.
