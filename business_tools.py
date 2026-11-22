```
"""Wkala business tools for Insurance Buddy.

Reads the carrier network files. Four carriers publish real per-city provider
tables (Amana, Bupa, GGI, GIG); the rest publish no list and must never be
answered with a hospital name.

The tool subject and authorization come from the signed invocation, never from
model output.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel

DATA = Path(__file__).parent / "data"

CARRIERS = {
    "acig": "acig-saudi-network",
    "aseej": "acig-saudi-network",
    "arabia insurance": "aicc-arabia-insurance-saudi-network",
    "aicc": "aicc-arabia-insurance-saudi-network",
    "al etihad": "al-etihad-saudi-network",
    "aljazira": "aljazira-takaful-saudi-network",
    "al jazira": "aljazira-takaful-saudi-network",
    "al rajhi": "alrajhi-takaful-saudi-network",
    "rajhi": "alrajhi-takaful-saudi-network",
    "al sagr": "alsagr-saudi-network",
    "sagr": "alsagr-saudi-network",
    "amana": "amana-coop-saudi-network",
    "arabian shield": "arabian-shield-saudi-network",
    "bupa": "bupa-saudi-network",
    "buruj": "buruj-saudi-network",
    "chubb": "chubb-saudi-network",
    "gulf general": "ggi-gulf-general-saudi-network",
    "ggi": "ggi-gulf-general-saudi-network",
    "gig": "gig-gulf-insurance-saudi-network",
    "gulf insurance": "gig-gulf-insurance-saudi-network",
    "gulf union": "gulf-union-saudi-network",
    "integrated insurance": "integrated-insurance-broker-saudi-network",
    "liva": "liva-insurance-saudi-network",
    "al alamiya": "liva-insurance-saudi-network",
    "malath": "malath-saudi-network",
    "medgulf": "medgulf-saudi-network",
    "med gulf": "medgulf-saudi-network",
    "saico": "saico-saudi-network",
    "salama": "salama-iaic-saudi-network",
    "iaic": "salama-iaic-saudi-network",
    "enaya": "saudi-enaya-saudi-network",
    "tawuniya": "tawuniya-saudi-network",
    "uca": "uca-united-cooperative-saudi-network",
    "united cooperative": "uca-united-cooperative-saudi-network",
    "walaa": "walaa-saudi-network",
    "wataniya": "wataniya-saudi-network",
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").strip().lower()).strip("-")


def find_carrier(text: str) -> str | None:
    """Return the carrier data directory name named in `text`, or None."""
    t = (text or "").lower()
    for name in sorted(CARRIERS, key=len, reverse=True):
        if re.search(r"\b" + re.escape(name) + r"\b", t):
            return CARRIERS[name]
    return None


class Hospital(BaseModel):
    name: str
    network: str
    phone: str | None
    address: str | None
    provider_type: str = ""


class HospitalSearch(BaseModel):
    carrier: str | None
    city: str
    class_level: str
    may_name: bool
    reason: str
    hospitals: list[Hospital]


def _network_dir(carrier: str) -> Path:
    return DATA / carrier / "network"


@lru_cache(maxsize=64)
def _cities_cached(carrier: str) -> tuple[str, ...]:
    d = _network_dir(carrier)
    if not d.is_dir():
        return ()
    return tuple(sorted(p.stem for p in d.glob("*.md") if p.stem != "README"))


def published_cities(carrier: str) -> list[str]:
    return list(_cities_cached(find_carrier(carrier) or carrier))


def search_hospitals(carrier_text: str, city: str, class_level: str, limit: int = 4) -> HospitalSearch:
    """Look for hospitals in the carrier's published city table.

    `may_name` is False whenever this insurer has no published table for the
    city or the class cannot be tied to a row. The caller must obey it.
    """
    carrier = find_carrier(carrier_text)
    cls = (class_level or "").strip().upper().replace("CLASS", "").strip()

    if not carrier:
        return HospitalSearch(
            carrier=None, city=city, class_level=class_level, may_name=False,
            reason="No carrier file for this insurer, so no hospital may be named.",
            hospitals=[],
        )

    cities = published_cities(carrier)
    if not cities:
        return HospitalSearch(
            carrier=carrier, city=city, class_level=class_level, may_name=False,
            reason="This insurer publishes no provider list, so no hospital may be named.",
            hospitals=[],
        )

    f = _network_dir(carrier) / f"{slug(city)}.md"
    if not f.exists():
        return HospitalSearch(
            carrier=carrier, city=city, class_level=class_level, may_name=False,
            reason=(f"This insurer publishes no table for {city}, so no hospital may be named."),
            hospitals=[],
        )

    if cls not in {"A", "A+", "B", "B+", "C", "C+", "VIP", "VVIP"}:
        return HospitalSearch(
            carrier=carrier, city=city, class_level=class_level, may_name=False,
            reason="The class on the card is unknown, so no hospital may be named.",
            hospitals=[],
        )

    rows = _parse_table(f.read_text(encoding="utf-8"))
    if not rows:
        return HospitalSearch(
            carrier=carrier, city=city, class_level=class_level, may_name=False,
            reason=f"The {city} table could not be read, so no hospital may be named.",
            hospitals=[],
        )

    matched = [r for r in rows if _row_allows_class(r, cls)]
    matched.sort(key=_place_rank)
    matched = matched[:limit]
    if not matched:
        return HospitalSearch(
            carrier=carrier, city=city, class_level=class_level, may_name=False,
            reason=(f"No hospital in the published {city} table matches Class {cls} "
                    "for this insurer."),
            hospitals=[],
        )

    return HospitalSearch(
        carrier=carrier, city=city, class_level=class_level, may_name=True,
        reason=f"{len(matched)} hospital(s) from the published {city} table.",
        hospitals=matched,
    )


def _parse_table(text: str) -> list[Hospital]:
    """Read the provider table from a city file."""
    header = None
    out: list[Hospital] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            low = [c.lower() for c in cells]
            if "provider" in low:
                header = low
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        row = dict(zip(header, cells))
        name = row.get("provider", "").strip()
        if not name:
            continue
        network = (row.get("network")
                   or row.get("network list")
                   or row.get("tiers accepted")
                   or "").replace("*", "").strip()
        phone = (row.get("telephone") or "").strip()
        addr = (row.get("address") or "").strip()
        ptype = (row.get("type") or "").strip()
        out.append(Hospital(
            name=name,
            network=network,
            phone=None if phone in ("", "—", "-", "0", "00", "N/A") else phone,
            address=None if addr in ("", "—", "-") else addr,
            provider_type=ptype,
        ))
    return out


def _place_rank(row: Hospital) -> int:
    """Where a person should be sent first.

    A table row may be a hospital, a medical centre, or an optician. Someone
    asking for care must not be handed three optical shops, so hospitals sort
    first and optical, dental and hearing providers sort last.
    """
    t = (row.provider_type or "").lower()
    if "hospital" in t:
        return 0
    if "medical" in t or "clinic" in t:
        return 1
    if any(w in t for w in ("optical", "dental", "hearing", "pharmac")):
        return 9
    return 2


def _row_allows_class(row: Hospital, cls: str) -> bool:
    """Does this provider row cover the wanted class or tier?

    A row is only usable when its own tier text names the class. Tier systems
    that never map to a card class (Bupa's NW7+/NW6/NW5, for example) are not
    guessed at: an unmatched row means the answer is 'I cannot confirm'.
    """
    net = row.network.upper().strip()
    if not net:
        return False
    cls = cls.upper().strip()
    return any(token.strip() == cls for token in net.split(","))


def carrier_summary(carrier_text: str) -> dict:
    """What this insurer publishes — lets the agent answer honestly."""
    carrier = find_carrier(carrier_text)
    if not carrier:
        return {
            "carrier": None,
            "publishes_provider_list": False,
            "cities": 0,
            "note": "No file for this insurer. Ask which insurer is on the card.",
        }
    cities = published_cities(carrier)
    return {
        "carrier": carrier,
        "publishes_provider_list": bool(cities),
        "cities": len(cities),
        "note": ("Published per-city tables are available."
                 if cities else
                 "This insurer publishes no provider list. No hospital may be named."),
    }

```
