#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/15: Dueling Generators")
problem.preprocessor = lambda initial: [
    int(initial.split("\n")[0].split(" ")[4]),
    int(initial.split("\n")[1].split(" ")[4]),
]


@problem.solver(part=1)
def p1(initial):
    A, B = initial

    matches = 0
    for trial in range(40_000_000):
        A, B = (A * 16807) % 2147483647, (B * 48271) % 2147483647

        if A & 0xFFFF == B & 0xFFFF:
            matches = matches + 1

    return matches


@problem.solver(part=2)
def p2(initial):
    A, B = initial

    # there's probably a clever algorithm based on the factors of the scalars,
    # but I haven't found it yet.
    matches = 0
    for trial in range(5_000_000):
        A = (A * 16807) % 2147483647
        while A % 4 > 0:
            A = (A * 16807) % 2147483647

        B = (B * 48271) % 2147483647
        while B % 8 > 0:
            B = (B * 48271) % 2147483647

        if A & 0xFFFF == B & 0xFFFF:
            matches = matches + 1

    return matches


if __name__ == "__main__":
    problem.solve()
