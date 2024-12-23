#!/usr/bin/env python3
""" 2024/13: Claw Contraption """

import re
import sys

machines = [
    tuple(map(int, re.findall(r"(\d+)", s)))
        for s in sys.stdin.read().strip().split("\n\n")
]

def solve(dx1, dy1, dx2, dy2, gx, gy):
    # We'll use Cramer's rule...
    d = dx1*dy2 - dx2*dy1
    assert d != 0

    A =  dy2 * gx - dx2 * gy
    B = -dy1 * gx + dx1 * gy
    if A % d == 0 and B % d == 0:
        return 3*(A // d) + B // d
    else:
        return 0

print("Part 1:", sum(solve(*m) for m in machines))
print("Part 2:", sum(solve(*m[:4], m[4] + 10000000000000, m[5] + 10000000000000) for m in machines))
