#!/usr/bin/env python3
"""One-star review of something essential: socks and the dryer.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3 stdlib only, no network, deterministic, binary write with no
trailing newline. Only the output file is chmodded (0644); the output
directory itself is never touched or removed.
"""

import os
import sys

ENTRY_TEXT = (
    "One star. Socks disappear one at a time, never in pairs, "
    "and the dryer has maintained its innocence for ten years."
)
MIN_LENGTH = 1
MAX_LENGTH = 160
OUTPUT_FILENAME = "entry.txt"
OUTPUT_FILE_MODE = 0o644
DEFAULT_OUTPUT_DIR = "/output"


def validate(text):
    """Reject anything outside the contest gate: 1-160 chars, non-blank,
    no newline or carriage return."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must not contain a newline or carriage return")
    return text


def main():
    text = validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, OUTPUT_FILE_MODE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
