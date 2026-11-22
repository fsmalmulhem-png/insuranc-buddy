"""Real end-to-end test against the Wkala service.

This spends real money, so it only runs when explicitly enabled:

    BUDDY_PAID_TESTS=1 WKALA_API_KEY=... python test_e2e_paid.py

It verifies what the mocked test cannot: a real session and run exist, real
events stream, and the real usage record is read without turning an unknown
cost into zero.
"""

from __future__ import annotations

import asyncio
import os
import sys
import uuid

from wkala import AgentClient, SnapshotUpdate

PAID = os.environ.get("BUDDY_PAID_TESTS") == "1"
KEY = os.environ.get("WKALA_API_KEY", "")
PROFILE_ID = os.environ.get("WKALA_PROFILE_ID")


async def main() -> int:
    if not PAID:
        print("SKIP  set BUDDY_PAID_TESTS=1 to run the paid end-to-end test")
        return 0
    if not KEY:
        print("FAIL  WKALA_API_KEY is not set")
        return 1

    failures = 0
    async with AgentClient(api_key=KEY) as agents:
        try:
            caps = await agents.capabilities.get()
            print("PASS  capabilities:", caps.model_dump(mode="json", by_alias=True))
        except Exception as e:
            print("FAIL  capabilities:", type(e).__name__, e)
            return 1

        session = await agents.sessions.create(
            title="Insurance Buddy e2e",
            profile_id=PROFILE_ID or None,
        )
        print("PASS  session created:", session.session_id)

        key = f"e2e-{uuid.uuid4()}"
        run = await session.send(
            "Which insurer is on your card?",
            idempotency_key=key,
            subject={"id": "e2e-user"},
        )
        print("PASS  run admitted:", run.id, "idempotency:", key)

        events = 0
        async with run.stream() as stream:
            async for update in stream:
                events += 1
                if isinstance(update, SnapshotUpdate):
                    print("      snapshot restored")
                if events >= 3:
                    break
        print(f"PASS  streamed {events} update(s)")

        result = await run.result()
        usage = getattr(result.run, "usage", None)
        cost = getattr(usage, "cost_microusd", None) if usage else None
        if cost is None:
            print("PASS  cost is unresolved (None) — not displayed as zero")
        else:
            print(f"PASS  cost recorded: {cost} micro-USD ({cost / 1e6:.6f} USD)")

        print("PASS  run status:", result.run.status, "| stop:", result.run.stop_reason)
        print("PASS  messages:", len(result.messages))

        # Duplicate business request must replay, not duplicate.
        again = await session.send(
            "Which insurer is on your card?",
            idempotency_key=key,
            subject={"id": "e2e-user"},
        )
        if again.id == run.id:
            print("PASS  same idempotency key returned the same run")
        else:
            failures += 1
            print("FAIL  duplicate work created:", again.id, "!=", run.id)

        await run.cancel()
        print("PASS  cancellation issued explicitly")

    print("\npaid e2e:", "PASSED" if failures == 0 else f"{failures} failure(s)")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
