#!/usr/bin/env python3
"""Tests for the one-line entry.

Pure standard library (unittest). Runs main.py twice and asserts:
- the output file is written, UTF-8, 1-240 chars, not only whitespace
- exactly one sentence
- the content is exactly the expected line
- the two runs are byte-identical (deterministic, per run_deterministic)
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_PY = os.path.join(REPO, "main.py")

EXPECTED = "Post one bounty, and hundreds of agents race to win it \u2014 you pay only the winner."


def run_entry(out_path):
    result = subprocess.run(
        [sys.executable, MAIN_PY, out_path],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


class TestOneLineEntry(unittest.TestCase):
    def test_line_is_one_sentence_and_within_limit(self):
        self.assertEqual(len(EXPECTED), 81)
        self.assertTrue(1 <= len(EXPECTED) <= 240)
        self.assertTrue(EXPECTED.strip())
        self.assertTrue(EXPECTED.endswith("."))
        self.assertNotIn(".", EXPECTED[:-1])
        self.assertNotIn("!", EXPECTED)
        self.assertNotIn("?", EXPECTED)

    def test_program_writes_exact_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            with open(out, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, EXPECTED)

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out1 = os.path.join(tmp, "a.txt")
            out2 = os.path.join(tmp, "b.txt")
            r1 = run_entry(out1)
            r2 = run_entry(out2)
            self.assertEqual(r1.returncode, 0, msg=r1.stderr)
            self.assertEqual(r2.returncode, 0, msg=r2.stderr)
            with open(out1, "rb") as f:
                b1 = f.read()
            with open(out2, "rb") as f:
                b2 = f.read()
            self.assertEqual(b1, b2)

    def test_default_output_path(self):
        # main.py with no argument targets /output/entry.txt; only check
        # the constant, not the write, so the suite never needs /output.
        source = open(MAIN_PY, encoding="utf-8").read()
        self.assertIn('DEFAULT_OUTPUT = "/output/entry.txt"', source)


if __name__ == "__main__":
    unittest.main()
