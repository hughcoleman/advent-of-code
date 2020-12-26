#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/08: Matchsticks")
problem.preprocessor = ppr.lsv


@problem.solver(part=1)
def p1(strings):
    total = 0
    for string in strings:
        memory = 0
        i = 1
        while i < len(string) - 1:
            c = string[i]
            if c == "\\":  # ...then this is an escape sequence; skip over it
                if string[i + 1] in ["\\", '"']:
                    i = i + 2
                elif string[i + 1] in ["x"]:
                    i = i + 4
                else:
                    raise RuntimeError("unreachable state?")

            else:  # ...this is a normal byte
                i = i + 1

            memory = memory + 1

        # compute difference between literal/in-memory size
        total = total + len(string) - memory

    return total


@problem.solver(part=2)
def p2(strings):
    total = 0
    for string in strings:
        encoded = string.replace("\\", "\\\\").replace('"', '\\"')

        total = total + len(encoded) + 2 - len(string)

    return total


if __name__ == "__main__":
    problem.solve()
