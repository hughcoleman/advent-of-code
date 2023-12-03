#!/usr/bin/env python3
""" 2023/03: Gear Ratios """

import itertools as it
import sys

numbers, symbols = {}, {}
for y, ln in enumerate(sys.stdin.readlines()):
    x = 0
    while x < len(ln.strip()):
        c = ln[x]
        if c.isdigit():
            x0, n = x, int(c)
            while (c := ln[x + 1]).isdigit():
                n = 10 * n + int(c)
                x = x + 1
            numbers[x0, y] = n
        elif c != ".":
            symbols[x, y] = c
        x = x + 1

# Part numbers are adjacent to a symbol. We can be lazy with the bounds, since
# no grid square is both a symbol and a digit.
print("Part 1:",
    sum(
        number
            for (x, y), number in numbers.items()
            if any(
                (x + dx, y + dy) in symbols.keys()
                    for dx in range(-1, len(str(number)) + 1)
                    for dy in (-1, 0, 1)
            )
    )
)

# Gears are a little more difficult to detect, but it's do-able in quadratic
# time.
t = 0
for (x, y), symbol in symbols.items():
    if symbol == "*":
        adjacent_numbers = [
            number
                for (x0, y0), number in numbers.items()
                if (
                    x - len(str(number)) <= x0 <= x + 1
                    and y - 1 <= y0 <= y + 1
                )
        ]
        if len(adjacent_numbers) == 2:
            t = t + adjacent_numbers[0] * adjacent_numbers[1]
print("Part 2:", t)
