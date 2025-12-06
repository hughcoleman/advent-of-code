#!/usr/bin/env python3
""" 2025/06: Trash Compactor """

import math
import sys

problems = [
    list(ln) for ln in iter(sys.stdin.readline, "")
]

p1, p2 = 0, 0
cols = zip(*problems)
while (col := next(cols, None)):
    op = sum if col[-1] == '+' else math.prod

    # `n1` accumulates the "normal" problems, and `n2` accumulates the
    # "pivoted" problems.
    n1 = col[:-1]
    n2 = [
        ''.join(ch for ch in col if ch.isdigit())
    ]
    while (col := next(cols)) and not all(ch.isspace() for ch in col):
        n1 = [
            num + ch for num, ch in zip(n1, col)
        ]
        n2.append(''.join(ch for ch in col if ch.isdigit()))

    p1, p2 = p1 + op(map(int, n1)), p2 + op(map(int, n2))

print("Part 1:", p1)
print("Part 2:", p2)
