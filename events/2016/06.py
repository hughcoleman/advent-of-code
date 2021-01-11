#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/06: Signals and Noise")
problem.preprocessor = ppr.lsv


import collections as cl


@problem.solver(part=1)
def p1(messages):
    return "".join(
        c.most_common(1)[0][0]
        for c in [
            cl.Counter(message[i] for message in messages) for i in range(8)
        ]
    )


@problem.solver(part=2)
def p2(messages):
    return "".join(
        c.most_common()[-1][0]
        for c in [
            cl.Counter(message[i] for message in messages) for i in range(8)
        ]
    )


if __name__ == "__main__":
    problem.solve()
