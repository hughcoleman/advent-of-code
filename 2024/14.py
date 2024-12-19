#!/usr/bin/env python3
""" 2024/14: Restroom Redoubt """

import re
import statistics as stat
import sys

robots = [
    tuple(map(int, re.findall(r"(-?\d+)", s)))
        for s in sys.stdin.read().strip().split("\n")
]

def at(t):
    return [
        ((x + t*dx) % 101, (y + t*dy) % 103)
            for (x, y, dx, dy) in robots
    ]

print("Part 1:",
    sum(1 for (x, y) in at(100) if x > 50 and y > 51)
    * sum(1 for (x, y) in at(100) if x > 50 and y < 51)
    * sum(1 for (x, y) in at(100) if x < 50 and y > 51)
    * sum(1 for (x, y) in at(100) if x < 50 and y < 51)
)

# We'll look at the time which minimises the variance of the robot positions
# in each direction, and then use the Chinese Remainder Theorem to determine
# when the overall variance is minimised (ie. when the robots are clustered).
m = lambda i, mod: min(
    [ (t, stat.variance(p[i] for p in at(t))) for t in range(mod) ],
    key=lambda p: p[1],
)[0]
x_min = m(0, 101)
y_min = m(1, 103)

print("Part 2:", ((x_min * pow(103, -1, 101) * 103) + (y_min * pow(101, -1, 103) * 101)) % (101 * 103))
