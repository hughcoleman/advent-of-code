#!/usr/bin/env python3
""" 2024/06: Guard Gallivant """

import sys

lab = {
    (r, c): ch
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ch in enumerate(line)
}
lab_obstructions = set((r, c) for (r, c), ch in lab.items() if ch == "#")

def walk(r, c, lab_obstructions):
    dr, dc = -1, 0
    visited = set()
    seen = set()
    while True:
        if not lab.get((r, c)):
            return visited
        if (r, c, dr, dc) in seen:
            return True
        visited.add((r, c))
        seen.add((r, c, dr, dc))

        if (r + dr, c + dc) in lab_obstructions:
            dr, dc = dc, -dr
        else:
            r, c = r + dr, c + dc

r0, c0 = next((r, c) for (r, c), ch in lab.items() if ch == "^")
visited = walk(r0, c0, lab_obstructions)
print("Part 1:", len(visited))
print("Part 2:",
    sum(
        walk(r0, c0, lab_obstructions | { (r, c) }) == True
            for r, c in visited
            if r != r0 or c != c0
    )
)

