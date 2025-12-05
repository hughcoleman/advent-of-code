#!/usr/bin/env python3
""" 2025/05: Cafeteria """

import sys

ingredient_ranges = sorted(
    tuple(map(int, ln.split('-')))
        for ln in iter(sys.stdin.readline, "\n")
)
ingredients = [
    int(ln) for ln in iter(sys.stdin.readline, "")
]

print("Part 1:", sum(
    any(lo <= i <= hi for lo, hi in ingredient_ranges)
        for i in ingredients
))

def merge():
    it = iter(ingredient_ranges)
    lo, hi = next(it)
    for lo0, hi0 in it:
        if lo0 <= hi:
            hi = max(hi, hi0)
        else:
            yield (lo, hi)
            lo, hi = lo0, hi0
    yield (lo, hi)

print("Part 2:", sum(hi - lo + 1 for lo, hi in merge()))
