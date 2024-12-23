#!/usr/bin/env python3
""" 2024/08: Resonant Collinearity """

import collections as cl
import itertools as it
import math
import sys

city = {
    (r, c): ch
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ch in enumerate(line)
}

antennas = cl.defaultdict(set)
for (r, c), ch in city.items():
    if ch != ".":
        antennas[ch].add((r, c))

p1, p2 = set(), set()
for ch, antennas in antennas.items():
    for (a1_r, a1_c), (a2_r, a2_c) in it.combinations(antennas, 2):
        dr = a2_r - a1_r
        dc = a2_c - a1_c
        assert math.gcd(abs(dr), abs(dc)) == 1

        for sgn in { -1, 1 }:
            r0, c0 = (a1_r, a1_c) if sgn == -1 else (a2_r, a2_c)
            for i in it.count(0):
                r, c = r0 + sgn*i*dr, c0 + sgn*i*dc
                if (r, c) not in city.keys():
                    break
                if i == 1:
                    p1.add((r, c))
                p2.add((r, c))

print("Part 1:", len(p1))
print("Part 2:", len(p2))
