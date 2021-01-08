#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/03: Squares With Three Sides")
problem.preprocessor = lambda triangles: [
    [int(measurement) for measurement in triangle.split()]
    for triangle in triangles.strip().split("\n")
]


@problem.solver(part=1)
def horizonal(triangles):
    valid = 0
    for triangle in triangles:
        sides = sorted(triangle)

        if sides[0] + sides[1] > sides[2]:
            valid = valid + 1

    return valid


@problem.solver(part=2)
def vertical(triangles):
    valid = 0
    for row in range(0, len(triangles), 3):
        for column in range(3):
            sides = sorted(triangles[row + d][column] for d in range(3))

            if sides[0] + sides[1] > sides[2]:
                valid = valid + 1

    return valid


if __name__ == "__main__":
    problem.solve()
