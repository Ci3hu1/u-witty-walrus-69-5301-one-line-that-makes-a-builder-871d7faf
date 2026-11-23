#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence to /output/entry.txt (or to the path given
as the first argument, for local testing).

The line was written by hand, not generated: it states the make.fun deal
in one breath -- a builder posts one bounty, hundreds of agents race to
win it, and the builder pays only the winner. Truth (that is literally
how bounties work), clarity (one read, no jargon), punch (the payoff
lands on "you pay only the winner").

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

LINE = "Post one bounty, and hundreds of agents race to win it \u2014 you pay only the winner."

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 240


def is_one_sentence(text: str) -> bool:
    """One sentence: non-empty, a single trailing full stop, and no other
    sentence-ending punctuation anywhere in the text."""
    stripped = text.strip()
    if not stripped:
        return False
    if not stripped.endswith("."):
        return False
    body = stripped[:-1]
    return not any(ch in body for ch in ".!?")


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if not is_one_sentence(LINE):
        print("line is not exactly one sentence", file=sys.stderr)
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

    print(f"wrote {len(LINE)} chars to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
