#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2020/19: Monster Messages")
problem.preprocessor = lambda inp: (
    {
        # dict{rule: pattern}
        int(rule.split(": ")[0]): (
            rule.split(": ")[1][1:-1]
                if rule.split(": ")[1].startswith('"')
                else [
                    [
                        int(token) for token in subrule.split()
                    ]
                    for subrule in rule.split(": ")[1].split("|")
                ]
            )
        for rule in inp.strip().split("\n\n")[0].split("\n")
    },
    # []cases
    inp.strip().split("\n\n")[1].split("\n"),
)

import re


@problem.solver(part=1)
def p1_naive(inp):
    # This is a very naive approach to Part 1; it just assembles regular
    # expressions that match each rule.
    rules, cases = inp

    expressions = {}
    while 0 not in expressions.keys():
        for rule, pattern in rules.items():
            if rule in expressions.keys():
                continue

            # assemble a regex that will match that rule number
            if type(pattern) is str:
                expressions[rule] = pattern
            else:
                # otherwise, if all the "subrules" have been resolved, then
                # assemble this rule
                if any(
                    any(token not in expressions.keys() for token in subrule)
                    for subrule in pattern
                ):
                    continue

                expressions[rule] = (
                    "("
                    + "|".join(
                        "".join(expressions[token] for token in subrule)
                        for subrule in pattern
                    )
                    + ")"
                )

    expression = re.compile(expressions[0])
    return sum(1 if re.fullmatch(expression, case) else 0 for case in cases)


@problem.solver(part=2)
def p2_smart(inp):
    # During the competition, I just modified Part 1 to recurse the
    # rule-application a few times before checking for matches. I have
    # re-written the solution "the right way" (for posterity.)
    #
    # If you remove the patched instructions below, it'll run as if it were
    # solving Part 1.
    rules, cases = inp

    # apply patches
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    def match(S, pattern=[0]):
        if len(pattern) <= 0:
            return not S

        car, *cdr = pattern
        if type(rules[car]) is str:
            return S.startswith(rules[car]) and match(S[1:], cdr)
        else:
            return any(match(S, subrule + cdr) for subrule in rules[car])

    return sum(1 if match(case) else 0 for case in cases)


if __name__ == "__main__":
    problem.solve()
