#!/usr/bin/env python3
""" 2021/25: Sea Cucumber """

import sys
import itertools as it

cucumbers = [
    list(ln) for ln in sys.stdin.read().strip().split("\n")
]

width, height = len(cucumbers[0]), len(cucumbers)

for step in it.count(1):
    moves = sorted(
        (cucumbers[y][x], x, y)
            for y in range(height)
            for x in range(width)
            if (
                # This is an east-facing cucumber that can move into an empty
                # space.
                (cucumbers[y][x] == ">" and cucumbers[y][(x + 1) % width] == ".")

                or
                # This is a south-facing cucumber that is moving into a cell
                # containing an east-facing cucumber that is about to get out
                # of the way.
                (cucumbers[y][x] == "v" and cucumbers[(y + 1) % height][x] == ">" and cucumbers[(y + 1) % height][(x + 1) % width] == ".")

                or
                # This is a south-facing cucumber that is moving into a cell
                # that will not be occupied by an east-facing cucumber.
                (cucumbers[y][x] == "v" and cucumbers[(y + 1) % height][x] == "." and cucumbers[(y + 1) % height][(x - 1) % width] != ">")
            )
    )

    if len(moves) == 0:
        print("Part 1:", step)
        break

    for c, x, y in moves:
        cucumbers[y][x] = "."

        if c == ">":
            cucumbers[y][(x + 1) % width] = c
        else:
            cucumbers[(y + 1) % height][x] = c

print("Part 2:", "Remotely Start The Sleigh")
