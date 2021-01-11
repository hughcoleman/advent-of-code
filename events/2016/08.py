#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/08: Two-Factor Authentication")
problem.preprocessor = lambda instructions: [
    instruction.split(" ") for instruction in instructions.strip().split("\n")
]


@problem.solver()
def solve(instructions):
    screen = {(x, y): 0 for x in range(50) for y in range(6)}

    for instruction in instructions:
        op, *args = instruction

        if op == "rect":
            width, height = [int(d) for d in args[0].split("x")]

            for y in range(height):
                for x in range(width):
                    screen[x, y] = 1
        elif op == "rotate":
            direction = args.pop(0)

            if direction == "row":
                y, offset = int(args[0].split("=")[1]), int(args[2])

                screen = {
                    (_x, _y):      screen[_x, _y] if _y != y
                              else screen[(_x - offset) % 50, _y]
                    
                    for _x in range(50) for _y in range(6)
                }

            elif direction == "column":
                x, offset = int(args[0].split("=")[1]), int(args[2])

                screen = {
                    (_x, _y):      screen[_x, _y] if _x != x
                              else screen[_x, (_y - offset) % 6]
                    
                    for _x in range(50) for _y in range(6)
                }

            else:
                raise RuntimeError("cannot rotate along {}".format(direction))
        else:
            raise RuntimeError("unknown operation {}".format(op))

    checksum = sum(screen.values())

    # unfortunately, no OCR here
    captcha = "\n"
    for y in range(6):
        for x in range(50):
            captcha = captcha + " #"[screen[x, y]]
        captcha = captcha + "\n"

    return (checksum, captcha)


if __name__ == "__main__":
    problem.solve()
