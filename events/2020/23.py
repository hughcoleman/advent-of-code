#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2020/23: Crab Cups")
problem.preprocessor = ppr.digits

import array

@problem.solver(part=1)
def small(cups):
    for move in range(100):
        # pickup three cups after the first
        pickup = [cups.pop(1), cups.pop(1), cups.pop(1)]

        dest = cups[0] - 1
        while dest <= 0 or dest in pickup:
            if dest <= 0:
                dest = 9
            else:
                dest = dest - 1

        idx = cups.index(dest)
        for cup in pickup[::-1]:
            cups.insert(idx + 1, cup)

        cups.append(cups.pop(0))

    cups = cups[cups.index(1) + 1 :] + cups[: cups.index(1)]
    return "".join(str(cup) for cup in cups)

@problem.solver(part=2)
def large(initial):
    cups = array.array("I", range(1, 1_000_000 + 2))

    cups[0] = 999999999 # cups are indexed by 1, so set this to an illegal cup
                        # value so that if it ever comes up we'll know we have
                        # an off-by-one error somewhere
    for cup, successor in zip(initial, initial[1:] + [10]):
        cups[cup] = successor
    cups[-1] = initial[0]

    current = initial[0]
    for move in range(10_000_000):
        # pickup cups
        c1 = cups[current]
        c2 = cups[c1]
        c3 = cups[c2]

        # find destination
        dest = current - 1
        while (dest <= 0) or dest in {c1, c2, c3}:
            if dest <= 0:
                dest = 1_000_000
            else:
                dest = dest - 1

        # sever the linked list...
        tail = cups[dest]

        # ...then stitch it back together
        cups[current] = cups[c3]
        cups[dest] = c1
        cups[c3] = tail

        current = cups[current]

    # give us back our stars!
    star = cups[1]
    return star * cups[star]

if __name__ == "__main__":
    problem.solve()
