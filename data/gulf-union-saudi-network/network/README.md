# Gulf Union — the provider list, and why it is not public

## A provider lookup exists — inside the member login

The customer portal has a **Service Providers** page, linked from the Health section as:

- Route: `/health/health-services-providers`
- Icon label: *Service Provider* / *مقدم الخدمة*
- Sits alongside Health Benefits, Health Approvals, New Cash Claims

So Gulf Union does provide a provider search. It is not public.

## The evidence it is member-scoped

From the compiled application bundle (`main.0a0a484477a881a0.js`, 4.3 MB), the provider call is:

```js
PointedProviders("MemberId=" + memberId)
```

and, where a city/provider filter is applied:

```js
... + this.memberId + "&CityId=" + this.selectedCity
... += "&ProviderId=" + this.providerId
```

`memberId` and `mobileNumber` come from **local session storage**
(`_LocalService.getJsonValue("memberDetails")`). The medical services base URL is
`config.servicesBaseUrl + "Health/"`.

**Conclusion:** the provider list is fetched **for one identified member**, filtered by city and
provider. It cannot be enumerated by an outsider, and it would differ per policy anyway.

## Why no city files exist

There is nothing to split by city. The data is returned by an authenticated per-member query; no
static file, export or public endpoint exists. Attempting the API without a session returns
nothing usable, and fabricating a member ID would be both impossible and improper.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `gulfunion.com.sa`, `www.gulfunion.com.sa` | Both **302 → `eservices.gulfunion.com.sa`** |
| 2 | Portal root, direct | 200, 44 KB — Angular shell plus an **F5/Shape bot-protection script** (`/TSPD/…`) |
| 3 | Portal root via text proxy | 200 — full nav and product text rendered |
| 4 | `/robots.txt`, `/sitemap.xml` | Return the app shell; no real robots or sitemap |
| 5 | Bundle `main.0a0a484477a881a0.js` | **72 routes extracted** — found `health/health-services-providers` |
| 6 | Provider route, anonymous | Shell only; requires session |
| 7 | Bundle search for provider/network endpoints | Found `PointedProviders(MemberId=…)`, `GetAllServiceProviders(memberId)` |
| 8 | Bundle search for class vocabulary | None present |

## A note on the bot protection

The portal loads an F5 `TSPD` anti-automation script, and does not serve a usable
`robots.txt` or `sitemap.xml` — both return the application shell. Anyone re-checking should read
the bundle (as here) rather than expect a sitemap route list to exist.

## Contacts

| Detail | Value |
|---|---|
| Phone | **8003040077** |
| Email | `customercare@gulfunion-saudi.com` |
| Portal | `eservices.gulfunion.com.sa` |

## What the agent does instead

Directs the member to log in and open **Health → Service Providers**, and still gives the
hospital question. See `../SKILL.md`.
