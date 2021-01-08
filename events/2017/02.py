#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/02: Corruption Checksum")
problem.preprocessor = lambda spreadsheet: [
        [int(cell) for cell in row.split()]
        for row in spreadsheet.strip().split("\n")
]


@problem.solver(part=1)
def p1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)


@problem.solver(part=2)
def p2(spreadsheet):
    total = 0
    for row in spreadsheet:
        for i, A in enumerate(row):
            for _, B in enumerate(row[i + 1:]):
                if max(A, B) % min(A, B) <= 0:
                    break
            else:
                continue
            break
        else:
            raise RuntimeError("no pairs divide each other")

        total = total + (max(A, B) // min(A, B))

    return total


if __name__ == "__main__":
    problem.solve()
