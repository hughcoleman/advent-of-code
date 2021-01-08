#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/01: Inverse Captcha")
problem.preprocessor = ppr.digits


@problem.solver(part=1)
def p1(digits):
    return sum(
        d1 for d1, d2 in zip(digits, digits[1:] + digits[:1]) if d1 == d2
    )


@problem.solver(part=2)
def p2(digits):
    return sum(
        d1 for d1, d2 in
        zip(digits, digits[len(digits) // 2:] + digits[:len(digits) // 2])
        if d1 == d2
    )


if __name__ == "__main__":
    problem.solve()
