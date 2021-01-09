#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/06: Permutation Promenade")
problem.preprocessor = lambda routine: [
    (
        move[0],
        [
            int(argument) if argument.isdigit() else argument
            for argument in move[1:].split("/")
        ],
    )
    for move in routine.strip().split(",")
]


def dance(programs, routine, rounds=1):
    # perform the routine once, keeping track of the exchanges and
    # substitutions between programs rather than the actual positions of the
    # programs themselves.
    exchanges = list(range(16))
    substitutions = {program: program for program in list(programs)}

    for move, arguments in routine:
        if move == "s":  # SHIFT
            exchanges = exchanges[-arguments[0] :] + exchanges[: -arguments[0]]
        elif move == "x":  # EXCHANGE
            exchanges[arguments[0]], exchanges[arguments[1]] = (
                exchanges[arguments[1]],
                exchanges[arguments[0]],
            )
        elif move == "p":  # PARTNER
            for k, v in substitutions.items():
                if v == arguments[0]:
                    substitutions[k] = arguments[1]
                elif v == arguments[1]:
                    substitutions[k] = arguments[0]

    # now, we can jumpahead as many rounds as desired, using the
    # square-and-multiply algorithm for exponentiation
    while rounds > 0:
        if (rounds % 2) > 0:
            programs = [substitutions[programs[i]] for i in exchanges]

        exchanges = [exchanges[i] for i in exchanges]
        substitutions = {k: substitutions[v] for k, v in substitutions.items()}

        rounds >>= 1

    return "".join(programs)


@problem.solver()
def solve(routine):
    return (
        dance(list("abcdefghijklmnop"), routine, rounds=1),
        dance(list("abcdefghijklmnop"), routine, rounds=1000000000),
    )
    return (0, 0)


if __name__ == "__main__":
    problem.solve()
