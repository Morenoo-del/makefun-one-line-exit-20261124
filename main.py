#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes exactly one line to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

ENTRY = (
    "I hereby resign, effective immediately: after five years, "
    "the vending machine knows my name and my manager still doesn't."
)


def main() -> None:
    # Enforce the bounty gate before writing: one line, 1-140 chars.
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry is {len(line)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
