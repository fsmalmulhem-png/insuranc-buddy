"""Tests for the instant answer path. Run: python test_fast_answers.py"""

from __future__ import annotations

import time

import fast_answers as f

CASES = [
    # (message, history, expect_kind, must_contain, must_not_contain)
    ("I have GIG VIP in Riyadh, which hospital?",
     [], "answer", "AL DARA", None),
    ("Tawuniya Class B Alkhobar",
     [], "answer", "cannot confirm", "Hospital —"),
    ("Bupa Class A Riyadh",
     [], "answer", "cannot confirm", "Hospital —"),
    ("Amana Class B Jeddah",
     [], "answer", "cannot confirm", None),
    ("I am sick and I dont know which hospital to go to",
     [], "ask", "insurer", None),
    ("I have Bupa", [], "ask", "class", None),
    ("chest pain, GIG VIP Riyadh",
     [], "answer", "997", None),
    # fact carried across turns
    ("which one is closest?",
     [{"role": "user", "content": "GIG VIP Riyadh"}],
     "answer", "Riyadh", None),
    # Regression: "Alkhobar" (no hyphen) was not recognised, so the previous
    # city's hospitals were returned. Khobar files are named al-khobar.md.
    ("Yes, check Alkhobar.",
     [{"role": "user", "content": "I have GIG VIP in Riyadh, which hospital?"},
      {"role": "user", "content": "I am going to Alkhobar next week"}],
     "answer", "AL SALAM", "riyadh"),
    ("Al Khubar please",
     [{"role": "user", "content": "GIG VIP"}],
     "answer", "KHOBAR", None),
    # Regression: Tawuniya was recorded as publishing no data. A policy
    # holder's app PDF proved otherwise. Class A must answer; Class B must not
    # borrow Class A's list.
    ("I have Tawuniya Class A in Riyadh, which hospital?",
     [], "answer", "CLINIC", None),
    ("I have Tawuniya Class B in Riyadh",
     [], "answer", "cannot confirm", "CLINIC"),
]


def main() -> int:
    f.prefetch_warm()
    bad = 0
    slow = []
    for msg, hist, kind, want, forbidden in CASES:
        t0 = time.perf_counter()
        r = f.respond(msg, hist)
        ms = (time.perf_counter() - t0) * 1000
        ok = r.kind == kind and want.lower() in r.text.lower()
        if forbidden and forbidden.lower() in r.text.lower():
            ok = False
        if ms > 50:
            slow.append((msg, ms))
        if not ok:
            bad += 1
        print(("OK  " if ok else "FAIL"), f"{ms:6.2f} ms", f"[{r.kind}]", repr(msg)[:52])

    print()
    if slow:
        print("SLOW (>50ms):", slow)
        bad += len(slow)
    print(f"{len(CASES) - bad}/{len(CASES)} passed")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
