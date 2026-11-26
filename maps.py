"""Build a Google Maps link that opens the place, with directions ready.

Two decisions, both deliberate:

1. `/maps/dir/` rather than `/maps/search/`. A search URL always shows a list
   of results, which is what we had before: the user had to choose a hospital
   Google had already found for them. The directions URL opens the place, with
   its address and a Directions button.

2. The query is cleaned of the suffixes the provider tables carry. Rows read
   "Al Mana General Hospital - Khobar" and "GAMA Hospital (Ex Astoon Hospital -
   Al Khobar)"; the trailing city and the "Ex ..." note make Google return a
   list rather than the place. They are stripped before the query is built.

The link is only as precise as the address in the table. Where the table holds
a street or district it is used; where it holds only the city, the query is the
name and the city, and Google resolves it.
"""

from __future__ import annotations

import re
from urllib.parse import quote_plus

COUNTRY = "Saudi Arabia"


def _clean(s: str | None) -> str:
    return (s or "").strip().strip(",").strip()


def _is_city_only(address: str, city: str) -> bool:
    a = _clean(address).lower().replace("-", " ")
    c = _clean(city).lower().replace("-", " ")
    if not a:
        return True
    if a == c:
        return True
    return a.startswith(c) and len(a) <= len(c) + 3


def clean_name(hospital_name: str, city: str) -> str:
    """Strip the table's suffixes so Google matches the place, not a list.

    "Al Mana General Hospital - Khobar"          -> "Al Mana General Hospital"
    "GAMA Hospital (Ex Astoon Hospital - Al K.)" -> "GAMA Hospital"
    """
    name = _clean(hospital_name)
    place = _clean(city)

    # drop a trailing parenthetical, e.g. "(Ex Astoon Hospital - Al Khobar)"
    name = re.sub(r"\s*\([^)]*\)\s*$", "", name)
    # drop a trailing " - <city>" or " – <city>"
    if place:
        name = re.sub(r"\s*[-\u2013\u2014]\s*" + re.escape(place) + r"\s*$",
                      "", name, flags=re.I)
    # drop a trailing ", <city>"
    if place:
        name = re.sub(r",\s*" + re.escape(place) + r"\s*$", "", name, flags=re.I)
    return name.strip(" -\u2013,") or _clean(hospital_name)


def maps_query(hospital_name: str, address: str, city: str) -> str:
    """The destination string. Never invents a street or a district."""
    name = clean_name(hospital_name, city)
    addr = _clean(address)
    place = _clean(city)

    parts = [name]
    if addr and not _is_city_only(addr, place):
        parts.append(addr)
    if place:
        parts.append(place)
    parts.append(COUNTRY)
    return ", ".join(p for p in parts if p)


def maps_url(hospital_name: str, address: str, city: str) -> str:
    """A Google Maps directions link that opens on the place itself."""
    return ("https://www.google.com/maps/dir/?api=1&destination="
            + quote_plus(maps_query(hospital_name, address, city)))


def maps_confidence(address: str, city: str) -> str:
    """How much the link can be trusted to land on the right building.

    "street" — the table names a street or district
    "city"   — the table names only the city, so Google resolves the name
    """
    return "city" if _is_city_only(_clean(address), _clean(city)) else "street"
