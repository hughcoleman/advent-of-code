#!/usr/bin/env python3
""" 2021/01: Sonar Sweep """

import sys

depths = [
    int(depth) for depth in sys.stdin.read().strip().split("\n")
]

print("Part 1:", sum(a < b for a, b in zip(depths, depths[1:])))

# The "middle" two numbers don't matter, since they are added to both
# sliding windows.
print("Part 2:", sum(a < b for a, b in zip(depths, depths[3:])))
