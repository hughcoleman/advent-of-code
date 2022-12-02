#!/usr/bin/env python3
""" 2022/02: Rock Paper Scissors """

import sys

guide = [
    ("ABC".index(ln[0]), "XYZ".index(ln[2]))
        for ln in sys.stdin.read().strip().split("\n") 
]

# Behold, magic formulas.
print("Part 1:", sum(3*((2*p1 + p2 + 1) % 3) + p2 + 1 for p1, p2 in guide))
print("Part 2:", sum((p1 + p2 - 1) % 3 + 1 + 3*p2 for p1, p2 in guide))
