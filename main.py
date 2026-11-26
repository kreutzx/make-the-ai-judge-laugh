#!/usr/bin/env python3
"""Entry for 'Make the AI Judge Laugh' (u-rama-melon-make-the-ai-judge-laugh-302d0825).

Writes one office-life joke, one line, to /output/entry.txt.
Stdlib only. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I hid in the fourth-floor stairwell for 47 minutes to dodge "
    "the 3 p.m. standup, and HR just booked it as my new office."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

    # Read it back and assert byte equality with what we intended to write.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "read-back mismatch"
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
