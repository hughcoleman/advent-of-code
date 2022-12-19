#!/usr/bin/env python3
""" 2022/12: Hill Climbing Algorithm """

import networkx as nx
import sys

heightmap = {
    complex(x, y): c
        for y, ln in enumerate(sys.stdin.read().strip().split("\n"))
        for x, c in enumerate(ln)
}

# Locate S and E; replace them with `a` and `z`.
S = next(k for k, v in heightmap.items() if v == "S")
E = next(k for k, v in heightmap.items() if v == "E")
heightmap[S], heightmap[E] = "a", "z"

G = nx.DiGraph()
for xy, c in heightmap.items():
    for d in (1, -1, 1j, -1j):
        if ord(heightmap.get(xy + d, "{")) <= ord(c) + 1:
            G.add_edge(xy, xy + d)

H = nx.shortest_path_length(G, target = E)
print("Part 1:", H.get(S))
print("Part 2:", min(v for k, v in H.items() if heightmap[k] == "a"))
