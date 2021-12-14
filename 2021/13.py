#!/usr/bin/env python3
""" 2021/13: Transparent Origami """

import sys

dots, instructions = sys.stdin.read().strip().split("\n\n")

dots = set(
    tuple(int(c) for c in dot.split(","))
        for dot in dots.split("\n")
)
instructions = [
    tuple(f(x) for x, f in zip(instruction.split()[-1].split("="), [str.strip, int]))
        for instruction in instructions.split("\n")
]

for i, (axis, coordinate) in enumerate(instructions):
    dots = set(
        (
            coordinate - abs(x - coordinate) if axis == "x" else x,
            coordinate - abs(y - coordinate) if axis == "y" else y
        )
            for x, y in dots
    )

    if i == 0:
        print("Part 1:", len(dots))

max_x = max(x for x, y in dots)
max_y = max(y for x, y in dots)

print("Part 2:",
    "\n" + "\n".join(
        "".join(
            "#" if (x, y) in dots else " "
                for x in range(max_x + 1)
        )
        for y in range(max_y + 1)
    )
)
