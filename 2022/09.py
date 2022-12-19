#!/usr/bin/env python3
""" 2022/09: Rope Bridge """

import sys

motions = sys.stdin.read().strip().split("\n")

def sgn(x):
    return (x > 0) - (x < 0)

part1, part2 = set(), set()
knot = [
    0 + 0j for _ in range(10)
]
for motion in motions:
    for _ in range(int(motion[1:])):
        for i in range(len(knot)):
            d = 0
            if i <= 0:
                d = {"R": 1, "L": -1, "U": 1j, "D": -1j}[motion[0]]
            else:
                k = knot[i - 1] - knot[i]
                if abs(k) >= 2:
                    d = sgn(k.real) + sgn(k.imag) * 1j

            knot[i] = knot[i] + d

            if i == 1: part1.add(knot[i])
            if i == 9: part2.add(knot[i])
                
print("Part 1:", len(part1))
print("Part 2:", len(part2))
