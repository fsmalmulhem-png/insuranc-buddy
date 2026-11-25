"""Fast answer path for Insurance Buddy."""

from __future__ import annotations

import re
from dataclasses import dataclass

import business_tools

CITIES = [
    "riyadh", "jeddah", "makkah", "mecca", "madinah", "medina", "dammam",
    "khobar", "al khobar", "al-khobar", "alkhobar", "khubar", "al khubar",
    "al-khubar", "alkhubar", "dhahran", "jubail", "yanbu", "taif",
    "abha", "tabuk", "buraydah", "buraidah", "hail", "najran", "jazan",
    "jizan", "hofuf", "al ahsa", "ahsa", "qatif", "sakaka", "arar", "bisha",
    "khamis mushait", "khurais", "unaizah", "qassim", "bahah", "jouf",
]
CITY_NORMAL = {
    "mecca": "makkah", "medina": "madinah",
    "khobar": "al-khobar", "al khobar": "al-khobar",
    "alkhobar": "al-khobar", "khubar": "al-khobar",
    "al khubar": "al-khobar", "al-khubar": "al-khobar",
    "alkhubar": "al-khobar",
    "buraidah": "buraydah", "jizan": "jazan",
    "al ahsa": "hofuf", "ahsa": "hofuf", "qassim": "buraydah",
}

EMERGENCY = [
    "chest pain", "heart attack", "can't breathe", "cannot breathe",
    "breathing", "bleeding", "unconscious", "fainted", "seizure",
    "stroke", "pregnant", "accident", "emergency", "urgent",
]
UNWELL = [
    "sick", "ill", "unwell", "not feeling well", "hurts", "pain",
    "fever", "tired", "dizzy", "nausea",
]

SYMPATHY = "I am sorry you are feeling unwell."
DISCLAIMER = "Coverage changes; confirm before you travel."


@dataclass
class Reply:
    kind: str
    text: str = ""
    reason: str = ""


def _norm_city(word: str) -> str:
    return CITY_NORMAL.get(word, word)


def find_city(text: str) -> str | None:
    t = text.lower()
    for city in sorted(CITIES, key=len, reverse=True):
        if re.search(r"\b" + re.escape(city) + r"\b", t):
            return _norm_city(city)
    return None


def find_class(text: str) -> str | None:
    t = text.upper().strip()
    m = re.search(r"\bCLASS\s*([A-E])\s*(\+)?", t)
    if m:
        return m.group(1) + (m.group(2) or "")
    m = re.search(r"\b(VVIP|VIP)\b", t)
    if m:
        return m.group(1)
    m = re.search(r"\b([A-E])(\+)\b", t)
    if m:
        return m.group(1) + m.group(2)
    if re.fullmatch(r"[A-E]\+?", t.rstrip(".!")):
        return t.rstrip(".!")
    return None


def is_emergency(text: str) -> bool:
    t = text.lower()
    return any(w in t for w in EMERGENCY)


def wants_emergency_care(text: str) -> bool:
    t = text.lower()
    return "emergency" in t or "urgent" in t


LOOKUP_WORDS = [
    "hospital", "clinic", "centre", "center", "polyclinic", "doctor",
    "specialist", "dentist", "optical", "pharmacy",
    "accept", "covered", "coverage", "reimburse",
    "near me", "where can i go", "which hospital",
]

SICK_WORDS = [
    "sick", "ill", "unwell", "not feeling well", "hurts", "pain",
    "fever", "dizzy", "nausea", "emergency", "urgent",
]

SMALL_TALK = [
    "hello", "hi", "hey", "salam", "thanks", "thank you", "good morning",
    "good evening", "who are you", "what can you do", "help",
]

QUESTION_SHAPES = (
    "what is ", "what's ", "what does ", "what do ", "what are ",
    "meaning of", "explain ", "how does ", "how do ", "why is ",
    "why do ", "tell me about",
)


def _asked_for_a_fact(text: str) -> bool:
    """Did the assistant's previous reply ask for insurer / class / city?"""
    t = (text or "").lower()
    return ("which insurer" in t or "what class" in t
            or "which city" in t or "printed on" in t)


def is_not_a_lookup(message: str, history: list[dict] | None = None) -> bool:
    """True when the message is not a hospital lookup."""
    text = (message or "").strip()
    if not text:
        return True
    t = text.lower()

    # A general question is never a lookup, even when it mentions a class:
    # "what is class A" is a question to answer, not a fact to collect.
    if any(t.startswith(sh) or (" " + sh) in t for sh in QUESTION_SHAPES):
        return True

    # A greeting overrides the check below, otherwise one asked question makes
    # every later message look like the answer to it.
    bare = t.strip().strip(".!,")
    if any(bare == w or t.startswith(w + " ") or t.startswith(w + ",")
           for w in SMALL_TALK):
        return True

    # A bare answer to the question the advisor just asked is a lookup step.
    last_assistant = ""
    for m in reversed(history or []):
        if m.get("role") == "assistant":
            last_assistant = m.get("content", "")
            break
    if _asked_for_a_fact(last_assistant):
        return False

    if business_tools.find_carrier(text) or find_city(text) or find_class(text):
        return False

    if any(w in t for w in SICK_WORDS):
        return True
    if any(w in t for w in LOOKUP_WORDS):
        return False

    return True


PRETTY = {
    "gig-gulf-insurance-saudi-network": "GIG",
    "ggi-gulf-general-saudi-network": "Gulf General",
    "aicc-arabia-insurance-saudi-network": "Arabia Insurance",
    "acig-saudi-network": "ACIG",
    "bupa-saudi-network": "Bupa",
    "amana-coop-saudi-network": "Amana",
    "tawuniya-saudi-network": "Tawuniya",
    "medgulf-saudi-network": "MEDGULF",
    "saudi-enaya-saudi-network": "Saudi Enaya",
    "uca-united-cooperative-saudi-network": "UCA",
    "wataniya-saudi-network": "Wataniya",
    "walaa-saudi-network": "Walaa",
    "malath-saudi-network": "Malath",
    "salama-iaic-saudi-network": "Salama",
    "saico-saudi-network": "SAICO",
    "chubb-saudi-network": "Chubb",
    "buruj-saudi-network": "Buruj",
    "liva-insurance-saudi-network": "Liva",
    "al-etihad-saudi-network": "Al Etihad",
    "aljazira-takaful-saudi-network": "Aljazira Takaful",
    "alrajhi-takaful-saudi-network": "Al Rajhi Takaful",
    "alsagr-saudi-network": "Al Sagr",
    "arabian-shield-saudi-network": "Arabian Shield",
    "gulf-union-saudi-network": "Gulf Union",
    "integrated-insurance-broker-saudi-network": "your broker",
}


def _label(carrier: str) -> str:
    return PRETTY.get(carrier, carrier.replace("-saudi-network", "").replace("-", " ").title())


def _fmt(h) -> str:
    bits = [h.name]
    if h.phone:
        bits.append(h.phone)
    return " — ".join(bits)


def respond(message: str, history: list[dict] | None = None,
            carrier: str | None = None, city: str | None = None,
            class_level: str | None = None) -> Reply:
    """Answer from the tables when possible; return kind='model' otherwise."""
    history = history or []
    text = message.strip()
    if not text:
        return Reply("ask", "Which insurer is on your card?")

    if not carrier:
        carrier = business_tools.find_carrier(text)
    if not carrier:
        for m in reversed(history):
            if m.get("role") == "user":
                carrier = business_tools.find_carrier(m.get("content", ""))
                if carrier:
                    break
    if not city:
        city = find_city(text)
        if not city:
            for m in reversed(history):
                if m.get("role") == "user":
                    city = find_city(m.get("content", ""))
                    if city:
                        break
    if not class_level:
        class_level = find_class(text)
        if not class_level:
            for m in reversed(history):
                if m.get("role") == "user":
                    class_level = find_class(m.get("content", ""))
                    if class_level:
                        break

    emergency = is_emergency(text)
    lead = ("If this is an emergency, call 997 now — do not wait for me.\n\n"
            if emergency else "")

    if carrier:
        summary = business_tools.carrier_summary(carrier)
        if not summary["publishes_provider_list"]:
            name = _label(carrier)
            where = f" in {city.title()}" if city else ""
            klass = f" Class {class_level}" if class_level else ""
            return Reply(
                "answer",
                f"{lead}I cannot confirm a hospital for {name}{klass}{where} — "
                "this insurer publishes no provider list.\n\n"
                f'Ask the hospital desk: "Do you bill {name}{klass} directly?"\n\n'
                f"{DISCLAIMER}",
            )

    if carrier and city and class_level:
        res = business_tools.search_hospitals(carrier, city, class_level)
        name = _label(carrier)
        if res.may_name and res.hospitals:
            lines = [f"{lead}Yes — {name} Class {class_level}, {city.title()}:", ""]
            for h in res.hospitals[:4]:
                lines.append("• " + _fmt(h))
            lines += ["", DISCLAIMER]
            return Reply("answer", "\n".join(lines))
        return Reply(
            "answer",
            f"{lead}I cannot confirm a Class {class_level} hospital for {name} "
            f"in {city.title()} — the published list does not tie one to your "
            "class.\n\n"
            f'Ask the hospital desk: "Do you bill {name} Class {class_level} '
            'directly?"\n\n'
            f"{DISCLAIMER}",
        )

    if is_not_a_lookup(text, history):
        return Reply("model", reason="not a lookup — answer from the prompt")

    if not carrier:
        warm = ""
        if not lead and any(w in text.lower() for w in UNWELL):
            warm = SYMPATHY + " "
        return Reply("ask", f"{lead}{warm}Which insurer is on your card?")
    if not class_level:
        return Reply("ask", "What class is printed on it — A or B?")
    if not city:
        return Reply("ask", "Which city are you in?")

    return Reply("model", reason="tables could not settle this")


def prefetch_warm() -> None:
    """Touch the tables so the first real request is not the cold one."""
    try:
        for c in ("gig-gulf-insurance-saudi-network",
                  "bupa-saudi-network",
                  "amana-coop-saudi-network",
                  "ggi-gulf-general-saudi-network"):
            business_tools.published_cities(c)
    except Exception:
        pass
