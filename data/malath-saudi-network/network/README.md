# Malath — network files

## A network file exists. I could not get it.

Malath links a medical network PDF from its own site:

```
/data/content/docs/CustomerCare/2018.9.30.12.59.4.947.1927940-Malath_Medical_Network_List_R.pdf
```

It appears on both the **Products** page and the **Downloads** page, under Customer Care,
alongside the Road Assistance manual and the Corporate Kit. So the company does publish a
provider list — the only one of the four checked so far that publishes a single network file
rather than per-tier spreadsheets or a search box.

**It is not in this skill, for two independent reasons.**

## Reason 1 — the file is dated 2018

The filename encodes `2018.9.30`. At the newest, that list is eight years old. Insurance
networks change continuously, and this project's whole premise is that a member needs current
information. Using a 2018 list to tell someone which hospital will treat them today would be
worse than saying nothing.

## Reason 2 — it cannot be retrieved

| # | Attempt | Result |
|---|---|---|
| 1 | Direct request to `malath.com.sa` (both resolved IPs, 88.85.242.246 and 77.240.87.189) | Connection timeout after 30s, on every path including `/robots.txt` |
| 2 | Text proxy fetch of the homepage | Timeout — "page.goto: Timeout 60000ms exceeded" |
| 3 | Text proxy fetch of the PDF URL | Timeout |
| 4 | Wayback Machine availability API for the PDF | `"archived_snapshots": {}` — **never archived** |
| 5 | Wayback CDX index for the whole domain | Snapshots exist for HTML pages only; no PDF captures |
| 6 | Wayback replay of the PDF URL (`/web/2024id_/…`) | 404 — archive has the link, not the file |

The HTML pages that *link* the PDF were archived (that is where the URL came from); the PDF
itself was not.

## What the archived pages are good for

The archived **Products** and **Contact** pages gave this skill its real content: Malath's
health products, the SME program's "plans and classes" wording, and the contact numbers. Those
are HTML, small, and safely captured. See `sources/index.md`.

## What would legitimately fill this skill

1. **Retrieve the PDF from a network that can reach `malath.com.sa`** — then convert it the way
   the Bupa spreadsheets were converted, but first check its date, and refuse to publish it if
   it is still the 2018 edition.
2. **Ask Malath for the current network file** — a member, or the project owner by phone
   (9200 15815). Insurers will send the current list to a policyholder.
3. **A member's CCHI/Malath card pack**, which usually ships with a network booklet.
4. **The voice-agent route** already scoped as future work.

## What the agent does instead

Gives the member the call-centre number and the exact question to ask the hospital. See
`../SKILL.md`.
