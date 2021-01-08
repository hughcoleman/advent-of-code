#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/03: Spiral Memory")
problem.preprocessor = int


import math


@problem.solver(part=1)
def p1(address):
    i = 1
    while i * i < address:
        i = i + 2

    corners = [pow(i, 2) - d*(i - 1) for d in range(4)]
    for corner in corners:
        distance = abs(corner - address)
        if distance <= (i - 1) // 2:
            return i - 1 - distance


@problem.solver(part=2)
def p2(threshold):
    memory = {0: 1}

    turtle = 0
    direction = 1
    n = 1

    while True:
        # turn twice, then extend leg length
        for _ in range(2):
            for __ in range(n):
                turtle = turtle + direction
                memory[turtle] = sum(
                    memory.get(complex(x, y), 0)
                        for x in range(
                            int(turtle.real) - 1, int(turtle.real) + 2
                        )
                        for y in range(
                            int(turtle.imag) - 1, int(turtle.imag) + 2
                        )
                )

                if memory[turtle] >= threshold:
                    return memory[turtle]

            direction = direction * 1j
        n = n + 1


if __name__ == "__main__":
    problem.solve()
