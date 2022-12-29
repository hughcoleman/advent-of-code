#!/usr/bin/env python3
""" 2022/25: Full of Hot Air """

import sys

def f(n):
    return 5*f(n[:-1]) + "=-012".index(n[-1]) - 2 if n else 0

def g(n):
    return g((n + 2) // 5) + "012=-"[n % 5] if n else ""

print("Part 1:", g(sum(map(f, sys.stdin.read().strip().split("\n")))))
print("Part 2:", "Start The Blender")
