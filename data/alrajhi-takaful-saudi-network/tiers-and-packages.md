# Al Rajhi Takaful — plans, classes, and what is publicly known

Populated from Al Rajhi Takaful's own site (`alrajhitakaful.com`), read 11 November 2026.

## Who they are

**تكافل الراجحي** — Al Rajhi Company for Cooperative Insurance (Al Rajhi Takaful). The site
markets itself as "Reinventing Insurance For The Kingdom" and sells motor, health, travel,
home, medical malpractice and a range of business products.

## The health products

| Route | Product |
|---|---|
| `/en/business/health-insurance` | **Health insurance for employees** (SME — the business menu labels it التأمين الصحي للشركات الصغيرة والمتوسطة) |
| `/ar/product-health` | Health product landing |
| `/ar/health-purchase`, `/ar/domestic-health-purchase` | Direct purchase flows |
| `/ar/value-added-medical-services` | Add-on medical services |
| `/ar/personal/medical-malpractice-insurance` | Professional liability (not member treatment) |
| `/ar/health-claims`, `/ar/make-claims` | Claims |

So Al Rajhi Takaful sells health to both companies and individuals — a broader footprint than
Arabian Shield (SME only) and similar to ACIG.

**What is not published:** no benefits table, no tier list, no class names.

## Classes — nothing published

| Aspect | Published? |
|---|---|
| Number of classes | **No** |
| Class names | **No** |
| Class A / Class B mapping | **No** |
| Benefits per class | **No** |
| Class → provider mapping | **No** |
| Provider list as a file | **No** |
| Public per-hospital lookup | **Yes — the medical provider locator** |

This is the same A/B gap as all eight other companies. The difference here is only in *what a
user can do without calling anyone*.

## Where they sit in the set

| Company | Tiers named | Provider file | Public self-service lookup |
|---|---|---|---|
| Bupa | Yes (5) | **Yes** | App |
| **Al Rajhi Takaful** | No | No | **Yes — public locator, no login** |
| Tawuniya | No | No | Yes — search box |
| Al Sagr | No | No | No (TCS route, named) |
| ACIG | No | No | No (member portal, login) |
| MedGulf | Yes (5, counts) | No | No |
| Malath | "classes" only | Dead 2018 PDF | No |
| Arabian Shield | No | No | No |
| Al Etihad | — | — | — (placeholder site) |

Al Rajhi Takaful and Tawuniya are the two "you can check it yourself right now" companies.
Al Rajhi Takaful's locator is the more useful of the two on paper, because it carries a
**"near me"** control — it can answer a location question rather than requiring the user to
already know which hospital to type. That advantage is inferred from the interface (the search
box, the "near me" control and the map pane), **not** from a tested query: the site refuses
non-browser requests, so the result behaviour was never exercised. Say "it has a near-me
control", not "it finds hospitals near you".
