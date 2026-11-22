# Arabia Insurance (AICC) — the four network documents

## What exists

| # | Network | LinkedIn as | Pages | Date | Provider rows parsed |
|---|---|---|---|---|---|
| 1 | **Corporate** | شبكة الشركات | 54 | 08-11-2026 | **2,524** |
| 2 | **Unique Iqama** | شبكة الإقامة المميزة | 57 | 08-11-2026 | **2,550** |
| 3 | **Elite SME — business** | شبكة المنشآت الصغيرة والمتوسطة | 43 | 08-11-2026 | **935** |
| 4 | **Elite SME — C0666** | شبكة النخبة للمنشآت الصغيرة والمتوسطة | 10 | 07-04-2026 | **336** |

All four are linked from `https://www.aicc.com.sa/products` under **شبكات الرعاية الطبية**
("medical care networks"). Each is a PDF generated from a spreadsheet (the PDF metadata names a
`.xlsx` source).

## Row structure

```
[status per class columns]  Phone  District  [Arabic address/district/city/region]  [Arabic provider name]  S.NO.
```

Status vocabulary:

- `Direct Access`
- `Emergency & Ref` / `Emergency & Referral`
- `NOT COVERED`
- `√` (in the C0666 sheet, meaning covered)

## Why no provider table was published

**Names are Arabic-only**, and the text extraction interleaves them with address words because
the PDF renders right-to-left. A sample of extracted names:

- `مجمع الهشبول` — correct
- `الحزم عشار المطار م` — contaminated with street/district words

Publishing a name column built this way would present wrong hospital names as authoritative. The
skill therefore publishes **class structure and coverage statistics**, which are reliably
extractable, and declines to name providers.

## What is reliable — and therefore published

| Data | Reliability |
|---|---|
| Number of classes per document | ✅ exact |
| Class names (VIP / A / B / C 0222 / C+ / C5+) | ✅ exact |
| Status per class per row | ✅ exact — the three status tokens are unambiguous ASCII |
| Row counts | ✅ exact |
| Telephone | ✅ mostly — Saudi landline pattern |
| Provider name | ❌ not reliable |
| City | ⚠️ partially — Arabic spelling variants resolve ~50% |

## What would close the gap

The underlying **`.xlsx`** files. The PDFs' own metadata names them as the source, so AICC
generated these from spreadsheets. If AICC publishes or supplies the spreadsheets, the full
provider table becomes trivially convertible — names, cities, classes and all.

## Contacts

| Number | Purpose |
|---|---|
| **920005002** | Unified number (الرقم الموحد) |
| **8001288888** | Toll-free (الرقم المجاني) |
| **920002013** | **Medical approvals and claims** — WhatsApp on the same number |
