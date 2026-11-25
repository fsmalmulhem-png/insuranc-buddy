"""Resolve a city the user typed to the slug the data uses.

The lookup used to be `slug(city) + ".md"` — exact match only. So "Khobar"
missed al-khobar, "الخبر" missed everything, and "Al Khubar" missed
al-khobar. The advisor looked unintelligent about names it plainly should know.

Layers, cheapest first:
  1. exact slug
  2. Arabic script names, matched through a normalised alias table
  3. common Latin spellings
  4. fuzzy match against the carrier's own city list (typos, transliteration)
  5. single substring match
  6. edit distance, for vowel drift such as hofuf / hafouf

If nothing matches, returns None. The caller then states it cannot confirm —
it does not guess, and it does not fall back to a different city.
"""

from __future__ import annotations

import difflib
import re

# Arabic city names -> the English slug used in the files.
ARABIC = {
    "الخبر": "al-khobar", "الخبراء": "al-khobar", "خبر": "al-khobar",
    "الرياض": "riyadh", "رياض": "riyadh",
    "جدة": "jeddah", "جده": "jeddah",
    "مكة": "makkah", "مكه": "makkah", "مكة المكرمة": "makkah",
    "المدينة": "madinah", "المدينه": "madinah", "المدينة المنورة": "madinah",
    "الدمام": "dammam", "دمام": "dammam",
    "الظهران": "dhahran", "ظهران": "dhahran",
    "الجبيل": "jubail", "جبيل": "jubail",
    "ينبع": "yanbu", "ينبع البحر": "yanbu-al-bahr", "ينبع الصناعية": "yanbu-industrial",
    "الطائف": "taif", "الطايف": "taif",
    "أبها": "abha", "ابها": "abha",
    "تبوك": "tabuk", "حائل": "hail", "نجران": "najran",
    "جيزان": "jazan", "جازان": "jazan",
    "الهفوف": "al-hafouf", "هفوف": "al-hafouf",
    "الأحساء": "al-ahsa", "الاحساء": "al-ahsa", "أحساء": "al-ahsa",
    "القطيف": "qatif", "سكاكا": "sakaka", "عرعر": "arar",
    "بريدة": "buraydah", "بريده": "buraydah", "عنيزة": "unaizah",
    "خميس مشيط": "khamis-mushait", "بيشة": "bisha",
    "الباحة": "al-baha", "سيهات": "saihat", "صفوى": "safwa",
    "الخفجي": "khafji", "حفر الباطن": "hafar-al-batin",
    "رابغ": "rabigh", "القنفذة": "qunfudah", "العلا": "al-ola",
    "الرس": "al-rass", "الزلفي": "zulfi",
    "المجمعة": "majmaah", "شقراء": "shaqra", "الدوادمي": "dawadmi",
    "وادي الدواسر": "wadi-al-dawaser", "أملج": "umluj", "املج": "umluj",
    "الوجه": "al-wajh", "ضباء": "dhiba", "رفحاء": "rafha",
    "طريف": "turaif", "القريات": "qurayat", "دومة الجندل": "dawamt-al-jandal",
    "بلجرشي": "baljurashi", "النماص": "al-namas", "تنومة": "tanomah",
    "الخرمة": "al-khorma", "المزاحمية": "muzahmiyah", "المذنب": "al-mithnab",
    "الخرج": "al-kharj", "الأفلاج": "al-aflaj", "البدائع": "badaya",
}

# Common Latin spellings, by convention. Keys are lowercase.
LATIN = {
    "khobar": "al-khobar", "khubar": "al-khobar", "al khubar": "al-khobar",
    "al-khubar": "al-khobar", "alkhobar": "al-khobar",
    "mecca": "makkah", "medina": "madinah",
    "hofuf": "al-hafouf", "hafouf": "al-hafouf", "hufuf": "al-hafouf",
    "al ahsa": "al-ahsa", "ahsa": "al-ahsa", "hasa": "al-ahsa",
    "ihsaa": "al-ahsa", "al hasa": "al-ahsa",
    "jazan": "jazan", "jizan": "jazan",
    "skaka": "sakaka", "sakakah": "sakaka",
    "buraidah": "buraydah", "bureidah": "buraydah",
    "unaizah": "unaizah", "onizah": "unaizah",
    "hafr al batin": "hafar-al-batin", "hafar al batin": "hafar-al-batin",
    "yanbu al bahr": "yanbu-al-bahr", "yanbu industrial": "yanbu-industrial",
}


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9\u0600-\u06FF]+", "-", (s or "").strip().lower()).strip("-")


def _fold_ar(s: str) -> str:
    """Fold Arabic orthography so spelling variants collide."""
    s = (s or "").strip().lower()
    s = re.sub("[إأآٱ]", "ا", s)
    s = s.replace("ة", "ه").replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي")
    s = re.sub("[\u064B-\u0652\u0640]", "", s)
    s = re.sub(r"^ال", "", s)
    return re.sub(r"[^a-z0-9\u0600-\u06FF]+", " ", s).strip()


def _fold_lat(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").strip().lower()).strip()


def resolve_city(typed: str, available: list[str]) -> str | None:
    """Best match for `typed` among the carrier's own city slugs."""
    if not typed or not available:
        return None
    raw = typed.strip()

    # 1. exact
    slug = _slug(raw)
    if slug in available:
        return slug

    # 2. Arabic table
    if re.search(r"[\u0600-\u06FF]", raw):
        key = _fold_ar(raw)
        for arabic, target in ARABIC.items():
            if _fold_ar(arabic) == key and target in available:
                return target
        folded_keys = {_fold_ar(k): v for k, v in ARABIC.items()}
        close = difflib.get_close_matches(key, list(folded_keys), n=1, cutoff=0.8)
        if close and folded_keys[close[0]] in available:
            return folded_keys[close[0]]

    # 3. Latin convention table, exact then near
    for candidate in (_fold_lat(raw), _fold_lat(raw.replace("-", " "))):
        target = LATIN.get(candidate)
        if target and target in available:
            return target
    for candidate in (_fold_lat(raw), _fold_lat(raw.replace("-", " "))):
        close_key = difflib.get_close_matches(candidate, list(LATIN), n=1, cutoff=0.85)
        if close_key and LATIN[close_key[0]] in available:
            return LATIN[close_key[0]]

    # 4. fuzzy against the carrier's own cities
    flat = _fold_lat(raw)
    if flat:
        hyphenated = flat.replace(" ", "-")
        close = difflib.get_close_matches(hyphenated, available, n=1, cutoff=0.82)
        if close:
            return close[0]
        compact = [c for c in available
                   if c.replace("-", "") == hyphenated.replace("-", "")]
        if len(compact) == 1:
            return compact[0]

    # 5. single substring hit
    hyphenated = _fold_lat(raw).replace(" ", "-")
    if len(hyphenated) >= 4:
        hits = [c for c in available if hyphenated in c or c in hyphenated]
        if len(hits) == 1:
            return hits[0]

    # 6. edit distance, for vowel drift such as hofuf / hafouf
    if len(hyphenated) >= 4:
        best, score = None, 0.0
        for cand in available:
            ratio = difflib.SequenceMatcher(None, hyphenated, cand).ratio()
            if ratio > score:
                best, score = cand, ratio
        if best and score >= 0.72:
            return best

    return None
