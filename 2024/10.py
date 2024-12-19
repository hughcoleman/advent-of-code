#!/usr/bin/env python3
""" 2024/10: Hoof It """

import networkx as nx
import sys

area = {
    (r, c): int(ht)
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ht in enumerate(line)
}

G = nx.DiGraph(
    ((r, c), (r + dr, c + dc))
        for (r, c), d in area.items()
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if area.get((r + dr, c + dc)) == d + 1
)

trails = [
    list(nx.all_simple_paths(G, r0, r9))
        for r0 in filter(lambda n: area.get(n) == 0, G.nodes)
        for r9 in filter(lambda n: area.get(n) == 9, G.nodes)
]

print("Part 1:", sum(map(any, trails)))
print("Part 2:", sum(map(len, trails)))
