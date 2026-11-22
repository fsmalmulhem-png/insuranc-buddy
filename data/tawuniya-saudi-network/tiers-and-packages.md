# Tawuniya — plans, packages, and what is publicly known

Status: **thin, because the source is thin.** Populated only from what Tawuniya's public
pages state. No provider data, and no published level-to-network mapping.

## What Tawuniya's site presents

Tawuniya segments health insurance by buyer, not by network level. The product routes that
resolve from the public sitemap are:

| Route | Segment | Notes |
|---|---|---|
| `/individuals/products/health/my-family-insurance` | Individual / family | Direct-to-consumer family product |
| `/individuals/products/domestic-worker-health-insurance` | Domestic workers | Mandated product |
| `/individuals/products/health/hajj-insurance` | Hajj / Umrah visitors | Short-term |
| `/individuals/products/health/umrah-insurance` | Umrah visitors | Short-term |
| `/individuals/products/health/visit-visa-insurance` | Visitors | Short-term |
| `/medicalsme` | SME employers | ≤ 200 employees, by Tawuniya's own framing |
| `/corporate` | Corporate employers | Group plans |

**What is missing from that table, and is the whole problem:** none of these pages names a
network level (no equivalent to Bupa's `NW5` / `NW6` / `NW7+`), and none links a provider
file. Tawuniya presents "network" as a property you look up after you have a policy, not as a
thing the company publishes per product.

## The Class A / Class B gap

Cards in Saudi Arabia commonly print Class A or Class B. Tawuniya's public pages do not use
either term, and publish no mapping from a card's class to a network.

| Card wording | Tawuniya's public wording | Stated anywhere public? |
|---|---|---|
| Class A | — | No |
| Class B | — | No |

Do not invent a mapping. If a user says "Class A" or "Class B" for Tawuniya, the skill cannot
place them, and that is the correct answer.

## The contract problem

Tawuniya sells through employers. Two employees of different companies, both holding
"Tawuniya", can sit on different networks and different limits, because the network is
attached to the employer's contract. A single Tawuniya provider list — even one procured
privately — would not be enough on its own. The plan (usually on the policy schedule, not the
card) has to be named first.

This is the same structural point the Bupa skill records, and it is worth stating once in the
write-up as a property of the market rather than of one insurer.

## What would let this table be filled

A Tawuniya policy schedule or employer HR letter, which names the plan. Even then, the
network list for that plan is not published — it is on Tawuniya's member lookup. See
`network/README.md`.
