#!/usr/bin/env python3
""" 2024/25: Code Chronicle """

import itertools as it
import sys

lockkeys = sys.stdin.read().strip().split("\n\n")

print("Part 1:",
    sum(
        not any(x1 == x2 == "#" for x1, x2 in zip(X1, X2))
            for X1, X2 in it.combinations(lockkeys, 2)
    )
)
print("Part 2:", "Deliver The Chronicle")
