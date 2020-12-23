#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/15: Rambunctious Recitation")
problem.preprocessor = ppr.csi


@problem.solver()
def solve(seed):
    spoken = [-1] * 30_000_000
    for i, number in enumerate(seed[:-1]):
        spoken[number] = i

    previous = seed[-1]
    for i in range(len(seed), 2020):
        n = 0
        if spoken[previous] >= 0:
            n = i - spoken[previous] - 1

        spoken[previous] = i - 1
        previous = n

    p1 = previous

    for i in range(2020, 30_000_000):
        n = 0
        if spoken[previous] >= 0:
            n = i - spoken[previous] - 1

        spoken[previous] = i - 1
        previous = n

    p2 = previous

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
