"""Tests for the carrier detection in app.py. Run: python test_app.py"""

import re

# Mirrors CARRIERS in app.py
from business_tools import find_carrier

CASES = [
    ("I have Bupa Class B", "bupa-saudi-network"),
    ("my card says Tawuniya", "tawuniya-saudi-network"),
    ("I am with GIG", "gig-gulf-insurance-saudi-network"),
    ("Arabia Insurance class B", "aicc-arabia-insurance-saudi-network"),
    ("Al Rajhi Takaful", "alrajhi-takaful-saudi-network"),
    ("MedGulf please", "medgulf-saudi-network"),
    ("Gulf General", "ggi-gulf-general-saudi-network"),
    ("UCA", "uca-united-cooperative-saudi-network"),
    ("Walaa", "walaa-saudi-network"),
    ("Wataniya", "wataniya-saudi-network"),
    ("Saudi Enaya Class A", "saudi-enaya-saudi-network"),
    ("Malath", "malath-saudi-network"),
    ("Liva", "liva-insurance-saudi-network"),
    ("Salama", "salama-iaic-saudi-network"),
    ("SAICO", "saico-saudi-network"),
    ("Gulf Union", "gulf-union-saudi-network"),
    ("Buruj", "buruj-saudi-network"),
    ("Chubb", "chubb-saudi-network"),
    ("Amana", "amana-coop-saudi-network"),
    ("Al Sagr", "alsagr-saudi-network"),
    ("Al Etihad", "al-etihad-saudi-network"),
    ("Arabian Shield", "arabian-shield-saudi-network"),
    ("ACIG", "acig-saudi-network"),
    ("Aljazira Takaful", "aljazira-takaful-saudi-network"),
    # no carrier named — must stay None
    ("I am sick and I dont know which hospital to go to", None),
    ("which hospital can I use", None),
    ("yes", None),
    ("Class B in Riyadh", None),
]

if __name__ == "__main__":
    bad = 0
    for text, want in CASES:
        got = find_carrier(text)
        ok = got == want
        if not ok:
            bad += 1
        print(("OK  " if ok else "FAIL"), repr(text), "->", got, "(want", want, ")")
    print(f"\n{len(CASES) - bad}/{len(CASES)} passed")
    raise SystemExit(1 if bad else 0)
