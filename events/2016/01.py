#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/01: No Time for a Taxicab")
problem.preprocessor = lambda instructions: [
    (instruction[0], int(instruction[1:]))
    for instruction in instructions.split(", ")
]


@problem.solver()
def solve(instructions):
    position, direction = 0 + 0j, 0 + 1j
    visited, p2 = set(), None

    for (turn, distance) in instructions:
        direction *= {"R": -1j, "L": 1j}[turn]

        for _ in range(distance):
            position = position + direction

            if position in visited and not p2:
                p2 = position
            visited.add(position)

    return (
        int(abs(position.real) + abs(position.imag)),
        int(abs(p2.real) + abs(p2.imag)),
    )


if __name__ == "__main__":
    problem.solve()
