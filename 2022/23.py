#!/usr/bin/env python3
""" 2022/23: Unstable Diffusion """

import collections as cl
import itertools as it
import sys

# Since the y-axis is flipped, north is down.
N, E = complex(0, -1), complex(1, 0)
S, W = -N, -E
P = [
    (N, N + E, N + W),
    (S, S + E, S + W),
    (W, N + W, S + W),
    (E, N + E, S + E),
]

elves = set(
    complex(x, y)
        for y, ln in enumerate(sys.stdin.read().strip().split("\n"))
        for x, c in enumerate(ln)
        if c == "#"
)
for i in it.count(1):
    mv = {}
    for elf in elves:
        if all(elf + d not in elves for d in (N, N + E, E, S + E, S, S + W, W, N + W)):
            continue

        for p in P:
            if all(elf + d not in elves for d in p):
                mv[elf] = elf + p[0]
                break

    if len(mv) == 0:
        print("Part 2:", i)
        break

    mv0 = cl.Counter(mv.values())
    for d, v in mv0.items():
        if v == 1:
            elves.remove(next(k for k, v in mv.items() if v == d))
            elves.add(d)

    P = P[1:] + P[:1]

    # Part 1: How much ground, after 10 rounds?
    if i == 10:
        mx, *_, Mx = sorted(int(elf.real) for elf in elves)
        my, *_, My = sorted(int(elf.imag) for elf in elves)
        print("Part 1:", (Mx - mx + 1) * (My - my + 1) - len(elves))
