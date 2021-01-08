#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/25: Let It Snow")
problem.preprocessor = lambda message: tuple(
    int(coordinate) for coordinate in re.findall(r"\d+", message)
)

import re


@problem.solver()
def solve(inp):
    row, column = inp

    N = (row + column - 2) * (row + column - 1) // 2 + column

    return (
        (20151125 * pow(252533, N - 1, 33554393)) % 33554393,
        "Merry Christmas!",
    )


if __name__ == "__main__":
    problem.solve()
