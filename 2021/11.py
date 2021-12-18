#!/usr/bin/env python3
""" 2021/11: Dumbo Octopus """

import sys
import itertools as it

octopuses = {
    (x, y): int(energy)
        for y, ln in enumerate(sys.stdin.read().strip().split("\n"))
        for x, energy in enumerate(ln)
}

def evolve(octopuses):
    for (x, y), energy in octopuses.items():
        octopuses[x, y] += 1

    flashed = set()
    while any(
        (x, y) not in flashed and energy > 9
            for (x, y), energy in octopuses.items()
    ):
        for (x, y), energy in octopuses.items():
            if (energy > 9) and ((x, y) not in flashed):
                flashed.add((x, y))

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (x + dx, y + dy) in octopuses.keys():
                            octopuses[x + dx, y + dy] += 1

    for (x, y) in flashed:
        octopuses[x, y] = 0

    return len(flashed)

flashes = 0
for step in range(1, 100 + 1):
    flashes = flashes + evolve(octopuses)

print("Part 1:", flashes)

# assume: Part 2 happens /after/ Part 1.
for step in it.count(step):
    if evolve(octopuses) >= len(octopuses.keys()):
        print("Part 2:", step + 1)
        break
