#!/usr/bin/python3
""" 2021/22: Reactor Reboot """

import sys
import collections as cl
import itertools as it
import re

steps = [
    (action == "on", tuple(map(int, bounds)))
        for action, *bounds in re.findall(
            r"(.*) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", sys.stdin.read()
        )
]

reactor = cl.defaultdict(bool)
for action, bounds in steps:
    min_x, max_x, min_y, max_y, min_z, max_z = bounds

    assert min_x <= max_x
    assert min_y <= max_y
    assert min_z <= min_z

    for x, y, z in it.product(
        range(max(min_x, -50), min(max_x + 1, 50)),
        range(max(min_y, -50), min(max_y + 1, 50)),
        range(max(min_z, -50), min(max_z + 1, 50))
    ):
        reactor[x, y, z] = action

print("Part 1:", sum(reactor.values()))

def volume(cuboid):
    min_x, max_x, min_y, max_y, min_z, max_z = cuboid

    return (
        max(max_x - min_x + 1, 0)
      * max(max_y - min_y + 1, 0)
      * max(max_z - min_z + 1, 0)
    )

reactor = {}
for action, bounds in steps:
    min_x, max_x, min_y, max_y, min_z, max_z = bounds

    reactions = cl.defaultdict(int)
    for (bmin_x, bmax_x, bmin_y, bmax_y, bmin_z, bmax_z), bsgn in reactor.items():
        intersection = (
            max(min_x, bmin_x), min(max_x, bmax_x),
            max(min_y, bmin_y), min(max_y, bmax_y),
            max(min_z, bmin_z), min(max_z, bmax_z)
        )
        if volume(intersection) > 0:
            reactions[intersection] -= bsgn

    if action:
        reactions[bounds] += 1

    reactor = {
        k: reactor.get(k, 0) + reactions.get(k, 0)
            for k in it.chain.from_iterable((reactor.keys(), reactions.keys()))
    }

print("Part 2:",
    sum(
        sgn * volume(bounds)
            for bounds, sgn in reactor.items()
    )
)
