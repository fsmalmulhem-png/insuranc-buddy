# Saudi Enaya — network files

## The class mapping is public. The provider names are not.

Saudi Enaya publishes network **codes** per class (`SE_VIP`, `SE_A`, `SE_B`, `SE_C+`, `SE_C`,
`SE_C LTD`, `SE_CR`) — but not the hospitals inside them. No city files exist in this skill.

## The provider lookup is member-gated

`/network-provider` exists as a route and **redirects to the login screen** for an anonymous
visitor. The app bundle shows why:

```
POST https://corporate.saudienaya.com/SEMobileApp/api/Provider/GetNetWorkList
POST https://corporate.saudienaya.com/SEMobileApp/api/Provider/GetNetWorkListByFilter
POST https://corporate.saudienaya.com/SEMobileApp/api/Provider/GetNetWorkFilterDetails
```

The request body carries **`PolicyNo`, `MemberNo`, `IdentityNo`** — and optionally `Region`,
`ServiceProvider`, `ServiceOffered`. So the API answers **for one identified member**, against
their own policy. It is a member service, not a public directory.

### Why this could not be exercised

`corporate.saudienaya.com` **times out** from this environment — direct request (40s) and via a
rendering proxy (422). Even if it answered, a valid `PolicyNo` / `MemberNo` / `IdentityNo` pair
would be required, and fabricating those would be both impossible and improper.

Recording the endpoint is still worthwhile: it is the concrete mechanism a future build could use
with a member's consent, and it proves the list exists and is structured.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `saudi-enaya.com` (the URL given) | **No DNS record** — the domain does not exist |
| 2 | `enaya.com.sa` | Live, but a **Riyadh cleaning company**, not an insurer |
| 3 | `saudienaya.com` | 200 — **the actual insurer** |
| 4 | `saudienaya.com/robots.txt` | 200 — crawlable |
| 5 | `saudienaya.com/sitemap.xml` | 200 — full route list |
| 6 | `/network-provider` | Redirects to login for anonymous visitors |
| 7 | `/static/js/main.bd711158.js` (**1.39 MB**) | **Primary source**: the three Provider endpoints |
| 8 | `/sme-plan`, `/corporate-plan` | **Primary source**: the full class table |
| 9 | `corporate.saudienaya.com/SEMobileApp/api/…` | Timeout, direct and proxied |

## What would legitimately fill the hospital layer

1. **A member logs in and exports/sees their network** — the authoritative answer for their class.
2. **The API, called with a real member's consent** — it is already structured for exactly this.
3. **A policy pack** naming in-network hospitals.

## What the agent does instead

States the class's **network code** (which *is* published) and directs the member to the
logged-in Network Provider section. That is a materially stronger answer than any other skill in
this set can give, even without hospital names.
