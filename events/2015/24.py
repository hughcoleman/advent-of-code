#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/24: It Hangs in the Balance")
problem.preprocessor = ppr.lsi


import math
import itertools


def qe(weights):
    p = 1
    for weight in weights:
        p *= weight
    return p


def pack(packages, compartements):
    weight = sum(packages) / compartements

    # determine number of packages to pack in the front compartement
    for size in range(1, len(packages)):
        for packing in itertools.combinations(packages, size):
            if sum(packing) != weight:
                continue
            break
        else:
            continue
        break

    # find optimal quantum entaglement score
    optimal = math.inf
    for packing in itertools.combinations(packages, size):
        if sum(packing) != weight:
            continue
        optimal = min(optimal, qe(packing))

    return optimal


@problem.solver()
def solve(packages):
    return (pack(packages, 3), pack(packages, 4))


if __name__ == "__main__":
    problem.solve()
