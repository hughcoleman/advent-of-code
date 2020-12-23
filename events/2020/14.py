#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/14: Docking Data")
problem.preprocessor = ppr.lsv

import itertools


@problem.solver(part=1)
def p1(program):
    memory, mask = {}, None
    for instruction in program:
        operation, argument = instruction.split(" = ")
        if operation.startswith("mask"):
            mask = list(argument)
        elif operation.startswith("mem"):
            address, value = int(operation[4:-1]), int(argument)

            for position, mbit in enumerate(mask):
                if mbit == "0":
                    value &= ~pow(2, 35 - position)
                elif mbit == "1":
                    value |= pow(2, 35 - position)

            memory[address] = value
        else:
            raise NotImplementedError(f"could not understand {instruction}")

    return sum(memory.values())


def powersets(s):
    # compute the powerset of a set n
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


@problem.solver(part=2)
def p2(program):
    memory, mask = {}, None
    for instruction in program:
        operation, argument = instruction.split(" = ")
        if operation.startswith("mask"):
            mask = list(argument)
        elif operation.startswith("mem"):
            address, value = int(operation[4:-1]), int(argument)

            floats = []  # keep track of bit positions of floating bits
            for position, mbit in enumerate(mask):
                if mbit == "1":
                    address |= pow(2, 35 - position)
                elif mbit == "X":
                    address &= ~pow(2, 35 - position)
                    floats.append(35 - position)

            # generate all powersets of the floating point bits; and apply
            # those positions to n
            for combination in powersets(floats):
                candidate = address
                for exponent in combination:
                    candidate = candidate + pow(2, exponent)

                memory[candidate] = value
        else:
            raise NotImplementedError(f"could not understand {instruction}")

    return sum(memory.values())


if __name__ == "__main__":
    problem.solve()
