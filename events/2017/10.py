#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/10: Knot Hash")
problem.preprocessor = ppr.csi


import functools


def kh(lengths, rounds=1):
    knot = list(range(0, 256))
    current, skip = 0, 0

    for _ in range(rounds):
        for length in lengths:
            for i in range(0, length // 2):
                a = (current + i) % 256
                b = (current + length - i - 1) % 256

                knot[a], knot[b] = knot[b], knot[a]

            current = current + length + skip
            skip = skip + 1

    return knot


@problem.solver()
def solve(lengths):
    p1 = kh(lengths)
    p2 = kh(
        [ord(c) for c in ",".join(str(l) for l in lengths)]
        + [17, 31, 73, 47, 23],
        rounds=64,
    )

    dense = []
    for i in range(0, 256, 16):
        dense.append(functools.reduce(lambda l, r: l ^ r, p2[i : i + 16]))

    return (p1[0] * p1[1], "".join(hex(b)[2:].zfill(2) for b in dense))


if __name__ == "__main__":
    problem.solve()
