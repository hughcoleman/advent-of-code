#!/usr/bin/env python3
""" 2024/21: Keypad Conundrum """

import itertools as it
import functools as ft
import sys

NUMPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}
DIRPAD = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

# "What's the number of button presses required on pad 0 to move from `b1` to
# `b2` on pad `d` and press `b2` under the assumption that `b1` was just
# pressed?" 
@ft.cache
def move(d, b1, b2, num=False):
    if d == 0:
        return 1

    # The optimal path will always consist of only vertical motion followed by
    # only horizontal motion, or vice-versa. Hence, there are at most two paths
    # to consider between any two buttons on the pad.
    PAD = (NUMPAD if num else DIRPAD)
    r1, c1 = PAD[b1]
    r2, c2 = PAD[b2]
    dr, dc = r2 - r1, c2 - c1 
    def paths():
        if (r2, c1) in PAD.values(): yield ('v' if dr > 0 else '^')*abs(dr) + ('>' if dc > 0 else '<')*abs(dc)
        if (r1, c2) in PAD.values(): yield ('>' if dc > 0 else '<')*abs(dc) + ('v' if dr > 0 else '^')*abs(dr)

    return min(
        sum(move(d - 1, b1, b2) for b1, b2 in it.pairwise(f"A{path}A"))
            for path in paths()
    )

codes = sys.stdin.read().strip().split("\n")

solve = lambda d: sum(
    sum(move(d + 1, b1, b2, num=True) for b1, b2 in it.pairwise(f"A{code}")) * int(code.removesuffix("A"))
        for code in codes
)
print("Part 1:", solve(2))
print("Part 2:", solve(25))
