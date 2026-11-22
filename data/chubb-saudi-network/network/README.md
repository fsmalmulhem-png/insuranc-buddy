# Chubb Arabia — network files

## There is no network, because there is no health product

Chubb Arabia Cooperative Insurance Company is a **property and casualty** insurer. Its published
catalogue of **17 products** contains no medical or health line — so there is no provider network,
no city list and no Class A / Class B structure to document.

This is not an insurer withholding its network. It is an insurer that does not sell the product.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `chubb.com/sa` (supplied URL) | **Redirects to an ad-tracking pixel** (`match.adsrvr.org`) — no page content |
| 2 | `chubb.com/sa/en`, `/middle-east` | 329–335 bytes — no usable content |
| 3 | `chubb.com/sa-en` | 200 → resolves to **`chubb.com.sa`** — the real Saudi site |
| 4 | `chubb.com.sa/products/` | 200 — **all 17 products enumerated** |
| 5 | `chubb.com.sa/about-us/` | 200 — *"multi-line property and casualty insurer"* |
| 6 | `chubb.com.sa/contact/` | 200 — contact numbers |
| 7 | Full-text scan of all pages for `medical`, `health`, `طبي`, `صحي` | **Zero relevant matches** — only travel-insurance context |

Attempts 4 and 7 are decisive: the product catalogue is complete and public, and no page mentions
health insurance as a product.

## The three things easily mistaken for health

Worth listing here because they are where a user's confusion will come from:

| Product Chubb DOES sell | Why someone might call it "health" |
|---|---|
| **Travel Insurance** | Travel policies often include emergency medical cover abroad |
| **Group Life** | Frequently bundled with group medical at other insurers |
| **Personal Accident** | Pays for injury; sounds health-adjacent |

None of these is a domestic health policy. None has a hospital network.

## What the agent does instead

Establishes that Chubb Arabia does not sell health in Saudi Arabia, identifies which of the three
near-misses the user actually holds, and — if they need real health cover — explains that this must
come from a different insurer.

## Contacts, for confirmation

| Channel | Value |
|---|---|
| Toll-free (inside KSA) | **8001160038** |
| Outside KSA | **920024429** |
| WhatsApp | +966 920024429 |

Useful if a user wants to confirm directly that their Chubb policy is not medical.
