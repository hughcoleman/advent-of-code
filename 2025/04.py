#!/usr/bin/env python3
""" 2025/04: Printing Department """

import itertools as it
import sys

rolls = set(
    (r, c) for r, ln in enumerate(iter(sys.stdin.readline, ""))
           for c, ch in enumerate(ln.strip())
           if ch == "@"
)

def removable(R):
    return set(
        (x, y) for (x, y) in R
            if sum(
                (x + dx, y + dy) in R
                    for dx, dy in it.product((-1, 0, 1), repeat=2)
            ) <= 4
    )

print("Part 1:", len(removable(rolls)))

i = it.accumulate(it.repeat(None), lambda R, _: R - removable(R), initial=rolls)
u = next(t for t, t1 in it.pairwise(i) if t == t1)
print("Part 2:", len(rolls - u))
