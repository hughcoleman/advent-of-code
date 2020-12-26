#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/03: Perfectly Spherical Houses in a Vacuum")
problem.preprocessor = ppr.characters


COMPLEX_DIRECTIONS = {">": 1, "<": -1, "^": 1j, "v": -1j}


def deliver(instructions):
    position = 0 + 0j
    visited = set([position])

    for instruction in instructions:
        position = position + COMPLEX_DIRECTIONS[instruction]
        visited.add(position)

    return visited


@problem.solver(part=1)
def p1(instructions):
    return len(deliver(instructions))


@problem.solver(part=2)
def p2(instructions):
    return len(
        set.union(deliver(instructions[::2]), deliver(instructions[1::2]))
    )


if __name__ == "__main__":
    problem.solve()
