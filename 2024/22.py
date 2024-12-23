#!/usr/bin/env python3
""" 2024/22: Monkey Market """

import collections as cl
import itertools as it
import sys

def prng(S):
    while True:
        yield S
        S = (S ^ (S <<  6)) & 0xffffff
        S = (S ^ (S >>  5)) & 0xffffff
        S = (S ^ (S << 11)) & 0xffffff

assert next(it.islice(prng(1), 2000, 2001)) == 8685429

sequences = [
    list(it.islice(prng(int(s)), 0, 2001))
        for s in sys.stdin.read().strip().split("\n")
]
print("Part 1:", sum(sequence[-1] for sequence in sequences))

patterns = cl.defaultdict(int)
for sequence in sequences:
    deltas = [
        (s2 % 10) - (s1 % 10) for (s1, s2) in it.pairwise(sequence)
    ]

    # For each four-tuple, if we're yet to see it, record it.
    S = set()
    for i in range(len(sequence) - 4):
        pattern = tuple(deltas[i:i + 4])
        if pattern not in S:
            patterns[pattern] = patterns[pattern] + sequence[i + 4] % 10
            S.add(pattern)

print("Part 2:", max(patterns.values()))
