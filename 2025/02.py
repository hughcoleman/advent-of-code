#!/usr/bin/env python3
""" 2025/02: Gift Shop """

import sys

ranges = [
    tuple(map(int, ln.split("-")))
        for ln in sys.stdin.readline().strip().split(",")
]

print("Part 1:", sum(
    sum(
        i for i in range(lo, hi + 1)
            if (s := str(i)) and (l := len(s)) and s == s[:l // 2] * 2
    ) for lo, hi in ranges
))

print("Part 2:", sum(
    sum(
        i for i in range(lo, hi + 1)
            if (s := str(i)) and (l := len(s)) and any(s == s[:l // q] * q for q in range(2, l + 1))
    ) for lo, hi in ranges
))
