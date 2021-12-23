#!/usr/bin/env python3
""" 2021/20: Trench Map """

import sys

rule, image = sys.stdin.read().strip().split("\n\n")

assert len(rule) == 512
assert rule[0] == "#"
assert rule[-1] == "."

p = set(
    (x, y)
        for y, ln in enumerate(image.split())
        for x, c in enumerate(ln)
        if c == "#"
)

for r in range(1, 50 + 1):
    pp = set()

    # In odd-numbered steps, we only track the cells that turn off because an
    # infinite number turn on. In even-numbered steps, we only track the cells
    # that turn on because an infinite number turn off.
    t = "." if r % 2 else "#"

    min_x, *_, max_x = sorted(x for (x, y) in p)
    min_y, *_, max_y = sorted(y for (x, y) in p)
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            n = sum(
                x*pow(2, i)
                    for i, x in enumerate(
                        (x + dx, y + dy) in p if r % 2 else (x + dx, y + dy) not in p
                            for dy in [1, 0, -1]
                            for dx in [1, 0, -1]
                    )
            )

            if rule[n] == t:
                pp.add((x, y))

    p = pp

    if r in { 2, 50 }:
        print("Part {}:".format({2: "1", 50: "2"}[r]),
            len(p)
        )
