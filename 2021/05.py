#!/usr/bin/env python3
""" 2021/05: Hydrothermal Venture """

import sys
import collections as cl

vents = [
    tuple(
        tuple( int(coordinate) for coordinate in point.split(",") )
            for point in ln.strip().split(" -> ")
    )
        for ln in sys.stdin.read().strip().split("\n")
]

floor = cl.defaultdict(int)

for (x1, y1), (x2, y2) in vents:
    if (x1 == x2) or (y1 == y2):
        for d in range(abs(x2 - x1) + abs(y2 - y1) + 1):
            floor[min(x1, x2) + d*(x1 != x2), min(y1, y2) + d*(y1 != y2)] += 1

print("Part 1:", sum(x > 1 for x in floor.values()))

for (x1, y1), (x2, y2) in vents:
    if (x1 != x2) and (y1 != y2):
        dx = (x2 > x1) - (x1 > x2)
        dy = (y2 > y1) - (y1 > y2)
        for d in range(abs(x2 - x1) + 1):
            floor[x1 + dx*d, y1 + dy*d] += 1

print("Part 2:", sum(x > 1 for x in floor.values()))
