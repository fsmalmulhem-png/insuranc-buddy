# GIG — how the city files were built

## Source

GIG's **public provider locator**: `https://www.gig.sa/provider-locator/`

No login, no API key. And — unusually — **the entire provider dataset is embedded directly in the
page HTML**, not fetched afterwards by JavaScript. That is why it could be extracted completely.

## The markup

Each provider is one block:

```html
<div class="providerEntry hidden"
     data-city="Riyadh"
     data-network="A"
     data-providertype="Dental Provider">
  <h5>SAVVY MEDICAL COMPANY RIYADH</h5>
  <p><span>Group:</span> Savvy Dental Group</p>
  <p><span>Network:</span> A</p>
  <p><span>Provider Type:</span> Dental Provider</p>
  <p><span>Address:</span> Urubah Road, Warood, Riyadh</p>
  <p><span>Main phone:</span> <a href="tel:9665...">…</a></p>
</div>
```

The blocks are class `providerEntry hidden` — visually hidden until the locator's own JS filters them
by city/network/type. **3,437 blocks were present in the page source.**

## Extraction result

| | Count |
|---|---|
| Provider blocks found | **3,437** |
| Blocks with a provider name | 3,437 |
| Distinct city strings (raw) | 374 |
| **Distinct cities after normalisation** | **357** |
| Cities written as files | 355 |

## City normalisation

GIG's city strings are inconsistent (`Khobar` / `alkobar`, `Bureidah` / `Burayda`, `Skaka` /
`Sakaka`, `Hofuf` / `Al Hufuf`, `Dammam City` / `Dammam`). These were folded to one common English
form so a city is one file — 374 raw strings became 357 cities.

The mapping is in the extraction notes; the original string is not retained per row.

## Known limits

1. **Numbered tiers are not in the locator.** The locator tags `VIP`; the benefit table lists
   `VIP 1` … `VIP 5`. The files carry the family tag only.
2. **Pharmacies dominate the row count** (2,073 of 3,437). The type column makes this visible, and
   the skill warns against quoting 3,437 as a hospital count.
3. **Telephones** come from `tel:` links and are mobile numbers in many cases (e.g.
   `966568786899`) rather than clinic landlines. Presented as published.
4. **The locator may not be exhaustive.** It is what GIG chose to publish. A provider absent from it
   is not proven absent from the network — the skill says "I cannot confirm this" rather than "not
   covered".

## Why this is the strongest dataset in the set

Every other company that published anything gave provider *names* without a network tag (Bupa,
Amana) or network structure without names (Saudi Enaya, MedGulf). **GIG gives both**, in one
public page, with 3,437 rows.

That makes it the reference case: where a provider and a network can be joined, the advisor can
answer the real question — *is this hospital on MY tier* — from published data, with a source.
