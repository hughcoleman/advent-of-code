#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/06: Memory Reallocation")
problem.preprocessor = lambda banks: [
        int(bank) for bank in banks.strip().split()        
]


import math


@problem.solver()
def solve(banks):
    p1, p2 = math.inf, 0

    # track seen configurations of banks
    seen = {}

    cycle = 0
    while tuple(banks) not in seen:
        seen[tuple(banks)] = cycle

        # find the bank with the most funds
        i = banks.index(max(banks))
        n = banks[i]

        # distribute the funds in that bank
        banks[i] = 0
        for j in range(i + 1, i + n + 1):
            banks[j % len(banks)] = banks[j % len(banks)] + 1

        cycle = cycle + 1

    return (cycle, cycle - seen[tuple(banks)])


if __name__ == "__main__":
    problem.solve()
