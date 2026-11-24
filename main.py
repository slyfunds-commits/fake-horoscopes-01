#!/usr/bin/env python3
"""Fake Horoscopes R1 — "The Family Summary".

Writes the keeper horoscope to /output/entry.txt and verifies it.
Keeper (133 chars, 133 bytes, no trailing newline):
"The stars say your family will ask you to summarise the group chat this week. 40,000 messages. The summary is 'we are still arguing'."

Reversal test: "we are still arguing" redefines the 40,000 messages — not a
conversation, a single unresolved argument. The reader completes the last step;
the line never narrates its own ending.
"""
import os

ENTRY = "The stars say your family will ask you to summarise the group chat this week. 40,000 messages. The summary is 'we are still arguing'."


def main():
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, f"gate: {len(ENTRY)} chars, need 1-200"
    assert ENTRY.strip(), "gate: entry is only whitespace"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    assert back == data, "byte verification failed"
    # Derived-length check: the written bytes must equal the entry's own length,
    # so a future edit to ENTRY cannot silently drift out of the gate.
    assert len(back) == len(ENTRY.encode("utf-8")), "length drift"
    assert not back.endswith(b"\n"), "no trailing newline"
    print(f"wrote /output/entry.txt: {len(ENTRY)} chars, {len(back)} bytes")


if __name__ == "__main__":
    main()
