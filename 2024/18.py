#!/usr/bin/env python3
""" 2024/18: RAM Run """

import itertools as it
import networkx as nx
import sys

coordinates = [
    tuple(map(int, ln.split(",")))
        for ln in sys.stdin.read().strip().split("\n")
]

G = nx.Graph()
for x, y in it.product(range(71), repeat=2):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + dx < 71 and 0 <= y + dy < 71:
            G.add_edge((x, y), (x + dx, y + dy))

# We'll assume that the problem is well-defined; that is, none of the first
# 1024 coordinates break connectivity.
p2 = False
for i, coordinate in enumerate(coordinates):
    if i == 1024:
        print("Part 1:", nx.shortest_path_length(G, (0, 0), (70, 70)))
        p2 = True
    G.remove_node(coordinate)
    if p2 and not nx.has_path(G, (0, 0), (70, 70)):
        print("Part 2:", ",".join(map(str, coordinate)))
        break
