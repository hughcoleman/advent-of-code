#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/04: The Ideal Stocking Stuffer")
problem.preprocessor = ppr.identity

import hashlib


def ac_miner(key):
    # initial number of leading zeroes required is five.
    lead = 5

    i = 0
    while True:
        token = (key + str(i)).encode()
        if hashlib.md5(token).hexdigest().startswith("0" * lead):
            yield i
            lead = lead + 1
        i = i + 1


@problem.solver()
def solve(key):
    miner = ac_miner(key.strip())

    return (next(miner), next(miner))


if __name__ == "__main__":
    problem.solve()
