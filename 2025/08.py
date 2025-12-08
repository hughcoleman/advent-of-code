#!/usr/bin/env python3
""" 2025/08: Playground """

import itertools as it
import math
import networkx as nx
import sys

junctions = [
    tuple(map(int, ln.split(",")))
        for ln in iter(sys.stdin.readline, "")
]
N = len(junctions)

edges = iter(sorted(
    it.combinations(range(N), 2),
    key=lambda ij: \
        sum((ci - cj)**2 for ci, cj in zip(junctions[ij[0]], junctions[ij[1]]))
))

G = nx.Graph(it.islice(edges, 1000))
G.add_nodes_from(range(N)) # need to add isolated vertices

print("Part 1:", math.prod(
    sorted(map(len, nx.connected_components(G)), reverse=True)[:3]
))

for i, j in edges:
    G.add_edge(i, j)
    if nx.is_connected(G):
        print("Part 2:", junctions[i][0] * junctions[j][0])
        break
else:
    assert False, "The graph is never connected."
