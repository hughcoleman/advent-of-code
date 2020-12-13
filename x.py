#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2015/01: ???")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0
    for v in inp:
        print(v)

    return (p1, p2)

# tests?

if __name__ == "__main__":
    problem.solve()
