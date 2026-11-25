#!/usr/bin/env python3
"""Entry program for the make.fun contest 'Worst Fix Ever: Funniest Commit Message'.

The joke was picked from three drafts against the contest's judge brief:
it had to read like a real commit subject, and the humour had to come from
the specific irony of a repair that broke more than it fixed. The winning
draft treats a deleted comment as load-bearing, which beat a typo-fix joke
and a warning-deletion joke. Running this program emits that one line.
"""

import os
import sys

ENTRY_TEXT = "fix: remove the one comment that was apparently holding the whole system together"
CHAR_LIMIT = 100


def check_text(text):
    if not text or not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError("entry text exceeds the character limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    return text


def emit(text, directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return target


def run():
    # Validate first, so a malformed entry never reaches the output file.
    text = check_text(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    emit(text, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(run())
