#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/09: All in a Single Night")
problem.preprocessor = ppr.lsv

import collections as cl
import itertools as it
import math


@problem.solver()
def tsp(inp):
    distances = cl.defaultdict(dict)
    for ln in inp:
        origin, _, destination, _, distance = ln.split(" ")

        distances[origin][destination] = int(distance)
        distances[destination][origin] = int(distance)

    # only seven places to visit; a brute-force is probably fast enough
    shortest, longest = math.inf, -math.inf
    for sequence in it.permutations(distances.keys()):
        distance = 0
        for l1, l2 in zip(sequence, sequence[1:]):
            distance = distance + distances[l1][l2]

        shortest = min(shortest, distance)
        longest = max(longest, distance)

    return (shortest, longest)


if __name__ == "__main__":
    problem.solve()
