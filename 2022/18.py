#!/usr/bin/env python3
""" 2022/18: Boiling Boulders """

import sys

droplets = set(
    tuple(map(int, droplet.split(",")))
        for droplet in sys.stdin.read().strip().split("\n")
)

def neighbours(x, y, z):
    yield from (
        (x + dx, y + dy, z + dz)
            for dx, dy, dz in [
                # Can this be generated using itertools?
                (1, 0, 0), (-1,  0,  0),
                (0, 1, 0), ( 0, -1,  0),
                (0, 0, 1), ( 0,  0, -1),
            ]
    )
    
print("Part 1:", sum(
    1 for droplet in droplets
      for droplet0 in neighbours(*droplet)
      if droplet0 not in droplets
))

# For Part 2, we flood-fill starting from a point known to be outside the lava.
xm, *_, xM = sorted(droplet[0] for droplet in droplets)
ym, *_, yM = sorted(droplet[1] for droplet in droplets)
zm, *_, zM = sorted(droplet[2] for droplet in droplets)

S = set([
    # These points, for certain, are outside the lava. 
    (xm - 1, ym - 1, zm - 1),
    (xM + 1, yM + 1, zM + 1),
])
while True:
    S0 = set()
    for s in S:
        for s0 in neighbours(*s):
            x, y, z = s0
            if (
                s0 not in droplets
                and xm - 1 <= x <= xM + 1
                and ym - 1 <= y <= yM + 1
                and zm - 1 <= z <= zM + 1
            ):
                S0.add(s0)
    
    if all(s0 in S for s0 in S0):
        break
    S |= S0
    
print("Part 2:", sum(
    1 for droplet in droplets
      for droplet0 in neighbours(*droplet)
      if droplet0 in S
))
