# Wataniya — network files

## There is no network, because there is no health product

Wataniya does not sell health insurance. Its full product menu — individual, corporate and SME —
covers motor, travel, home, property, engineering, marine, liability, aviation, life/accident,
and medical malpractice. **No medical/health line appears anywhere.**

So there is no provider network to publish and no city files to build. This is not a case of an
insurer withholding its network; it is a case of an insurer with no member health network at all.

## What was checked

| # | Attempt | Result |
|---|---|---|
| 1 | `wataniya.com.sa/` | 200 — full homepage, product menu rendered |
| 2 | Individual menu (الأفراد) | Motor · Home · Travel · **Medical Malpractice** — no health |
| 3 | Corporate menu (الشركات) | Motor · Property · Engineering · Marine · Liability · Life/Accident · Aviation · Other — **no health** |
| 4 | SME menu (المنشآت الصغيرة والمتوسطة) | Same corporate lines with `Segment=SME` — **no health** |
| 5 | `/Wataniya_Home/CorporateDLIOtherInsurances` (أخرى) | Enumerated in full: warranty, fine arts, banker's bond, events cancellation, cyber, heritage buildings, domestic labour — **no health** |
| 6 | Word scan of all page text for طبي / صحي / health | Only **medical malpractice** matched (اخطاء المهن الطبية) |

Attempts 2–5 are the decisive ones: every menu level was enumerated, including the "other"
bucket where an odd product would hide. Health is absent at all three segments.

## What "medical" means here

The only medical-adjacent product is **Medical Malpractice (اخطاء المهن الطبية)** — professional
indemnity for practitioners. It protects a doctor against complaints and negligence claims. It
has:

- no patient/member,
- no hospital,
- no provider network,
- no relevance at a hospital reception desk.

Do not mistake it for health cover.

## What the agent does instead

Asks the user to read the company name off their card. If it says **التعاونية**, they mean
**Tawuniya**, which does sell health — use the `tawuniya-saudi-network` skill. If it genuinely says
**الوطنية** and they believe they have health cover, tell them Wataniya sells none and the policy
must be something else.

## Contacts (for quotes, claims on non-health lines, or to confirm directly)

| Channel | Value |
|---|---|
| Toll-free | **8001188855** (8:45–16:45) |
| WhatsApp | **9668001188855** (24 hours) |
| International | **966126013400** |
