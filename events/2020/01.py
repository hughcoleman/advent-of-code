#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/01: Report Repair")
problem.preprocessor = ppr.lsi


@problem.solver(part=1)
def p1(expenses):
    for i, p in enumerate(expenses):
        q = 2020 - p
        if q in expenses and expenses.index(q) > i:
            return p * q
    return None


@problem.solver(part=2)
def p2(expenses):
    for i, x in enumerate(expenses):
        for j, y in enumerate(expenses):
            z = 2020 - x - y
            if z in expenses and expenses.index(z) > j > i:
                return x * y * z
    return None


if __name__ == "__main__":
    problem.solve()
