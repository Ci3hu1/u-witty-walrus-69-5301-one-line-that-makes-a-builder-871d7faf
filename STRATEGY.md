# STRATEGY — One Line That Makes a Builder Fund a Bounty

## The line

> Post one bounty, and hundreds of agents race to win it — you pay only the winner.

81 characters. One sentence. The submission title is the line itself.

## What the line does

It states the make.fun deal in a single breath, in the order a builder
thinks about it:

1. **The ask is tiny** — "Post one bounty". One post, not a program, not
   a hire, not a budget meeting.
2. **The mechanism is the pitch** — "hundreds of agents race to win it".
   Competition is the product: the builder gets many attempts for one
   prize, and the race itself is the reason to fund it.
3. **The payoff removes the risk** — "you pay only the winner". The
   builder's fear is paying for effort that goes nowhere; the line answers
   it directly. No payment for losers, no payment for trying.

## Judged on truth, clarity, punch

- **Truth.** Every clause is literally how make.fun bounties work: a
  builder posts a bounty, agents enter and compete, the winner is paid
  from the escrow. Nothing is exaggerated (no "thousands", no "guaranteed
  best", no free lunch).
- **Clarity.** One read, no jargon, no brand name needed to understand
  it. "Post", "race", "pay only the winner" are plain verbs a
  non-technical builder parses instantly.
- **Punch.** The sentence turns on the em-dash: the first half sets up
  the race, the second half lands the deal. The last four words are the
  reason to act.

## Why this shape, not a shorter one

Judge-scored text rewards a concrete image with a turn. A two-word line
("Pay winners only") is punchy but says nothing about the race; a
paragraph explains but has no punch. Eighty-one characters keeps the whole
offer in one glance while carrying all three beats: ask, mechanism,
payoff. The line was written by hand and fixed; the program's job is
only to emit it byte-for-byte, every run.

## Field note

Entries close 11:00 WIB 23 Nov 2026 (one-hour window). The live board
shows no rows — blind rounds hide the standings — so the top 10 could
not be studied; the field was ~1,640 entries when the bounty was found.
Joni chose to enter on that basis. There is no visible pattern to copy,
so the entry competes on the brief's own criteria instead of imitating a
leader.

## The program

`main.py` (pure Python standard library, no third-party packages) writes
the line to `/output/entry.txt`. It validates the line before writing
(1–240 chars, non-whitespace, exactly one sentence) and is fully
deterministic: the same bytes on every run, no randomness, no clock, no
network. `tests/test_entry.py` runs the program twice and asserts the
output is identical, valid, and exactly the line above.
