#!/usr/bin/env python3
"""The Worst Pizza Topping: write one funny pitch line to /output/entry.txt.

The program is deterministic: no randomness, no network, no clock. The
line is a single sentence of at most 200 characters.
"""

import os

LINE = "Our new pizza is topped with unsent apology texts: cold, hard to swallow, and best served to someone you ghosted."


def check(line: str) -> None:
    if not line.strip():
        raise SystemExit("entry must not be empty")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be one line with no newline characters")


def main() -> None:
    check(LINE)
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != LINE:
        raise SystemExit("written file does not match the entry line")


if __name__ == "__main__":
    main()
