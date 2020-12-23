#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/10: Adapter Array")
problem.preprocessor = lambda adapters: sorted(
    int(joltage) for joltage in adapters.strip().split("\n")
)


@problem.solver()
def solve(joltages):
    device = max(joltages) + 3

    deltas = [0] * 4
    for a1, a2 in zip([0] + joltages, joltages + [device]):
        deltas[a2 - a1] = deltas[a2 - a1] + 1

    p1 = deltas[1] * deltas[3]

    # Part 2 is basically tribonacci, but only over the joltages which are
    # adapters that we possess.
    A = {}  # A[n] will be the number of arrangements of adapters that can
    # convert from 0 to n.
    A[0] = 1
    for joltage in joltages + [device]:
        A[joltage] = (
            A.get(joltage - 1, 0)
            + A.get(joltage - 2, 0)
            + A.get(joltage - 3, 0)
        )

    p2 = A[device]  # how many ways can the device be powered?

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
