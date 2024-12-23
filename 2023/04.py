#!/usr/bin/env python3
""" 2023/04: Scratchcards """

import sys

# We'll assume that the cards are given in order, nothing skipped, etc.
cards = [
    tuple(map(lambda k: set(k.split()), card.split(": ")[1].split(" | ")))
        for card in sys.stdin.readlines()
]

p1 = 0
m = [1] * len(cards)
for i, (ca, cb) in enumerate(cards):
    n = len(ca & cb)

    # The score is 2^(n - 1) if n > 0. This is a bit ugly, but we can compute
    # this without a branch using some bit-shifting.
    p1 = p1 + ((1 << n) >> 1)

    for j in range(i + 1, min(len(cards), i + n + 1)):
        m[j] += m[i]

print("Part 1:", p1)
print("Part 2:", sum(m))
