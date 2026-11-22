---
name: buruj-saudi-network
description: Buruj Cooperative Insurance (بروج) — NO LONGER AN INDEPENDENT INSURER. Merged into MEDGULF on 26 October 2025; policies continue under the MEDGULF name and its medical network is handled by TCS on 920014001 (24/7). Read when a user's card or policy says Buruj, to redirect them to the correct current routes.
---

# Buruj — a merged brand, not a current insurer

## Status — read this before anything else

**Buruj Cooperative Insurance ceased operating as an independent insurer.**

The merger between **Buruj** and **MEDGULF** was **officially completed on 26 October 2025**,
"unifying efforts under the MEDGULF name". Buruj's website (`burujinsurance.com`) no longer
responds — connections time out. Its DNS still resolves, but nothing is served.

**A Buruj user is now a MEDGULF user.** This skill exists to say so clearly and route them
correctly, not to describe a network Buruj once had.

Verified 11 November 2026. Source: MEDGULF's own merger FAQ at
`medgulf.com.sa/home/buruj-faqs`. See `sources/index.md`.

---

## The rule this skill exists to protect

A hospital may accept MEDGULF and still not accept the member's class. Buruj members kept their
policy terms through the merger, so **the class question is unchanged** — only the company name
on the paperwork changed.

---

## What happened, in MEDGULF's own words

Quoting its merger FAQ:

> "the merger between Buruj and MEDGULF was officially completed on **October 26, 2025**,
> unifying efforts under the MEDGULF name"

> "**The issuance of policies through Buruj has been stopped.** If your policy expires, you can
> renew it through MEDGULF"

> "We assure you that all your current services and policies, as well as support channels, will
> continue as usual without any changes."

> "There will be no changes to the insurance terms, and they will remain fully compliant with the
> requirements of the Insurance Authority."

> "All Buruj branches will become part of MEDGULF"

## What a Buruj member should actually do — verified routes

| Need | Route |
|---|---|
| **Medical — approvals, claims, network, complaints** | **TCS on 920014001, 24/7** |
| Motor / general policy questions | 8004414442, Sun–Thu 8:00–16:00 |
| Email for Buruj clients | `M-CSC@medgulf.com.sa` |
| Renewal | Through MEDGULF — Buruj no longer issues policies |
| Claim status portal | `forms.burujinsurance.com/claims/claim-status/services.php` |

### The TCS finding matters

**Buruj's medical member-level services are handled by TCS — the same third-party administrator
whose number appears in the Al Sagr skill.** That is not a coincidence: TCS administers medical
networks for multiple Saudi insurers, so the number a Buruj member should call is the same
administrator an Al Sagr member would call.

This is the clearest evidence in the project that **the insurer brand and the network
administrator are different entities**, and that the member's real answer may come from a name
that appears nowhere on their card.

### A practical warning about the app

MEDGULF's FAQ states plainly:

> "Currently the MEDGULF app does not support Buruj policies."

So a Buruj member who installs the MEDGULF app and finds no policy should not conclude the policy
is missing or expired. They should use the TCS line instead.

## What this skill does NOT hold

- No provider names — Buruj published none that survive, and the current network is MEDGULF's.
- No class names or tiers.
- No city files.

## What the agent must do for a Buruj user

1. Confirm the card or policy says **Buruj** (Arabic: بروج).
2. **Tell them immediately that Buruj merged into MEDGULF on 26 October 2025** — this is the most
   important fact for them, because it explains why Buruj's website is dead and why nothing
   renews under that name.
3. Reassure, quoting MEDGULF: their policies and terms continue unchanged.
4. Ask their class (Class A / Class B) — the class survives the merger.
5. Ask city and service.
6. **Do not name a hospital.** Refer to the MEDGULF skill for what MEDGULF publishes
   (`medgulf-saudi-network`), and note it publishes tier names and provider counts but no
   hospital list.
7. Give the working routes:
   - **Medical: TCS 920014001, 24/7**
   - Motor/general: 8004414442
   - Email: `M-CSC@medgulf.com.sa`
8. Warn that the MEDGULF app does not support Buruj policies.
9. Give the hospital question: *"Do you bill MEDGULF Class [A/B] directly?"* — note the company
   name has changed, so a hospital may still know the policy as Buruj.

---


### The answer block — use this shape every time

1. **What they hold:** a Buruj policy, now administered by **MEDGULF**.
2. **Class:** ask for Class A / Class B; the class survived the merger unchanged.
3. **What to do next:** tell them Buruj merged into MEDGULF on 26 Oct 2025 and their policy continues
   unchanged. Medical questions go to **TCS on 920014001** (24/7). The MEDGULF app does not support
   Buruj policies.
4. **Always ask the hospital:** *"Do you bill MEDGULF Class [A/B] directly?"* — a hospital may still
   know the policy as Buruj.

## Files

| File | Contents |
|---|---|
| `SKILL.md` (this) | The merger, the current routes, procedure. |
| `tiers-and-packages.md` | What transferred and what stopped. |
| `network/README.md` | Why the site is dead and why no provider data exists here. |
| `sources/index.md` | The dead-domain evidence and the merger FAQ. |

---

## Change log

- 2026-11-11 — skill created. `burujinsurance.com` does not respond; merger into MEDGULF
  confirmed complete on 26 Oct 2025 via MEDGULF's merger FAQ. Skill redirects rather than
  describing a defunct network.
