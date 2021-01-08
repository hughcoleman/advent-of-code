#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/17: No Such Thing as Too Much")
problem.preprocessor = ppr.lsi

import itertools


@problem.solver()
def solve(cups):
    ns = [0] * len(cups)
    for n in range(1, len(cups) + 1):
        m = 0
        for combination in itertools.combinations(cups, n):
            if sum(combination) == 150:
                m = m + 1
        ns[n - 1] = m

    return (sum(ns), next(m for m in ns if m != 0))


if __name__ == "__main__":
    problem.solve()
