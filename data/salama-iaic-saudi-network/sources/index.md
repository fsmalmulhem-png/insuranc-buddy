# Salama — sources checked

All checks on **11 November 2026**.

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://www.salama.com.sa/` | 200 → `https://salama.com.sa/` (29 KB) | Identity, contacts, nav |
| 2 | `https://salama.com.sa/robots.txt` | 200 | Crawlability |
| 3 | `https://salama.com.sa/sitemap.xml` | 200 — **37 routes** | **Full enumeration**; no network route |
| 4 | `/products/medical-insurance` | 200 — 17,233 bytes | Medical landing, quote form |
| 5 | `/products/medical-insurance/sme-raha-insurance` | 200 — 17,541 bytes | **Raha** SME product |
| 6 | `/products/medical-insurance/corporate-insurance` | 200 — 17,147 bytes | Corporate medical |
| 7 | `/claims-services` | 200 — 17,651 bytes | **The PPN reference** |
| 8 | `/claims/medical-insurance` | 200 — 225 bytes | Thin; redirects |
| 9 | Homepage raw HTML | 200 — 143,279 bytes | API host check, contact numbers |

## The 37 routes

Complete sitemap: home, about, board, members, blogs, branches, customer-service, claims (general,
malpractice, medical, motor, travel), investor-relations, login, register, checkout (malpractice,
motor), and products (general: engineering/accident/liability/marine/property; malpractice;
medical: landing/corporate/sme-raha; motor: comprehensive/corporate/third-party; travel).

**No `network`, `hospitals`, `providers` or `ppn` route.**

## Contact details, verified

| Number | Source | Purpose |
|---|---|---|
| **920023355** | Header `الرقم الموحد` | Unified number |
| **8002440002** | Header `الرقم الموحد` | Toll-free |
| **920002061** | `wa.me/966920002061` | WhatsApp |

Address given on site: Jeddah, Salama Tower, 12th floor, Madinah Road.

## The PPN sentence — exact wording

From the claim services page:

> `سبب عدم تلقي العلاج ضمن الشبكة الطبية المعتمدة (PPN) *`

A required field in a claim form: *"Reason for not receiving treatment within the approved medical
network (PPN)."* Quoted verbatim in `tiers-and-packages.md`.

## Download assets checked

`/assets/downloads/` holds governance, consumer-protection and regulation PDFs (consumer
protection principles, online insurance regulation, data protection, whistleblowing, corporate
governance, surplus distribution). **None is a network list.**

## Method note

The site is a Next.js app behind Cloudflare Turnstile. The sitemap is genuine and complete, so
route discovery did not require reading the bundle — unlike Gulf Union and ACIG. Content rendered
cleanly through a text proxy.

## Nothing from outside salama.com.sa informs this skill

No third-party directory was consulted or adopted.
