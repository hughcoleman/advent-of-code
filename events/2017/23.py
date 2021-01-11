#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/23: Coprocessor Conflagration")
problem.preprocessor = lambda program: [
    (instruction.split(" ")[0], instruction.split(" ", 1)[1].split(" "))
    for instruction in program.strip().split("\n")
]


import collections as cl
import math


class Coprocessor:
    """ Simulate a single experimental coprocessor. """

    def step(self):
        op, args = self.rom[self.ip]

        offset = 1
        if op == "set":
            self.registers[args[0]] = self.get(args[1])
        elif op == "sub":
            self.registers[args[0]] -= self.get(args[1])
        elif op == "mul":
            self.registers[args[0]] *= self.get(args[1])
        elif op == "jnz":
            if self.get(args[0]) != 0:
                offset = self.get(args[1])

        self.ip = self.ip + offset
        return 0 if op != "mul" else 1

    def run(self):
        # run the virtual machine, until the instruction pointer leaves the
        # bounds of addressable memory
        p1 = 0
        while 0 <= self.ip < len(self.rom):
            p1 = p1 + self.step()

        return p1

    def get(self, r):
        if r.isalpha():
            return self.registers[r]
        return int(r)

    def __init__(self, instructions, override={}):
        self.rom = instructions
        self.ip = 0

        # registers are unknown (but known to be referred to using
        # one-character strings.
        self.registers = cl.defaultdict(lambda: 0)
        for register, value in override.items():
            self.registers[register] = value


@problem.solver(part=1)
def p1(instructions):
    processor = Coprocessor(instructions)
    return processor.run()


@problem.solver(part=2)
def p2(instructions):
    # Part 2 requires some amount of human intervention; it will not terminate
    # in a reasonable amount of time.

    # We can disassemble the program, and discover that when a is non-zero,
    # program control is redirected to a block not used by Part 1. It appears
    # to compute some value (unique to each player), and places it in register
    # b. It also computes b + 17000, and places this sum in register c.
    #
    # We can obtain these values for ourselves by stepping the computer seven
    # times after initialization.
    processor = Coprocessor(instructions, override={"a": 1})
    for _ in range(7):
        processor.step()

    b = processor.registers["b"]
    c = processor.registers["c"]

    # The program then runs the following (pseudocode)
    #
    #     while (b <= c) {
    #         f = 1
    #         for (int d = 2; d < b; d++) {
    #             for (int e = 2; e < b; e++) {
    #                 if d * e == b {
    #                     f = 0
    #                 }
    #             }
    #         }
    #
    #         if (f == 0) {
    #             h++;
    #         }
    #
    #         b = b + 17
    #     }
    #
    # This is esentially just counting the number of composite numbers in the
    # range [b, c], counting by 17s.
    #
    # We can re-implement this in Python, but use a much more efficient
    # algorithm to get the answer in a reasonable amount of time.
    h = 0
    for candidate in range(b, c + 1, 17):
        for factor in range(2, int(math.sqrt(candidate)) + 1):
            if candidate % factor <= 0:
                h = h + 1
                break

    return h


if __name__ == "__main__":
    problem.solve()
