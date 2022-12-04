#!/usr/bin/env python3
""" 2022/04: Camp Cleanup """

import sys

assignments = [
    tuple(tuple(map(int, x.split("-"))) for x in ln.split(","))
        for ln in sys.stdin.read().strip().split("\n")
]
assignments = [
    (set(range(x1, x2 + 1)), set(range(y1, y2 + 1)))
        for ((x1, x2), (y1, y2)) in assignments
]

print("Part 1:", sum(
    X.issubset(Y) or Y.issubset(X) for X, Y in assignments
))
print("Part 2:", sum(
    len(X.intersection(Y)) > 0 for X, Y in assignments
))
