#!/usr/bin/env python3
""" 2024/11: Plutonian Pebbles """

import functools as ft
import sys

@ft.cache
def blink(N, t):
    if t == 0:
        return 1
    else:
        s = str(N)
        if N == 0:
            return blink(1, t - 1)
        elif len(s) % 2 == 0:
            a, b = int(s[:len(s) // 2]), int(s[len(s) // 2:])
            return blink(a, t - 1) + blink(b, t - 1)
        else:
            return blink(2024*N, t - 1)

stones = [int(s) for s in sys.stdin.read().strip().split(" ")]
print("Part 1:", sum(blink(s, 25) for s in stones))
print("Part 2:", sum(blink(s, 75) for s in stones))
