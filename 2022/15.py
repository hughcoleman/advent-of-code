#!/usr/bin/env python3
""" 2022/15: Beacon Exclusion Zone """

import re
import sys
import z3

observations = [
    tuple(map(int, re.findall(r"-?\d+", observation)))
        for observation in sys.stdin.read().strip().split("\n")
]

# Part 1 can be solved by identifying the intervals that each sensor covers
# along y=2000000.
X = []
for sx, sy, bx, by in observations:
    d = abs(sx - bx) + abs(sy - by) - abs(sy - 2000000)
    if d >= 0:
        X.append((sx - d, sx + d))

print("Part 1:", len(
    # At some point, remind me to re-write this using interval sets.
    set.union(
        *[set(range(a, b + 1)) for a, b in X]
    )
    # Don't forget to exclude known beacon positions!
    - set(bx for *_, bx, by in observations if by == 2000000)
))

# There are a number of very clever insights on Reddit regarding Part 2. I
# particularily enjoyed u/bluepichu's. I, however, propose a much more brute
# solution.
s = z3.Solver()
x, y = z3.Int("x"), z3.Int("y")

s.add(0 <= x); s.add(x <= 4000000)
s.add(0 <= y); s.add(y <= 4000000)

def z3_abs(x):
    return z3.If(x >= 0, x, -x)

for sx, sy, bx, by in observations:
    m = abs(sx - bx) + abs(sy - by)
    s.add(z3_abs(sx - x) + z3_abs(sy - y) > m)
    
assert s.check() == z3.sat
model = s.model()
print("Part 2:", model[x].as_long() * 4000000 + model[y].as_long())
