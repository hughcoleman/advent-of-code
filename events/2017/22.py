#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/22: Sporifica Virus")
problem.preprocessor = lambda network: [
    [".#".index(c) for c in r] for r in network.strip().split("\n")
]


import collections as cl


@problem.solver(part=1)
def weakened(network):
    # find the set of infected cells
    infected = set()
    for y in range(len(network)):
        for x in range(len(network[y])):
            if network[y][x] >= 1:
                # track the infected cells, adjusted to the correct coordinate
                # system
                infected.add(
                    complex(x - len(network[y]) // 2, -y + len(network) // 2)
                )

    position, direction = 0, 1j

    infections = 0
    for burst in range(10000):
        direction *= {True: -1j, False: 1j}[position in infected]

        if position in infected:
            infected.remove(position)
        else:
            infected.add(position)
            infections = infections + 1

        position = position + direction

    return infections


@problem.solver(part=2)
def resistant(network):
    state = cl.defaultdict(lambda: 0)
    for y in range(len(network)):
        for x in range(len(network[y])):
            state[
                complex(x - len(network[y]) // 2, -y + len(network) // 2)
            ] = (0 if network[y][x] <= 0 else 2)

    position, direction = 0, 1j

    infections = 0
    for burst in range(10_000_000):
        direction *= {0: 1j, 1: 1, 2: -1j, 3: -1}[state[position]]

        state[position] = (state[position] + 1) % 4
        if state[position] == 2:
            infections = infections + 1

        position = position + direction

    return infections


if __name__ == "__main__":
    problem.solve()
