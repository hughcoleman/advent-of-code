#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/17: Conway Cubes")
problem.preprocessor = ppr.grid

from collections import defaultdict


def evolve(active, generations=6, dimensions=3):
    for generation in range(generations):
        # track the activity around each (hyper)cube
        activities = defaultdict(int, {cell: 0 for cell in active})
        for cell in active:
            # it's significantly more efficient for each active cell to ping
            # each of its neighbours, rather than have each cell count the
            # number of active neighbours
            for neighbour in cell.neighbours(dimensions):
                activities[neighbour] += 1

        _active = set()  # next generation
        for cell, activity in activities.items():
            if (cell in active) and (2 <= activity <= 3):
                _active.add(cell)
            elif (cell not in active) and (activity == 3):
                _active.add(cell)

        active = _active

    return len(active)


@problem.solver(part=1)
def p1_3d(initial):
    active = set()
    for x, y in [
        (x, y) for x in range(len(initial[0])) for y in range(len(initial))
    ]:
        if initial[y][x] == "#":
            active.add(Point(x, y, 0))

    return evolve(active, generations=6, dimensions=3)


@problem.solver(part=2)
def p2_4d(initial):
    active = set()
    for x, y in [
        (x, y) for x in range(len(initial[0])) for y in range(len(initial))
    ]:
        if initial[y][x] == "#":
            active.add(Point(x, y, 0, 0))

    return evolve(active, generations=6, dimensions=4)


if __name__ == "__main__":
    problem.solve()
