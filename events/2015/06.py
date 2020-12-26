#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/06: Probably a Fire Hazard")
problem.preprocessor = ppr.lsv

import re
import collections as cl


@problem.solver(part=1)
def p1(instructions):
    lights = cl.defaultdict(lambda: False)
    for instruction in instructions:
        action, sx, sy, ex, ey = re.fullmatch(
            r"(.+?) (\d+),(\d+) through (\d+),(\d+)", instruction
        ).groups()

        for x in range(int(sx), int(ex) + 1):
            for y in range(int(sy), int(ey) + 1):
                lights[x, y] = {
                    "turn on": True,
                    "turn off": False,
                    "toggle": not lights[x, y],
                }[action]

    return list(lights.values()).count(True)


@problem.solver(part=2)
def p2(instructions):
    lights = cl.defaultdict(int)
    for instruction in instructions:
        action, sx, sy, ex, ey = re.fullmatch(
            r"(.+?) (\d+),(\d+) through (\d+),(\d+)", instruction
        ).groups()

        for x in range(int(sx), int(ex) + 1):
            for y in range(int(sy), int(ey) + 1):
                lights[x, y] += {"turn on": 1, "turn off": -1, "toggle": 2}[
                    action
                ]

                if lights[x, y] < 0:
                    lights[x, y] = 0

    return sum(lights.values())


if __name__ == "__main__":
    problem.solve()
