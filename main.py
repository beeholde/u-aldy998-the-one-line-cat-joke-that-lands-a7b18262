#!/usr/bin/env python3
"""One-line cat joke entry for make.fun (v2).

Writes a single cat joke, one line under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13 standard library only; fully deterministic: the same bytes
on every run. No network, no randomness, no input files.

The joke: warm-seat theft. Round 1 showed the kneading/dough angle
(v1, rank 862/1243, ~0.447) landed as a gentle smile, not a laugh:
its turn ("I'm undercooked") is a soft pun. The Feed study of ~900
visible submissions confirmed the crowded clusters (keyboard
promotion, gravity audit, 3 a.m. landlord/rent, performance review,
dead-mouse gifts) and that warm-seat theft is near-empty -- one
"sat on the warm spot" line with a different turn. Setup (seat
stolen in two seconds) + turn (the cat treats it as HER meeting) +
kicker ("learn to knock"): the politeness inversion is the laugh,
the angle is fresh, it is economical and retellable. Self-judged
pairwise against the strongest visible R1 lines ("some crimes need
an audience", "promoted before I did", gravity-auditions at rank
863): the warm-seat line wins on freshness (criterion 3) with an
equal-or-better laugh line (criterion 2); the toilet-paper,
vacuum and chest/breakfast trials all lost to it, and the
Schrodinger candidate stays demoted as clever-only per the brief.
"""

import os

JOKE = (
    "I stand up for two seconds and my cat steals my warm seat "
    "\u2014 then looks at me like I interrupted her meeting and "
    "should really learn to knock."
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
