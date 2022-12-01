#!/usr/bin/env python3
""" 2022/01: Calorie Counting """

import sys

elves = sorted(
    sum(map(int, elf.split())) for elf in sys.stdin.read().split("\n\n")
)[::-1]

print("Part 1:", elves[0])
print("Part 2:", sum(elves[:3]))