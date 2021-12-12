#!/usr/bin/env python3
""" 2021/09: Smoke Basin """

import sys
import math
import networkx as nx

depths = {
    (x, y): int(depth)
        for y, ln in enumerate(sys.stdin.read().strip().split("\n"))
        for x, depth in enumerate(ln.strip())
}

def neighbours(x, y):
    yield (x - 1, y)
    yield (x + 1, y)
    yield (x, y - 1)
    yield (x, y + 1)

print("Part 1:",
    sum(
        depth + 1
            for (x, y), depth in depths.items()
                if all(
                    depth < depths.get(neighbour, math.inf)
                        for neighbour in neighbours(x, y)
                )
    )
)

g = nx.Graph()
for (x, y), depth in depths.items():
    if depth == 9:
        continue

    for neighbour in neighbours(x, y):
        if depths.get(neighbour, 9) != 9:
            g.add_edge((x, y), neighbour)

basins = sorted(
    len(basin) for basin in nx.connected_components(g)
)

print("Part 2:", basins[-3] * basins[-2] * basins[-1])
