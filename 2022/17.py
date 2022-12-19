#!/usr/bin/env python3
""" 2022/17: Pyroclastic Flow """

import itertools as it
import sys

jets = enumerate(it.cycle(sys.stdin.read().strip()))
rocks = enumerate(it.cycle([
    set([
        0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j,
    ]),
    set([
                1 + 2j,
        0 + 1j, 1 + 1j, 2 + 1j,
                1 + 0j,
    ]),
    set([
                        2 + 2j,
                        2 + 1j,
        0 + 0j, 1 + 0j, 2 + 0j,
    ]),
    set([
        0 + 3j,
        0 + 2j,
        0 + 1j,
        0 + 0j,
    ]),
    set([
        0 + 1j, 1 + 1j,
        0 + 0j, 1 + 0j,
    ])
]))

def translate(X, d=0 + 0j):
    return set(x + d for x in X)

tower = set(
    # Monkey-patch a "floor" - this eliminates an edge-case for the first
    # couple rocks dropped.
    complex(i, 0) for i in range(7)
)
h = 0
i, j = 0, 0

_seen = {}
while True:
    i, rock = next(rocks)
    if i == 2022:
        print("Part 1:", h)

    # To detect loops, hash the previous seven rows; this isn't 100% fool-proof
    # but is "good enough" for this puzzle. (A better way to do this would be
    # to hash the set of tiles that are directly "exposed to air."
    k = 0
    for y in range(h, h - 8, -1):
        for x in range(7):
            k = (k << 1) + int(complex(x, y) in tower)

    K = (i % 5, j % 10091, k)
    if K in _seen.keys():
        i0, h0 = _seen.get(K)

        # Are we in a cycle, at the same index as one trillion?
        modulus = i - i0
        if (1000000000000 - i) % modulus <= 0:
            print("Part 2:",
                (1000000000000 - i) // modulus * (h - h0) + h
            )
            break
    else:
        _seen[K] = (i, h)

    # Otherwise, tetris time!
    rock = translate(rock, complex(2, h + 4))
    while True:
        j, jet = next(jets)
        jet = { ">": 1, "<": -1 }[jet]

        # Shift horizontally, if nothing collides?
        rock0 = translate(rock, jet)
        if all(
            (0 <= r.real < 7) and (r not in tower)
                for r in rock0
        ):
            rock = rock0

        # Shift vertically, if nothing collides?
        rock0 = translate(rock, -1j)
        if all(rock not in tower for rock in rock0):
            rock = rock0
        else:
            tower |= rock
            break

    h = max(h, max(int(r.imag) for r in rock))
