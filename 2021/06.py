#!/usr/bin/env python3
""" 2021/06: Lanternfish """

import sys
import collections as cl

lanternfish = cl.Counter(
    int(fish) for fish in sys.stdin.read().strip().split(",")
)

def reproduce(fish, generations=80):
    for _ in range(generations):
        offspring = cl.Counter()
        for age, number in fish.items():
            if age <= 0:
                offspring[6] += number
                offspring[8] += number
            else:
                offspring[age - 1] += number

        fish = offspring

    return fish

p1 = reproduce(lanternfish)

print("Part 1:", sum(p1.values()))
print("Part 2:", sum(reproduce(p1, generations=(256 - 80)).values()))
