"""Build a Google Maps link for a hospital.

The link is a *search* URL, not a place ID. That distinction matters: a search
shows the user what Google found, including "did you mean", so a wrong match is
visible and recoverable. A hard-coded place link would look authoritative while
pointing at the wrong building.

The query is only as specific as the data allows. Where the table stores just a
city, the query is "hospital name, city, Saudi Arabia" and the user lands on a
search result — not a guessed pin.
"""

from __future__ import annotations

from urllib.parse import quote_plus

COUNTRY = "Saudi Arabia"


def _clean(s: str | None) -> str:
    return (s or "").strip().strip(",").strip()


def _is_city_only(address: str, city: str) -> bool:
    """True when the 'address' is really just the city name."""
    a = _clean(address).lower().replace("-", " ")
    c = _clean(city).lower().replace("-", " ")
    if not a:
        return True
    if a == c:
        return True
    return a.startswith(c) and len(a) <= len(c) + 3


def maps_query(hospital_name: str, address: str, city: str) -> str:
    """The search string. Never invents a street or a district."""
    name = _clean(hospital_name)
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
    """A Google Maps search link for this hospital."""
    return ("https://www.google.com/maps/search/?api=1&query="
            + quote_plus(maps_query(hospital_name, address, city)))


def maps_confidence(address: str, city: str) -> str:
    """How much the link can be trusted to land on the right building.

    "street" — the table names a street or district
    "city"   — the table names only the city, so the link is a search
    """
    return "city" if _is_city_only(_clean(address), _clean(city)) else "street"
