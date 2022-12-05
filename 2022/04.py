#!/usr/bin/env python3
""" 2022/04: Camp Cleanup """

import re
import sys

f = lambda a, b, c, d: (set(range(a, b + 1)), set(range(c, d + 1)))
assignments = [
    f(*map(int, re.findall(r"\d+", assignment)))
        for assignment in sys.stdin.read().strip().split("\n") 
]

print("Part 1:", sum(
    X.issubset(Y) or Y.issubset(X) for X, Y in assignments
))
print("Part 2:", sum(
    len(X.intersection(Y)) > 0 for X, Y in assignments
))
