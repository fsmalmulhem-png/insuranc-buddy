# Chubb Arabia — sources checked

All checks on **11 November 2026**.

## The URL supplied does not serve a page

| # | URL | Result |
|---|---|---|
| 1 | `https://www.chubb.com/sa` (given) | 200 but **redirects to `match.adsrvr.org`** — an ad-tracking pixel; body is "A 1x1 image, likely to be a tracker probe" |
| 2 | `https://www.chubb.com/sa/en` | 329 bytes — no usable content |
| 3 | `https://www.chubb.com/middle-east` | 335 bytes — no usable content |
| 4 | `https://www.chubb.com/sa-en` | 200 — **10,225 bytes — the page content is Chubb Saudi, whose own nav links to `chubb.com.sa`** |

So Chubb's global `.com` country sub-paths either bounce through a tracker or carry nothing. The
**country domain `chubb.com.sa`** is the real Saudi site, and its own navigation links to it.

## The working site

| # | URL | Result | Used for |
|---|---|---|---|
| 5 | `https://chubb.com.sa/` | 200 | Navigation, identity |
| 6 | `https://chubb.com.sa/products/` | 200 — 11,647 bytes | **All 17 products** |
| 7 | `https://chubb.com.sa/about-us/` | 200 — 10,036 bytes | **Legal entity, P&C positioning** |
| 8 | `https://chubb.com.sa/contact/` | 200 — 9,725 bytes | Contact numbers |
| 9 | `https://www.chubb.com/sa/robots.txt` | 200 | Global Chubb robots; no Saudi sitemap route |

## Identity, verbatim from the About page

> **Chubb Arabia Cooperative Insurance Company**

> "Chubb Arabia Cooperative Insurance Company is a leading **multi-line property and casualty
> insurer** operating across the Kingdom of Saudi Arabia. As part of the globally renowned Chubb
> Group…"

> "With offices in the Kingdom's three major cities—**Khobar, Riyadh, and Jeddah**—Chubb Arabia
> offers a broad portfolio of products, including **commercial property and casualty insurance,
> personal accident coverage, and group life insurance**."

That second quotation is the decisive statement of scope: P&C, personal accident, group life.
No medical.

## The 17 products, as listed on `/products/`

Casualty · Civil Liability for Populated Areas and High Risk Activities · Contractors Plant &
Machinery · Cyber Security · Directors & Officers Liability · Engineering · Fidelity Guarantee ·
Financial Lines · Jewellers Block · Marine · Money Insurance · Motor · Professional Indemnity ·
Property & Business Interruption · Sabotage & Terrorism · Travel Insurance · Workmen's Comp. /
Employer Liability

**No medical or health product appears.**

## Full-text scan result

Searching every fetched page for `medical`, `health`, `طبي`, `صحي` returned **no product
references**. The only health-adjacent text is travel-insurance context.

## Contacts, from `/contact/`

| Channel | Value |
|---|---|
| Toll Free Number | **8001160038** |
| Toll Free Outside KSA | **920024429** |
| WhatsApp | +966 920024429 |
| Head office | 8th floor, Alkhobar Business Gate |

## Note on method

`chubb.com.sa` is a WordPress site with conventional routes — no bundle reading needed. Content
rendered cleanly through a text proxy. The only difficulty was the supplied URL, which goes
through an advertising tracker and yields nothing; that is recorded so nobody repeats it.

## Nothing from outside chubb.com.sa informs this skill

No third-party directory was used. Global Chubb's health products in other countries are noted as a
source of user confusion, not as evidence about the Saudi entity.
