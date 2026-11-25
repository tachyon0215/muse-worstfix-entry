#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Worst Fix Ever: Funniest Commit Message": Reads exactly like a plain, tired commit subject, and the irony is specific to a repair: the 'fix' deleted a mere comment and the comment turned out to be load-bearing - a fresh angle away from the worn revert and test-in-production jokes.
Deterministic: a fixed text, no network, no randomness, no clock.
This is a make.fun sprint entry.
"""
import os
from pathlib import Path

LINE = 'fix: remove the one comment that was apparently holding the whole system together'
TEXT = LINE + "\n"
MAX_CHARS = 100
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
