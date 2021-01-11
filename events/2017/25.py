#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/25: The Halting Problem")
problem.preprocessor = lambda blueprints: [
    block.split("\n") for block in ppr.llsv(blueprints)
]


import collections as cl


def parse(ruleset):
    # This is a really awful parser for this; it only handles the specific
    # format of the input used on AoC.

    rules = {}
    for rule in ruleset:
        rules[rule[0].split(" ")[2][0], 0] = [
            0 if "0" in rule[2] else 1,
            1 if "right" in rule[3] else -1,
            rule[4].split()[-1][0],
        ]
        rules[rule[0].split(" ")[2][0], 1] = [
            0 if "0" in rule[6] else 1,
            1 if "right" in rule[7] else -1,
            rule[8].split()[-1][0],
        ]

    return rules


@problem.solver()
def solve(blueprints):
    meta, *ruleset = blueprints

    # extract metadata, and steps
    state, steps = meta[0].split()[3][:-1], int(meta[1].split()[5])
    rules = parse(ruleset)

    # run the Turing machine!
    tape, cursor = cl.defaultdict(int), 0
    for _ in range(steps):
        write, move, state = rules[state, tape[cursor]]

        tape[cursor] = write
        cursor = cursor + move

    return (list(tape.values()).count(1), "Merry Christmas!")


if __name__ == "__main__":
    problem.solve()
