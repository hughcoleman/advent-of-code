#!/usr/bin/env python3
""" 2024/12: Garden Groups """

import sys

farm = {
    (r, c): ch
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ch in enumerate(line)
}

# Determine the connected components.
regions = { p: set([ p ]) for p in farm.keys() }
for (r, c), ch in farm.items():
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if farm.get((r + dr, c + dc)) == ch:
            regions[r, c] |= regions[r + dr, c + dc]
            for p in regions[r, c]:
                regions[p] = regions[r, c]
regions = set(map(tuple, regions.values()))

def edges(region):
    return [
        (r, c, dr, dc)
            for r, c in region
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if (r + dr, c + dc) not in region
    ]

def sides(region):
    E = edges(region)
    return [
        (r, c, dr, dc)
            for r, c, dr, dc in E
            if (r, c, -dc, dr) in E or (r + dr - dc, c + dc + dr, dc, -dr) in E
    ]

print("Part 1:", sum(len(region) * len(edges(region)) for region in regions))
print("Part 2:", sum(len(region) * len(sides(region)) for region in regions))
