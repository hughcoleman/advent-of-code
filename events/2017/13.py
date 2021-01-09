#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/13: Packet Scanners")
problem.preprocessor = lambda scanners: [
    tuple(int(i) for i in scanner.split(": "))
    for scanner in scanners.strip().split("\n")
]


@problem.solver()
def solve(scanners):
    severity = sum(
        (d * r) for d, r in scanners if d % (2 * (r - 1)) <= 0
    )

    # there's probably a clever, CRT-based algorithm that'll find the answer in
    # constant time, but I haven't worked it out yet
    delay = 0
    while any((delay + d) % (2 * (r - 1)) <= 0 for d, r in scanners):
        delay = delay + 1

    return (severity, delay)


if __name__ == "__main__":
    problem.solve()
