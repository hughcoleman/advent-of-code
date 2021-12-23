#!/usr/bin/env python3
""" 2021/21: Dirac Dice """

import sys
import collections as cl
import itertools as it
import re

_, p1, _, p2 = re.findall(r"\d+", sys.stdin.read())
p1, p2 = int(p1), int(p2)

die = it.count()
def roll3():
    return sum(next(die) % 100 + 1 for _ in range(3))

_p1, _p2, s1, s2 = p1 - 1, p2 - 1, 0, 0
while True:
    _p1 = (_p1 + roll3()) % 10
    s1 = s1 + _p1 + 1
    if s1 >= 1000:
        break

    _p2 = (_p2 + roll3()) % 10
    s2 = s2 + _p2 + 1
    if s2 >= 1000:
        break

print("Part 1:", min(s1, s2) * next(die))

rolls = cl.Counter(
    sum(roll) for roll in it.product([1, 2, 3], repeat=3)
)

memo = {}
def play(p1, p2, s1=0, s2=0):
    if s1 >= 21 or s2 >= 21:
        return (s1 >= 21, s2 >= 21)

    if (p1, p2, s1, s2) not in memo:
        w1, w2 = 0, 0
        for roll, frequency in rolls.items():
            _p1 = (p1 + roll) % 10
            _w1, _w2 = play(p2, _p1, s2, s1 + _p1 + 1)
            w1, w2 = w1 + _w2*frequency, w2 + _w1*frequency

        memo[p1, p2, s1, s2] = (w1, w2)

    return memo[p1, p2, s1, s2]

print("Part 2:", max(play(p1 - 1, p2 - 1)))
