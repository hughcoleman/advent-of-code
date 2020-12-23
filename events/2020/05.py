#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/05: Binary Boarding")
problem.preprocessor = ppr.lsv

import re


@problem.solver()
def solve(tickets):
    seats = []
    for ticket in tickets:
        seats.append(
            int(re.sub(r"[FL]", "0", re.sub(r"[BR]", "1", ticket)), 2)
        )

    mine = None
    # slightly more efficient to iterate between smallest-numered and
    # largest-numbered seats
    for sid in range(min(seats), max(seats)):
        if (sid - 1 in seats) and (sid not in seats) and (sid + 1 in seats):
            mine = sid

    return (max(seats), mine)


if __name__ == "__main__":
    problem.solve()
