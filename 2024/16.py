#!/usr/bin/env python3
""" 2024/16: Reindeer Maze """

import networkx as nx
import sys

maze = {
    (r, c): ch
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ch in enumerate(line)
}

# Ah, we'll cheat...
G = nx.DiGraph()
for (r, c), ch in maze.items():
    if maze.get((r, c)) == "#":
        continue

    for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        G.add_edge((r, c, dr, dc), (r, c, -dc, dr), weight=1000)
        if maze.get((r + dr, c + dc)) != "#":
            G.add_edge((r, c, dr, dc), (r + dr, c + dc, dr, dc), weight=1)

S = next((r, c) for (r, c), ch in maze.items() if ch == "S")
E = next((r, c) for (r, c), ch in maze.items() if ch == "E")

for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    G.add_edge((*E, dr, dc), "end", weight=0)

print("Part 1:", nx.shortest_path_length(G, (*S, 0, 1), "end", "weight"))
print("Part 2:", len(set(
    (r, c)
        for path in nx.all_shortest_paths(G, (*S, 0, 1), "end", "weight")
        for (r, c, _, _) in path[:-1]
)))
