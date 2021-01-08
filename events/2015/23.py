#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/23: Opening the Turing Lock")
problem.preprocessor = lambda instructions: [
    (instruction.split(" ")[0], instruction.split(" ", 1)[1].split(", "))
    for instruction in instructions.strip().split("\n")
]


def run(instructions, a=0, b=0):
    ip = 0
    registers = {"a": a, "b": b}

    while True:
        # machine halts if instruction pointer leaves the addressable space
        if ip < 0 or ip >= len(instructions):
            break

        instruction, arguments = instructions[ip]

        offset = 1
        if instruction == "hlf":
            registers[arguments[0]] //= 2
        elif instruction == "tpl":
            registers[arguments[0]] *= 3
        elif instruction == "inc":
            registers[arguments[0]] += 1
        elif instruction == "jmp":
            offset = int(arguments[0])
        elif instruction == "jie":
            if registers[arguments[0]] % 2 == 0:
                offset = int(arguments[1])
        elif instruction == "jio":
            if registers[arguments[0]] == 1:
                offset = int(arguments[1])
        else:
            raise RuntimeError(f"unparseable instruction {instruction}")

        ip = ip + offset

    return registers["b"]


@problem.solver()
def solve(instructions):
    p1 = run(instructions)
    p2 = run(instructions, a=1)

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
