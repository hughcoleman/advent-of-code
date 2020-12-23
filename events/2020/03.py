#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/03: Toboggan Trajectory")
problem.preprocessor = ppr.grid

import functools
import operator


def ski(terrain, slope):
    width, height = len(terrain[0]), len(terrain)
    dx, dy = slope

    x, y, collisions = 0, 0, 0
    while y < height:
        if terrain[y][x % width] == "#":
            collisions = collisions + 1

        x, y = x + dx, y + dy

    return collisions


@problem.solver()
def solve(terrain):
    collisions = [
        ski(terrain, (1, 1)),
        ski(terrain, (3, 1)),
        ski(terrain, (5, 1)),
        ski(terrain, (7, 1)),
        ski(terrain, (1, 2)),
    ]

    return (collisions[1], functools.reduce(operator.mul, collisions))


if __name__ == "__main__":
    problem.solve()
