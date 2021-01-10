#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/19: A Series of Tubes")
problem.preprocessor = lambda grid: [
    list(l) for l in grid.split("\n") if len(l) > 0
]


@problem.solver()
def solve(pipes):

    path = {}
    for y, row in enumerate(pipes):
        for x, c in enumerate(row):
            if not c.isspace():
                if y <= 0 and c in ["|", "-"]:
                    position, delta = complex(x, y), complex(0, 1)

                path[complex(x, y)] = c

    steps, letters = 0, []
    while position in path.keys():
        # pick up the letters
        if path[position].isalpha():
            letters.append(path[position])

        # consider turns
        elif path[position] == "+":
            delta = complex(delta.imag, delta.real)

            if delta.real == 0.0 and (position + delta) not in path.keys():
                delta = complex(delta.real, -delta.imag)

            elif delta.imag == 0.0 and (position + delta) not in path.keys():
                delta = complex(-delta.real, delta.imag)

        position = position + delta
        steps = steps + 1

    return ("".join(letters), steps)


if __name__ == "__main__":
    problem.solve()
