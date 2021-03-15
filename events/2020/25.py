#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib import *

problem = aoc.Problem("2020/25: Combo Breaker")
problem.preprocessor = ppr.lsi

import math

MODULUS = 20201227

def dlp_bsgs(h):
    # use baby-step, giant-step to compute the discrete log
    N = math.ceil(math.sqrt(MODULUS - 1))

    t = {
        pow(7, exp, MODULUS): exp for exp in range(N)
    }

    c = pow(7, N * (MODULUS - 2), MODULUS)

    for j in range(N):
        y = (h * pow(c, j, MODULUS)) % MODULUS
        if y in t:
            return j * N + t[y] 

    return -1

@problem.solver()
def solve(keys):
    Ec, Ed = keys

    # Lc = invert(Ec)
    Ld = dlp_bsgs(Ed)

    # I should probably be checking to make sure that the keys match, but in
    # theory, they should, so I don't check.
    return (pow(Ec, Ld, MODULUS), "Merry Christmas!")


if __name__ == "__main__":
    problem.solve()
