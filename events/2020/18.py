#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/18: Operation Order")
problem.preprocessor = ppr.lsv

import re


def shunting_yard(expression, precedence={}):
    rpn, operators = [], []

    tokens = re.findall(r"[0-9]+|[a-z]+|[\+\-\*\\\(\)]", expression)
    while len(tokens) > 0:
        token = tokens.pop(0)

        if token.isdigit():
            rpn.append(token)
        elif token in ["+", "-", "*", "/"]:
            while (
                len(operators) > 0
                and operators[-1] not in ["("]
                and precedence[operators[-1]] >= precedence[token]
            ):
                rpn.append(operators.pop())
            operators.append(token)
        elif token in ["("]:  # `in` because I'd like to expand this to handle
            # other types of parenthesis
            operators.append(token)
        elif token in [")"]:
            while len(operators) > 0 and operators[-1] != "(":
                rpn.append(operators.pop())
            operators.pop()

    while len(operators) > 0:
        rpn.append(operators.pop())

    # Now, evaluate the reverse-Polish/Lukasiewicz notated expression. This
    # probably could have been done during parsing, but I thought that it might
    # be "more handy" to separate the parsing/evaluation steps.
    result = []
    while len(rpn) > 0:
        token = rpn.pop(0)
        if token.isdigit():
            result.append(int(token))
        else:
            result.append(
                {
                    "+": lambda l, r: l + r,
                    "-": lambda l, r: r - l,  # subtration is non-commutative
                    "*": lambda l, r: l * r,
                    "/": lambda l, r: r // l,  # division is non-commutative
                }[token](result.pop(), result.pop())
            )

    return result[0]


@problem.solver()
def solve(expressions):
    p1, p2 = 0, 0
    for expression in expressions:
        p1 = p1 + shunting_yard(expression, precedence={"+": 1, "*": 1})
        p2 = p2 + shunting_yard(expression, precedence={"+": 2, "*": 1})

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
