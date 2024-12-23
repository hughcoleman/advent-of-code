#!/usr/bin/env python3
""" 2024/23: LAN Party """

import itertools as it
import networkx as nx
import sys

G = nx.Graph(
    ln.split("-") for ln in sys.stdin.read().strip().split("\n")
)

Cs = list(nx.enumerate_all_cliques(G))

print("Part 1:", sum(len(C) == 3 and any(c.startswith("t") for c in C) for C in Cs))

assert len(Cs[-1]) > len(Cs[-2]) # unique maximal clique?
print("Part 2:", ",".join(sorted(Cs[-1])))
