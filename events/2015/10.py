#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/10: Elves Look, Elves Say")
problem.preprocessor = ppr.characters

import itertools as it


def las(sequence, generations=40):
    for generation in range(generations):
        spoken = ""
        for digit, count in it.groupby(sequence):
            spoken += str(len(list(count))) + digit
        sequence = spoken

    return sequence


@problem.solver()
def solve(inp):
    p1 = las(inp, generations=40)
    p2 = las(p1, generations=(50 - 40))

    return (len(p1), len(p2))


if __name__ == "__main__":
    problem.solve()
