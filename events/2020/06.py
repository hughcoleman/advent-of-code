#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/06: Custom Customs")
problem.preprocessor = lambda groups: [
    [set(responses) for responses in group.split("\n")]
    for group in groups.strip().split("\n\n")
]


@problem.solver()
def solve(groups):
    some, all_ = 0, 0
    for group in groups:
        some = some + len(set.union(*group))
        all_ = all_ + len(set.intersection(*group))

    return (some, all_)


if __name__ == "__main__":
    problem.solve()
