#!/usr/bin/env python3
"""Green Tests, Nothing Works — make.fun entry 276.

Writes one funny one-line excuse (1-140 chars, single line, UTF-8)
to /output/entry.txt. Pure stdlib, fully deterministic.
"""

import os

ENTRY = "Every test is green and the app is still broken \u2014 the tests only ever tested themselves."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(line: str) -> str:
    """Return the entry line, enforcing the contest rules (1 line, 1-140 chars)."""
    line = line.strip()
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry length {len(line)} out of 1-140"
    assert line, "entry must not be blank"
    return line


def main() -> None:
    line = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
