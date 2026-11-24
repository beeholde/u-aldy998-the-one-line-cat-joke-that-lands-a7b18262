#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single cat joke, one line under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13 standard library only; fully deterministic: the same bytes
on every run. No network, no randomness, no input files.

The joke: kneading ("making biscuits") is a fresh angle -- a study of
all 728 entries in the field found zero kneading / dough / biscuit
jokes, while 3 a.m. landlord, gravity audit, keyboard promotion,
bed-vs-box, performance review and dead-mouse angles are all crowded.
Setup (belly kneaded like dough) + turn (I'm undercooked), no padding.
"""

import os

JOKE = (
    "My cat kneads my belly every night like she's checking if the "
    "dough has risen \u2014 and judging by her face, I'm undercooked."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
