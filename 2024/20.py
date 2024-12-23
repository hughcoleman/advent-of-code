#!/usr/bin/env python3
""" 2024/20: Race Condition """

import sys

racetrack = {
    (r, c): ch
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ch in enumerate(line)
}
(Sr, Sc), = ((r, c) for (r, c), ch in racetrack.items() if ch == "S")

# Compute the distance from `S` to every road tile.
distances, q = { (Sr, Sc): 0 }, [ (Sr, Sc) ]
while len(q):
    (r, c) = q.pop(0)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if racetrack.get((r + dr, c + dc)) != "#" and distances.get((r + dr, c + dc)) is None:
            distances[r + dr, c + dc] = distances[r, c] + 1
            q.append((r + dr, c + dc))

# Cheats are uniquely determined by their endpoints, so we can directly compute
# the time saved by looking at the distances to the endpoints of the cheats
# only.
solve = lambda D: sum(
    t1 - t0 - d >= 100
        for (r0, c0), t0 in distances.items()
        for (r1, c1), t1 in distances.items()
        if t1 - t0 >= 100 and (d := abs(r1 - r0) + abs(c1 - c0)) <= D
)
print("Part 1:", solve(2))
print("Part 2:", solve(20))
