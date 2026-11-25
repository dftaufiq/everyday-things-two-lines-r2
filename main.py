#!/usr/bin/env python3
"""Everyday Things, Two Lines (round 2) -- a fridge as a little winter.

Writes the two-line explanation to /output/entry.txt. The gate requires
UTF-8 text of 1 to 400 characters; the entry below is 377 characters
(378 bytes with the trailing newline).

Line 1 explains a fridge to a 10-year-old in one vivid sentence built on
a single analogy (a little winter living in the kitchen), with the reveal
in its final clause: the back of the fridge feels WARM while the ice
cream inside sits at minus eighteen degrees. That paradox is the click:
a fridge does not make cold, it moves heat out of your food and hides
it out the back. Line 2 says in one sentence what the analogy maps
(heat moved out, not cold made) and what it leaves out (real winter
cools the whole street; a fridge warms your kitchen a little).
"""

import os

LINE1 = (
    "A fridge is a little winter that lives in your kitchen: it steals "
    "the heat out of your food and hides it out the back, so the back "
    "feels warm while your ice cream sits at minus eighteen degrees inside."
)
LINE2 = (
    "It maps how a fridge moves heat out of your food instead of making "
    "cold, but it leaves out that real winter cools the whole street, "
    "while a fridge warms your kitchen a little."
)

ENTRY = LINE1 + "\n" + LINE2 + "\n"


def main():
    # The gate refuses anything outside 1-400 characters, so fail loudly
    # here instead of shipping an entry the judge never sees.
    body = ENTRY.rstrip("\n")
    assert 1 <= len(body) <= 400, f"entry is {len(body)} chars, gate is 1-400"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
