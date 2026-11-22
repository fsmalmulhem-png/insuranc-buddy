"""Tests for the LLM key handling. Run: python test_llm_config.py

Two groups:
  A. offline — format checks, precedence, redaction. No network, always run.
  B. live    — one real call. Skipped unless BUDDY_PAID_TESTS=1.

Nothing here prints or asserts on a real key. Only the last four characters
are allowed into output, and only from a fake key defined in this file.
"""

from __future__ import annotations

import os
import sys

import llm_config as L

FAKE = "sk-" + "a" * 32 + "zzzz"
RESULTS: list[tuple[bool, str]] = []


def check(ok: bool, label: str) -> None:
    RESULTS.append((ok, label))
    print(("PASS  " if ok else "FAIL  ") + label)


def group_a_offline() -> None:
    print("— A. offline checks —")
    # The checks below mutate and delete this var; keep the caller's value so
    # the live group still has a real key to use.
    saved_env = os.environ.get("DEEPSEEK_API_KEY")

    ok, _ = L.looks_valid("deepseek", FAKE)
    check(ok, "a well-formed key is accepted")

    ok, why = L.looks_valid("deepseek", "")
    check(not ok and "No key" in why, "empty key is rejected")

    ok, why = L.looks_valid("deepseek", "abc123")
    check(not ok and "sk-" in why, "wrong prefix is rejected")

    ok, why = L.looks_valid("deepseek", "sk-short")
    check(not ok and "short" in why, "short key is rejected")

    ok, why = L.looks_valid("deepseek", "sk-" + "a" * 20 + " b")
    check(not ok and "space" in why, "key with a space is rejected")

    # Precedence: a typed key beats the environment.
    os.environ["DEEPSEEK_API_KEY"] = "sk-" + "b" * 30 + "env1"
    key, source = L.resolve_key("deepseek", FAKE)
    check(key == FAKE and source == "typed", "typed key beats the env var")

    key, source = L.resolve_key("deepseek", "")
    check(source == "env" and key.endswith("env1"), "falls back to the env var")

    del os.environ["DEEPSEEK_API_KEY"]
    key, source = L.resolve_key("deepseek", None)
    check(key is None and source == "none", "reports 'none' when nothing is set")

    # Redaction: status must never contain the whole key.
    os.environ["DEEPSEEK_API_KEY"] = FAKE
    st = L.status("deepseek")
    blob = f"{st.source} {st.preview} {st.model}"
    check(FAKE not in blob, "status never contains the full key")
    check(st.preview == "…zzzz", "status shows only the last four characters")
    del os.environ["DEEPSEEK_API_KEY"]

    check(L.model_name("deepseek") == "deepseek-chat",
          "DeepSeek model defaults to deepseek-chat")
    check(L.PROVIDERS["deepseek"]["base_url"] == "https://api.deepseek.com",
          "DeepSeek base_url is set")

    # build_client with no key gives a readable error, not a traceback.
    try:
        L.build_client("deepseek", None)
        check(False, "build_client raises without a key")
    except RuntimeError as e:
        check("No DeepSeek API key" in str(e), "build_client raises a clear message")

    # A client can be constructed from a fake key without any network call.
    c = L.build_client("deepseek", FAKE)
    check(getattr(c, "base_url", None) is not None, "client builds from a typed key")

    # Restore whatever the caller provided.
    if saved_env:
        os.environ["DEEPSEEK_API_KEY"] = saved_env
    else:
        os.environ.pop("DEEPSEEK_API_KEY", None)


def group_b_live() -> None:
    print("— B. live call —")
    if os.environ.get("BUDDY_PAID_TESTS") != "1":
        print("SKIP  live call (set BUDDY_PAID_TESTS=1 to run)")
        return
    ok, msg = L.check_live("deepseek", None)
    # A 402 proves auth worked; it is not a key failure.
    balance = "402" in msg or "Insufficient" in msg
    if balance:
        print("NOTE  key authenticates but the account has no credit")
        check(True, "key reaches DeepSeek (402 = valid key, unpaid account)")
    else:
        check(ok, f"live call succeeded: {msg[:60]}")


def main() -> int:
    group_a_offline()
    group_b_live()
    failed = [lbl for ok, lbl in RESULTS if not ok]
    print()
    if failed:
        for lbl in failed:
            print("  failed:", lbl)
    print(f"{len(RESULTS) - len(failed)}/{len(RESULTS)} passed")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
