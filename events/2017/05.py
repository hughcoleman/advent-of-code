#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/05: A Maze of Twisty Trampolines, All Alike")
problem.preprocessor = ppr.lsi


def run(jumps, p2=False):
    ip, cycles = 0, 0
    while 0 <= ip < len(jumps):
        offset = jumps[ip]
        if p2 and offset >= 3:
            jumps[ip] = offset - 1
        else:
            jumps[ip] = offset + 1

        ip = ip + offset
        cycles = cycles + 1

    return cycles


@problem.solver()
def solve(jumps):
    return (
        run(jumps[:]),              # pass a copy, because run() modifies jumps
        run(jumps[:], p2=True)
    )


if __name__ == "__main__":
    problem.solve()
