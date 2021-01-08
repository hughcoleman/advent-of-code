#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/08: I Heard You Like Registers")
problem.preprocessor = ppr.lsv


import collections as cl


CONDITIONS = {
    "==": lambda l, r: l == r,
    "!=": lambda l, r: l != r,
    ">": lambda l, r: l > r,
    "<": lambda l, r: l < r,
    ">=": lambda l, r: l >= r,
    "<=": lambda l, r: l <= r,
}


@problem.solver()
def solve(program):
    registers = cl.defaultdict(int)
    memory = 0

    for instruction in program:
        (
            register,
            sign,
            scalar,
            _,
            lcomparand,
            comparator,
            rcomparand,
        ) = instruction.split(" ")

        # the left comparand in the condition is always the register, and the
        # rcomparand is always the value
        if CONDITIONS[comparator](registers[lcomparand], int(rcomparand)):
            registers[register] += {"inc": 1, "dec": -1}[sign] * int(scalar)

        memory = max(memory, max(registers.values()))

    return (max(registers.values()), memory)


if __name__ == "__main__":
    problem.solve()
