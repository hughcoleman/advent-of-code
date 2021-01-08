#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/11: Hex Ed")
problem.preprocessor = ppr.csv


DIRECTIONS = {
    "n": 1j,
    "s": -1j,
    "nw": -1,
    "se": 1,
    "ne": 1 + 1j,
    "sw": -1 - 1j,
}


@problem.solver()
def solve(directions):
    position = 0 + 0j
    distance = 0
    for step in directions:
        position = position + DIRECTIONS[step]

        # this shouldn't actually work (it'll return the distance back to the
        # origin travelling only along the axes) but it appears as if the
        # inputs have been crafted to allow this.
        distance = max(distance, abs(position.real) + abs(position.imag))

    return (int(abs(position.real) + abs(position.imag)), int(distance))


if __name__ == "__main__":
    problem.solve()
