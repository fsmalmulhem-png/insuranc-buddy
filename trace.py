"""Build the traversal trace for the Insurance Buddy UI.

Every lookup passes five gates. This module records which ones were passed,
which one stopped the search, and why — in the same order the code checks
them. Nothing here is invented; it is the actual control flow of
business_tools.search_hospitals().
"""

from __future__ import annotations

from dataclasses import dataclass, field

import business_tools as btools


@dataclass
class Step:
    """One gate in the traversal."""

    key: str
    label: str
    detail: str
    state: str          # "passed" | "failed" | "blocked" | "pending"
    count: int | None = None


@dataclass
class Trace:
    insurer: str = ""
    city: str = ""
    class_level: str = ""
    steps: list[Step] = field(default_factory=list)
    hospitals: list = field(default_factory=list)
    reason: str = ""
    may_name: bool = False

    @property
    def stopped_at(self) -> str:
        for s in self.steps:
            if s.state == "failed":
                return s.key
        return ""


def build_trace(insurer: str, city: str, class_level: str) -> Trace:
    """Walk the same gates search_hospitals() walks, recording each one."""
    tr = Trace(insurer=insurer or "", city=city or "", class_level=class_level or "")

    # Gate 1 — is the insurer in the registry?
    carrier = btools.find_carrier(insurer or "")
    if not carrier:
        tr.steps.append(Step("insurer", "Insurer known",
                             "not in the registry of 25", "failed"))
        for key, label in (("list", "Publishes a list"),
                           ("city", "City file exists"),
                           ("class", "Row states the class")):
            tr.steps.append(Step(key, label, "not reached", "blocked"))
        tr.reason = "No carrier file for this insurer, so no hospital may be named."
        return tr

    cities = btools.published_cities(carrier)
    tr.steps.append(Step("insurer", "Insurer known",
                         carrier.replace("-saudi-network", "").replace("-", " "),
                         "passed"))

    # Gate 2 — does this insurer publish any per-city table?
    if not cities:
        tr.steps.append(Step("list", "Publishes a list",
                             "publishes no provider list", "failed"))
        for key, label in (("city", "City file exists"),
                           ("class", "Row states the class")):
            tr.steps.append(Step(key, label, "not reached", "blocked"))
        tr.reason = "This insurer publishes no provider list, so no hospital may be named."
        return tr

    tr.steps.append(Step("list", "Publishes a list",
                         f"{len(cities)} city files", "passed", count=len(cities)))

    # Gate 3 — is there a table for this city?
    table = btools._table_file(carrier, city)
    if table is None:
        tr.steps.append(Step("city", "City file exists",
                             f"no file for {(city or 'this city').title()}", "failed"))
        tr.steps.append(Step("class", "Row states the class", "not reached", "blocked"))
        tr.reason = (f"This insurer publishes no table for {city}, so no hospital "
                     "may be named.")
        return tr

    tr.steps.append(Step("city", "City file exists", table.name, "passed"))

    # Gate 4 — is the class one the tables can express?
    cls = (class_level or "").strip().upper().replace("CLASS", "").strip()
    valid = {"A", "A+", "B", "B+", "C", "C+", "D", "E", "VIP", "VVIP"}
    if cls not in valid:
        tr.steps.append(Step("class", "Row states the class",
                             "class not recognised", "failed"))
        tr.reason = "The class on the card is unknown, so no hospital may be named."
        return tr

    # Gate 5 — does a row actually state this class?
    result = btools.search_hospitals(carrier, city, class_level)
    rows = btools._parse_table(table.read_text(encoding="utf-8"))
    matched = [r for r in rows if btools._row_allows_class(r, cls)]

    if not result.may_name or not result.hospitals:
        tr.steps.append(Step("class", "Row states the class",
                             f"0 of {len(rows)} rows", "failed"))
        tr.reason = result.reason
        return tr

    tr.steps.append(Step("class", "Row states the class",
                         f"{len(matched)} of {len(rows)} rows", "passed",
                         count=len(matched)))

    tr.hospitals = result.hospitals
    tr.reason = result.reason
    tr.may_name = True
    return tr
