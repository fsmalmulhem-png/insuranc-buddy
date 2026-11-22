# Salama — products, classes, and what is published

Populated from Salama's own site (`salama.com.sa`), read 11 November 2026.

## Who they are

**Saudi IAIC Cooperative Insurance Company** — سلامة (Salama). `salama.com.sa` (the `www.` form
redirects to the bare domain).

The site is a Next.js application with an accessibility overlay (UserWay), a login/register pair,
and a full product catalogue.

## Medical products

| Product | Route | Notes |
|---|---|---|
| **Medical insurance** (landing) | `/products/medical-insurance` | Quote request form |
| **Corporate medical** | `/products/medical-insurance/corporate-insurance` | "احصل على تأمين طبي للشركات والمؤسسات الصغيرة والمتوسطة" |
| **SME medical — راحة (Raha)** | `/products/medical-insurance/sme-raha-insurance` | Named product for small establishments |

**راحة (Raha)** is the product name for Salama's SME medical cover. That is the only branded tier
name anywhere on the public site — and it is a **product**, not a class.

## What the product pages actually contain

Both medical pages are dominated by a **quote-request form**:

- عدد الاشخاص (number of persons)
- تعليق (comment)
- رفع المستندات (upload documents)
- إرسال (submit)

That is a lead-capture form, not a benefits table. **There is no published tier ladder, no
class list, no coverage table and no provider list.**

## The PPN reference — the only network fact Salama publishes

In the **cash-claim** flow there is a required field:

> **سبب عدم تلقي العلاج ضمن الشبكة الطبية المعتمدة (PPN) \***
> *"Reason for not receiving treatment within the approved medical network (PPN)"*

Reading it carefully:

| What it tells us | What it does not tell us |
|---|---|
| Salama has an approved medical network | Which providers are in it |
| It is called a **PPN** (Preferred Provider Network) | How many providers, or in which cities |
| It is organisationally central enough to be a claim-failure reason | Whether it varies by class |

The field is a **dropdown of reasons on a form completed after treatment**. It is the opposite of
a directory: it exists because a member has *already* gone outside the network.

## Classes and tiers

| Aspect | Published? |
|---|---|
| Tier names | **No** |
| Class A / Class B | **No** |
| Benefits per class | **No** |
| Provider list / PPN contents | **No** |

Unlike MedGulf (five named tiers) or Saudi Enaya (A/B/C → network codes), Salama publishes **no
tier vocabulary at all** on its public pages.

## Where Salama sits

| Company | Provider list | Class structure |
|---|---|---|
| Bupa · Amana · AICC · Gulf General | Yes | Some |
| Tawuniya · Al Rajhi Takaful · Al Sagr | Lookup only | No |
| ACIG · Gulf Union | Member-locked | No |
| MedGulf | No | 5 tier names + counts |
| Saudi Enaya | No | A/B/C → codes |
| SAICO | No | "category and network" named only |
| **Salama** | **No** | **None — only "PPN" named** |

(Malath, Arabian Shield and Al Etihad also publish nothing; omitted for width.)
