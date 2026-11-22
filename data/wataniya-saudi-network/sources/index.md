# Wataniya — sources checked

All checks on **11 November 2026**.

## First: the name

| Name | Arabic | Domain | Sells health? |
|---|---|---|---|
| **Wataniya** / The National Insurance Company | **الوطنية** للتأمين | `wataniya.com.sa` | **No** |
| **Tawuniya** / Company for Cooperative Insurance | **التعاونية** | `tawuniya.com.sa` | Yes |

The two English names differ by a single letter. Both are Saudi insurers. They are **not related**
and do not share products. This distinction is the main reason this skill exists.

DNS check confirmed they are separate hosts (different IP ranges), so no redirect or aliasing
between them.

## Pages read

| # | URL | Result | Used for |
|---|---|---|---|
| 1 | `https://wataniya.com.sa/` | 200 — 14,776 bytes → `/Wataniya_web/` | **Full product menu** |
| 2 | `https://www.wataniya.com.sa/robots.txt` | 200 (served the page, no real robots) | Confirmed no sitemap route list |
| 3 | `/Wataniya_Home/CorporateDLIOtherInsurances` | 200 — 2,717 bytes | **Checked the "other" bucket for a hidden health line — none** |
| 4 | `/Wataniya_Home/clientcarecenter` | 200 — 6,145 bytes | **Contact numbers** |
| 5 | `/Wataniya_Home/ContactUs` | 200 — 13,206 bytes | Cross-check, identity |

## Site title, verbatim

> **الشركة الوطنية للتأمين أون لاين جدة، المملكة العربية السعودية**

*The National Insurance Company online, Jeddah, Saudi Arabia.*

## The product menus as rendered

**الأفراد (Individuals):** تأمين المركبات · تأمين المنازل · تأمين السفر · اخطاء المهن الطبية

**الشركات (Corporate):** تأمين المركبات · الممتلكات · الهندسي · النقل البحري · المسؤولية
والتعويضات · الحياة والحوادث الشخصية · تأمين هيكل الطائرة · أخرى

**المنشآت الصغيرة والمتوسطة (SME):** the same corporate set with `?Segment=SME`

**أخرى (Other), enumerated:** extended warranty, fine arts, extended warranty, banker's blanket
bond, events cancellation, cyber risk, heritage buildings, domestic labour.

**No health line at any level.**

## The malpractice product, verbatim

> "اخطاء المهن الطبية — تأمين اخطاء المهن الطبية
> إذا كنت ممارسًا طبيًا يوفر لك هذا التـأمين حماية قانونية متوافقة مع أحكام الشريعة الإسلامية
> تحميك من أي شكاوى او اخطاء تتعلق بالسهو أثناء مزاولة المهنة"

Professional liability for practitioners — not member treatment cover.

## Contacts, from `/clientcarecenter`

| Channel | Value | Hours |
|---|---|---|
| Toll-free | **8001188855** | 8:45 AM – 4:45 PM |
| WhatsApp | **9668001188855** | 24 hours |
| International | **966126013400** | — |

Address reference: Jeddah 23615.

## Method note

The site is server-rendered with traditional `/Wataniya_Home/…` routes — not an SPA. `robots.txt`
returns the page rather than a policy, and there is no usable sitemap, so the product menu was
enumerated directly from the rendered homepage, which lists every line explicitly. That is
sufficient here: an insurer's own navigation is the authoritative statement of what it sells.

## Nothing from outside wataniya.com.sa informs this skill

No third-party directory was consulted or adopted. The Tawuniya comparison comes from
`tawuniya-saudi-network`, a separate skill built earlier from Tawuniya's own site.
