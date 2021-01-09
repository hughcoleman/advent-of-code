#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/17: Spinlock")
problem.preprocessor = int


@problem.solver(part=1)
def spinlock(skip):
    pins, i = [0], 0
    for v in range(1, 2017 + 1):
        i = (i + skip) % len(pins) + 1
        pins.insert(i, v)

    return pins[pins.index(2017) + 1]


@problem.solver(part=2)
def solve(skip):
    # rather than keep track of the entire game, we can specifically track only
    # the value(s) inserted into position 1
    position, q = 1, None
    for i in range(1, 50000000 + 2):
        n = (position + skip) % i
        if n <= 0:
            q = i

        position = n + 1

    return q


if __name__ == "__main__":
    problem.solve()
