#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/09: Stream Processing")
problem.preprocessor = ppr.identity


@problem.solver()
def solve(stream):
    score = 0
    depth = 1
    garbage = False
    removed = 0

    i = 0
    while i < len(stream):
        c = stream[i]

        if c == "!":
            i = i + 1
        elif garbage and c != ">":
            removed = removed + 1
        elif c == "<":
            garbage = True
        elif c == ">":
            garbage = False
        elif c == "{":
            score = score + depth
            depth = depth + 1
        elif c == "}":
            depth = depth - 1

        i = i + 1

    return (score, removed)


if __name__ == "__main__":
    problem.solve()
