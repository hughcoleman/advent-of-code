#!/usr/bin/env python3
""" 2021/15: Chiton """

import sys
import networkx as nx

risk = {
    (x, y): int(v)
        for y, ln in enumerate(sys.stdin.read().strip().split("\n"))
        for x, v in enumerate(ln)
}
w, h = max(x for x, y in risk.keys()) + 1, max(y for x, y in risk.keys()) + 1

g = nx.DiGraph()
for x, y in risk.keys():
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (x + dx, y + dy) in risk.keys():
            g.add_edge((x, y), (x + dx, y + dy), weight=risk[x + dx, y + dy])

print("Part 1:",
    nx.shortest_path_length(g, (0, 0), (w - 1, h - 1), weight="weight")
)

g = nx.DiGraph()
for x in range(5 * w):
    for y in range(5 * h):
        cost = (risk[x % w, y % h] - 1 + (x // w) + (y // h)) % 9 + 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < 5 * w and 0 <= y + dy < 5 * h:
                g.add_edge((x + dx, y + dy), (x, y), weight=cost)

print("Part 2:",
    nx.shortest_path_length(g, (0, 0), (5*w - 1, 5*h - 1), weight="weight")
)
