"""LLM key and client handling.

The key is read in this order:
  1. what the user typed into the sidebar this session (only if there is no
     server-side key — a deployment sets one and the field never appears)
  2. Streamlit secrets  (st.secrets["OPENAI_API_KEY"])
  3. environment variable OPENAI_API_KEY

It is never written to disk, never logged, and never put in a URL. Only the last
four characters are ever displayed, so a screenshot cannot leak it.

The provider is pinned by LLM_PROVIDER, so a deployment needs no sidebar at all.
DeepSeek is OpenAI-compatible, so the same `openai` client works with a
different base_url.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

PROVIDERS = {
    "deepseek": {
        "label": "DeepSeek",
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-chat",
        "key_env": "DEEPSEEK_API_KEY",
        "key_prefix": "sk-",
        "docs": "https://platform.deepseek.com/api_keys",
    },
    "openai": {
        "label": "OpenAI",
        "base_url": None,  # library default
        "model": "gpt-4o-mini",
        "key_env": "OPENAI_API_KEY",
        "key_prefix": "sk-",
        "docs": "https://platform.openai.com/api-keys",
    },
}

# The provider can be pinned from the environment, so a deployment needs no
# sidebar at all. LLM_PROVIDER=openai + OPENAI_API_KEY is enough.
_ENV_PROVIDER = (os.environ.get("LLM_PROVIDER") or "").strip().lower()
DEFAULT_PROVIDER = _ENV_PROVIDER if _ENV_PROVIDER in PROVIDERS else "deepseek"


@dataclass
class KeyStatus:
    present: bool
    source: str          # typed | secrets | env | none
    provider: str
    model: str
    preview: str         # last 4 chars only, or ""


def _from_secrets(env_name: str) -> str | None:
    """Read from Streamlit secrets without exploding when there is no file."""
    try:
        import streamlit as st

        val = st.secrets.get(env_name)  # type: ignore[union-attr]
        if val:
            return str(val)
    except Exception:
        pass
    return None


def resolve_key(provider: str, typed: str | None) -> tuple[str | None, str]:
    """Return (key, source). Source is for display only — never the key."""
    if typed and typed.strip():
        return typed.strip(), "typed"
    env_name = PROVIDERS[provider]["key_env"]
    val = _from_secrets(env_name)
    if val:
        return val, "secrets"
    val = os.environ.get(env_name)
    if val:
        return val, "env"
    return None, "none"


def server_key_present() -> bool:
    """True when the deployment already has a usable key.

    The UI uses this to decide whether to ask the visitor for one at all.
    """
    provider = DEFAULT_PROVIDER
    key, _ = resolve_key(provider, None)
    return bool(key)


def status(provider: str, typed: str | None = None) -> KeyStatus:
    key, source = resolve_key(provider, typed)
    spec = PROVIDERS[provider]
    model = os.environ.get("LLM_MODEL") or spec["model"]
    preview = f"…{key[-4:]}" if key and len(key) >= 4 else ""
    return KeyStatus(
        present=bool(key), source=source, provider=provider,
        model=model, preview=preview,
    )


def looks_valid(provider: str, key: str) -> tuple[bool, str]:
    """Cheap local check. Real validity is only proven by a live call."""
    spec = PROVIDERS[provider]
    key = (key or "").strip()
    if not key:
        return False, "No key entered."
    if not key.startswith(spec["key_prefix"]):
        return False, f"{spec['label']} keys start with '{spec['key_prefix']}'."
    if len(key) < 20:
        return False, "That looks too short to be a key."
    if any(c.isspace() for c in key):
        return False, "The key contains a space — check the paste."
    return True, "Format looks right."


def build_client(provider: str, typed: str | None = None):
    """Return an OpenAI-compatible client, or raise with a readable message."""
    from openai import OpenAI

    key, source = resolve_key(provider, typed)
    if not key:
        raise RuntimeError(
            f"No {PROVIDERS[provider]['label']} API key. Paste one in the sidebar, "
            f"or set {PROVIDERS[provider]['key_env']}."
        )
    spec = PROVIDERS[provider]
    return OpenAI(
        [REDACTED CREDENTIAL]
        base_url=os.environ.get("LLM_BASE_URL") or spec["base_url"],
        timeout=30.0,
        max_retries=1,
    )


def model_name(provider: str) -> str:
    return os.environ.get("LLM_MODEL") or PROVIDERS[provider]["model"]


def check_live(provider: str, typed: str | None = None) -> tuple[bool, str]:
    """One tiny real call. Proves the key, the endpoint and the model name.

    Returns (ok, message). The message never contains the key.
    """
    try:
        client = build_client(provider, typed)
    except RuntimeError as e:
        return False, str(e)

    try:
        r = client.chat.completions.create(
            model=model_name(provider),
            messages=[{"role": "user", "content": "Reply with the single word: ok"}],
            temperature=0,
            max_tokens=8,
        )
        text = (r.choices[0].message.content or "").strip()
        return True, f"Key works. Model replied {text[:20]!r}."
    except Exception as e:  # noqa: BLE001 - surface the provider's message
        name = type(e).__name__
        msg = str(e)
        for scrub in ("api_key", "Authorization"):
            if scrub.lower() in msg.lower() and "Bearer" in msg:
                msg = "the key was rejected"
        return False, f"{name}: {msg[:200]}"
