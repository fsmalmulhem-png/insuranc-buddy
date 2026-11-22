# Walaa — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://walaa.com/robots.txt` (direct) | 200 — Allow all; sitemap at `/sitemap.xml`; `/dashboard`, `/myprofile` disallowed | Routes and policy |
| 2 | `https://walaa.com/sitemap.xml` | Returns the SPA shell, not XML | Proved the declared sitemap is not a real file |
| 3 | `https://walaa.com/` | 200 — 1,277-byte React shell | Finding the bundle |
| 4 | `https://walaa.com/assets/index-YQjw2Qpg.js` | 200 — **1,752,796 bytes** | **Primary source**: product map, 64 page modules, 25 routes, API config |
| 5 | `https://walaa.com/assets/index-DhTD1zIC.js` | 200 — 7,180 bytes | Document Library chunk |
| 6 | `https://apicoregcp.walaa.com/cms/` and probes | 404 | CMS exists but paths are runtime-built |
| 7 | `walaa.com/document-library`, `/faq`, `/branch-locator` | 200 (SPA shell) | Confirmed routes resolve, content client-side |
| 8 | Rendered via proxy | 248–723 bytes, shell only | Confirmed no server-rendered content |

## Build-output method — recorded deliberately

Walaa serves a Vite/React app whose HTML is a 1.2 KB shell. The `robots.txt` is real, but
`/sitemap.xml` returns the app rather than a sitemap, so route enumeration from a sitemap was
impossible.

The route list therefore came from the **production bundle**, by extracting:

- every `path:"…"` entry in the router,
- every lazy `../pages/…` module reference (64 of them),
- every bare string route (25),
- the product-code → label maps,
- the `VITE_*` configuration block.

Anyone re-checking Walaa should read the bundle, not the HTML.

## API surface found in the config block

Recorded for completeness — **none of these publishes a provider list**:

| Key | Value |
|---|---|
| `VITE_CONTENT_BASE_URI` | `https://apicoregcp.walaa.com/cms/` |
| `VITE_JAVA_BASE_URL` | `https://apicoregcp.walaa.com/web/` |
| `VITE_BACKEND_BASE_URL` | `…/web/claim` |
| `VITE_BACKEND_COMMON_UTILITY_URL` | `…/web/common` |
| `VITE_LOGIN_BASE_URL` | `…/web/login` |

No `…/network`, `…/provider` or `…/hospital` endpoint appears anywhere in the bundle.

**Note:** the config block also contains client-side keys (Firebase API keys, a Google Maps
key, an AES constant). Those are public web values shipped to every browser, not secrets. They
are **not** reproduced in this skill, to avoid copying credentials-shaped strings into a
document the agent loads.

## Why no phone number is asserted

Walaa's contact numbers are fetched from the CMS at runtime and are not present in the bundle.
The Contact page (`walaa.com/contact-walaa`) renders only a shell to a non-browser client, so
the numbers could not be verified. The skill therefore points at the page and states plainly
that no number is held, rather than guessing one.

## Nothing from outside walaa.com informs this skill

No third-party directory was consulted or adopted.
