#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/24: Electromagnetic Moat")
problem.preprocessor = lambda components: [
    tuple(int(port) for port in component.split("/"))
    for component in components.strip().split("\n")
]


import collections as cl


def build(components, foundation=(0, 0, set(), 0)):
    l, s, bridge, a = foundation

    for b in components[a]:
        if not ((a, b) in bridge or (b, a) in bridge):
            n = (l + 1, s + a + b, (bridge | {(a, b)}), b)

            yield n
            yield from build(components, foundation=n)


@problem.solver()
def solve(ports):
    # create a dictionary of all possible component port arrangements
    components = cl.defaultdict(set)
    for front, back in ports:
        components[front].add(back)
        components[back].add(front)

    # find strongest and longest bridges
    strongest, longest = (0, 0), (0, 0)
    for bridge in build(components):
        l, s, _, _ = bridge

        strongest = (    (l, s)         if s > strongest[1] 
                    else strongest
                    )
        longest   = (    (l, s)         if (l > longest[0]) or
                                           (l == longest[0] and s > longest[1])
                    else longest
                    )

    return (strongest[1], longest[1])


if __name__ == "__main__":
    problem.solve()
