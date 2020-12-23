#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/08: Handheld Halting")
problem.preprocessor = lambda program: [
    # parse each instruction to (op, [arg1, arg2, ...])
    (op, [int(arg) for arg in args.split(",")])
    for op, args in [ln.split(" ") for ln in program.strip().split("\n")]
]


def run(program, mutations=[]):
    ip, accumulator = 0, 0
    callstack = []

    while (ip not in callstack) and (0 <= ip < len(program)):
        # extract operation, arguments
        operation, arguments = program[ip]
        callstack.append(ip)

        # apply any mutations
        if ip in mutations:
            operation = {"jmp": "nop", "nop": "jmp"}[operation]

        # parse and execute instruction
        if operation == "acc":
            accumulator = accumulator + arguments[0]
            ip = ip + 1
        elif operation == "jmp":
            ip = ip + arguments[0]
        elif operation == "nop":
            ip = ip + 1
        else:
            raise NotImplementedError(f"illegal operation {operation}")

    looped = not (ip >= len(program))
    return (looped, accumulator, callstack)


@problem.solver()
def solve(bootcode):
    _, p1, callstack = run(bootcode)

    p2 = None
    for address in callstack:
        operation, _ = bootcode[address]
        if operation in ["jmp", "nop"]:
            looped, accumulator, _ = run(bootcode, mutations=[address])
            if not looped:
                p2 = accumulator

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
