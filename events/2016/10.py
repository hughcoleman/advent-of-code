#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/10: Balance Bots")
problem.preprocessor = ppr.lsv


import collections as cl
import dataclasses as dc
import functools


@dc.dataclass
class Node:
    lo, hi = None, None
    inputs: set = dc.field(default_factory=set)


@problem.solver()
def solve(connections):
    nodes = cl.defaultdict(lambda: Node())
    for connection in connections:
        if connection.startswith("value"):
            _, n, _, _, _, bot = connection.split(" ")
            nodes["bot" + bot].inputs.add(int(n))
        elif connection.startswith("bot"):
            _, bot, _, _, _, lo_t, lo, _, _, _, hi_t, hi = connection.split(
                " "
            )

            nodes["bot" + bot].lo = lo_t + lo
            nodes["bot" + bot].hi = hi_t + hi
        else:
            raise RuntimeError('couldn\'t understand "{}"'.format(connection))

    while (
        len(nodes["output0"].inputs) <= 0
        or len(nodes["output1"].inputs) <= 0
        or len(nodes["output2"].inputs) <= 0
    ):
        for identifier, node in list(nodes.items()):
            # if the node is a bot, and we have enough inputs to forward, then
            # forward to the appropriate destinations
            if identifier.startswith("bot") and len(node.inputs) >= 2:
                nodes[node.lo].inputs.add(min(node.inputs))
                nodes[node.hi].inputs.add(max(node.inputs))

                # is this is the "special" bot (that compares value-17
                # microchips against value-61 microchips)?
                if node.inputs.issubset({17, 61}):
                    special = identifier.replace("bot", "")

                del nodes[identifier]

    outputs = set.union(
        nodes["output0"].inputs,
        nodes["output1"].inputs,
        nodes["output2"].inputs,
    )

    return (special, functools.reduce(lambda x, y: x * y, outputs))


if __name__ == "__main__":
    problem.solve()
