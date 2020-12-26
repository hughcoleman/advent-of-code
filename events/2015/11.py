#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/11: Corporate Policy")
problem.preprocessor = ppr.identity

import re
from string import ascii_lowercase


def increment(password):
    # find base-10 representation of base-26 password
    n = 0
    for i, character in enumerate(password[::-1]):
        n = n + ascii_lowercase.index(character) * pow(26, i)

    # increment one character
    n = n + 1

    # reconstruct
    s = ""
    while n > 0:
        s = ascii_lowercase[n % 26] + s
        n = n // 26

    return s


def valid(password):
    return (
        any(
            ord(c1) + 2 == ord(c2) + 1 == ord(c3)
            for c1, c2, c3 in zip(password, password[1:], password[2:])
        )
        and all(confusing not in password for confusing in ["i", "o", "l"])
        and bool(re.search(r"(.)\1.*(.)\2", password))
    )


@problem.solver()
def solve(password):
    while not valid(password):
        password = increment(password)

    p1 = password

    password = increment(password)
    while not valid(password):
        password = increment(password)

    p2 = password

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
