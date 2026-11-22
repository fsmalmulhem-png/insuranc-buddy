# Liva — the visitor network, and why it is not a health network

## What exists

Liva publishes one provider document:

| Property | Value |
|---|---|
| Filename | `Visitor Visa_Medical Service Providers Network_1.PDF` |
| URL | `livainsurance.sa/sites/default/files/2025-01/Visitor Visa_Medical Service Providers Network_1.PDF` |
| Found on | `/en/documents` |
| Pages | **15** |
| Dated in file | **2025-01-09** |
| Published timestamp | 14 January 2025 |

## What it contains

244 provider rows across **45 cities**, in city-grouped sections (RIYADH, JEDDAH, MAKKAH, DAMMAM,
JUBAIL, BURAIDAH, QATIF, ABHA and others).

Per row:

```
Provider Name | Authorized Network | Telephone | [Arabic name] | Provider Code | CCHI No | ExpiryDate
```

**Authorized Network** takes one of two values:

| Network | Providers |
|---|---|
| **Direct** | 192 |
| **Emergency and referral** | 52 |

Provider codes are typed: `HOS` (hospital), `MDC` (medical centre), `PLY` (polyclinic), `CLN`
(clinic), `PHR` (pharmacy).

## Two reasons this cannot be used

### 1. It is visitor-only

The document is the network for **visitor-visa medical insurance** — the mandatory short-term cover
a visitor must hold to enter Saudi Arabia. It is not a resident health network.

Liva does not sell resident health insurance, so there is no resident network to publish. The
visitor document is the whole of Liva's medical network publication.

### 2. Every accreditation has expired

Parsing the file's own `ExpiryDate` column against 11 November 2026:

| | |
|---|---|
| Providers listed | **244** |
| Still valid | **0** |
| Latest expiry in the file | **11 August 2026** |
| Earliest expiry | 13 January 2025 |

Not one provider's CCHI accreditation is current. The document is over a year old and describes a
network whose members' accreditations have all lapsed.

This is the **second** company in the set whose published network is entirely expired — the first
was **Gulf General (GGCI)**, where 421 of 423 had lapsed. Liva's case is starker: **all 244**.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `/en/documents` | 200 — **the network PDF is linked here** |
| 2 | The PDF itself | 200 — 15 pages, parsed |
| 3 | Sitemap enumeration (29 routes) | **No `medical-insurance` or `health-insurance` route** |
| 4 | `/en/medical-insurance` | **404** |
| 5 | `/en/health-insurance` | **404** |
| 6 | FAQ full text | Health mentioned only as a **future** ambition |

So the only medical document Liva publishes is for visitors, and it is expired. There is no
resident health network, because there is no resident health product.

## Why no city files

Publishing 45 city files of expired, visitor-only providers would look like a usable network and is
not one. The skill records the document and its expiry status instead, and refuses to name a
provider from it.

## Contacts

| Channel | Value |
|---|---|
| Call centre | **8002444481** |
| WhatsApp | same number (`wa.me/9668002444481`) |
| Travel assistance (24/7) | **+971 4 601 8777** |
