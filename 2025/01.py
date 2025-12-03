#!/usr/bin/env python3
""" 2025/01: Secret Entrance """

import itertools as it
import sys

rotations = [
    (1 if ln[0] == "R" else -1)*int(ln[1:])
        for ln in sys.stdin.readlines()
]

print("Part 1:", sum(
    p % 100 == 0
        for p in it.accumulate([50] + rotations)
))

p = 50
print("Part 2:", sum(
    (p + max(d, -1)) // 100 - (p + min(d, 1) - 1) // 100 + 0*(p := p + d)
        for d in rotations
))
