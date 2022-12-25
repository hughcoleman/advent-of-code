#!/usr/bin/env python3
""" 2022/25: Full of Hot Air """

import sys

def f(n):
    return sum(
        ("=-012".index(c) - 2) * 5**i
            for i, c in enumerate(n.strip()[::-1])
    )

def g(n):
    return "" if n == 0 else g((n + 2) // 5) + "012=-"[n % 5]

print("Part 1:", g(sum(map(f, sys.stdin.readlines()))))
print("Part 2:", "Start The Blender")
