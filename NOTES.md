# NOTES — u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf

## Entry

- Competition: One Line That Makes a Builder Fund a Bounty ($5: 1st $2, 2nd $2, 3rd $1), free entry.
- Opens 10:00 WIB, closes 11:00 WIB 23 Nov 2026 (one-hour window). Final phase 11:00–12:00 WIB.
- The line (81 chars, one sentence): "Post one bounty, and hundreds of agents race to win it — you pay only the winner."
- Submission title is the line itself.
- Program: `main.py`, pure Python stdlib, writes the line to `/output/entry.txt`. Deterministic (identical bytes on repeat runs).

## Field

- Live board shows no rows (blind rounds hide standings); top 10 could not be studied. Field was ~1,640 entries when the bounty was found. Joni chose to enter on that basis.
- Quota at build: day cap 5 left, hard limit 40 left, can_submit true, entries_made 0.

## Build

- Fresh kit downloaded 23 Nov ~10:31 WIB. Kit `init` created LICENSE (MIT, SPDX line) + anchor commit.
- `main.py`, `STRATEGY.md`, `tests/test_entry.py`, `README.md` (template badges, owner/repo/referral filled), `NOTES.md` written in the build session.
- Tests: `python3 -m unittest discover -s tests -v` — all pass (line length/sentence, exact output, determinism over two runs).
- Kit check: ok=true, failed=[] (bundle: ~/workspace/tools/makefun/bundles/walrus-bundle.tar.gz).
- NOT submitted — awaiting Joni's Setuju on the exact entry.

## Live score

- (filled after submit)
