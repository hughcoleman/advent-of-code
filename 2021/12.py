#!/usr/bin/env python3
""" 2021/12: Passage Pathing """

import sys
import collections as cl

cave = cl.defaultdict(set)
for tunnel in sys.stdin.read().strip().split("\n"):
    e1, e2 = tunnel.split("-")

    cave[e1].add(e2)
    cave[e2].add(e1)

def p1(cave, position="start", visited=set()):
    return sum(
        p1(
            cave,
            d,
            visited=visited | {d}
        ) if d != "end" else 1
            for d in cave[position]
                # From here, we can proceed to any cell that is not the start,
                # or a small cave that we've already visited.
                if d != "start" and (d not in visited if d.islower() else True)
    )

def p2(cave, position="start", visited=set(), explored=False):
    return sum(
        p2(
            cave,
            d,
            visited=visited | {d},
            # If we've already explored a cell, or, if we're going to a small
            # cave we've already been to, then we can't explore any more.
            explored=explored or (d in visited if d.islower() else False)
        ) if d != "end" else 1
            for d in cave[position]
                if d != "start" and (
                    (d not in visited) or (not explored)
                        if d.islower() else True
                )
    )

print("Part 1:", p1(cave))
print("Part 2:", p2(cave))
