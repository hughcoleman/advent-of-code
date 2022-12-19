#!/usr/bin/env python3
""" 2022/14: Regolith Reservoir """

import itertools as it
import sys

paths = [
    list(map(lambda xy: tuple(map(int, xy.split(","))), path.split(" -> ")))
        for path in sys.stdin.read().strip().split("\n")
]

C = set()
for (x, y), *path in paths:
    C.add((x, y))
    for x0, y0 in path:
        while (x != x0) or (y != y0):
            x, y = x + (x0 > x) - (x > x0), y + (y0 > y) - (y > y0)
            C.add((x, y))

Y = max(
    max(map(lambda xy: xy[1], path)) + 2
        for path in paths
)
for x in range(500 - Y - 1, 500 + Y + 1):
    C.add((x, Y))

# Now that we've identified the terrain, we can proceed to simulate the falling
# sand particles.
p1 = False
for n in it.count():
    x, y = 500, 0
    if (x, y) in C:
        print("Part 2:", n)
        break

    while True:
        if not p1 and y >= Y - 1:
            print("Part 1:", n)
            p1 = True

        for dx in (0, -1, 1):
            if (x + dx, y + 1) not in C:
                x, y = x + dx, y + 1
                break
        else:
            C.add((x, y))
            break
