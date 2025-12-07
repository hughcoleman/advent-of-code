#!/usr/bin/env python3
""" 2025/07: Laboratories """

import collections as cl
import itertools as it
import sys

manifold = [
    ln.strip() for ln in iter(sys.stdin.readline, "")
]

p1 = 0
def f(beams, splitters):
    beams_ = cl.defaultdict(int)
    for i, ch in enumerate(splitters):
        if ch == "S":
            beams_[i] = 1
        elif ch == "^":
            if beams[i]:
                global p1
                p1 = p1 + 1
            beams_[i - 1] = beams_[i - 1] + beams[i]
            beams_[i + 1] = beams_[i + 1] + beams[i]
        else:
            beams_[i] = beams_[i] + beams[i]
    return beams_

*_, q = it.accumulate(manifold, f, initial=cl.defaultdict(int))
print("Part 1:", p1)
print("Part 2:", sum(q.values()))
