#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for a missed deadline
to /output/entry.txt. Python standard library only; deterministic:
the same fixed line every run.
"""

import os
import sys

LINE = (
    "I set five alarms for the deadline and they all went off at once, "
    "so I assumed it was a fire drill and evacuated the building."
)


def validate_line(line: str) -> None:
    """Validate the entry line before it is written.

    The bounty requires exactly one line: 1-200 characters, a single
    line with no newline characters inside it, and not only whitespace.
    Exit with a clear error message if any check fails.
    """
    if not line.strip():
        print("error: entry line must not be blank or only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line (no newline characters)", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(line) <= 200:
        print(
            f"error: entry line must be 1-200 characters, got {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
