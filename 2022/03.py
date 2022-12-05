#!/usr/bin/env python3
""" 2022/03: Rucksack Reorganization """

import string
import sys

rucksacks = sys.stdin.read().strip().split("\n")

def priority(x):
    x, = x
    return string.ascii_letters.index(x) + 1

print("Part 1:", sum(
    priority(set(rucksack[:len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2:]))
        for rucksack in rucksacks
))
print("Part 2:", sum(
    priority(set.intersection(*map(set, rucksacks[i:i + 3])))
        for i in range(0, len(rucksacks), 3)
))