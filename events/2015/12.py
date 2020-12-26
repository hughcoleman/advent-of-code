#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/12: JSAbacusFramework.io")
problem.preprocessor = lambda document: json.loads(document)

import json


def subsum(O, blacklist=[]):
    if type(O) is int:
        return O

    elif type(O) is list:
        return sum(subsum(v, blacklist=blacklist) for v in O)

    elif type(O) is dict:
        # skip if contains blacklisted value
        for k, v in O.items():
            if k in blacklist or v in blacklist:
                return 0

        return sum(subsum(v, blacklist=blacklist) for v in O.values())

    elif type(O) is str:
        return 0

    else:
        raise RuntimeError("illegal value in object?")


@problem.solver()
def solve(document):
    p1 = subsum(document)
    p2 = subsum(document, blacklist=["red"])

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
