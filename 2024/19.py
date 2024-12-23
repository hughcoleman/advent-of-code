#!/usr/bin/env python3
""" 2024/19: Linen Layout """

import functools as ft
import sys

patterns, designs = sys.stdin.read().strip().split("\n\n")
patterns = patterns.split(", ")
designs = designs.split("\n")

@ft.cache
def solve(design):
    if len(design) == 0:
        return 1
    else:
        return sum(solve(design[len(pattern):]) for pattern in patterns if design.startswith(pattern))

solutions = [
    solve(design) for design in designs
]
print("Part 1:", sum(s > 0 for s in solutions))
print("Part 2:", sum(solutions))
