#!/usr/bin/env python3
""" 2022/13: Distress Signal """

import functools as ft
import json
import math
import sys

packets = [
    json.loads(packet)
        for packet in sys.stdin.read().strip().split()
]

def cmp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return (l > r) - (r > l)
    elif isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            k = cmp(l[i], r[i])
            if k != 0:
                return k
        return cmp(len(l), len(r))
    else:
        l = [ l ] if isinstance(l, int) else l
        r = [ r ] if isinstance(r, int) else r
        return cmp(l, r)
    
print("Part 1:", sum(
    i // 2 + 1
        for i in range(0, len(packets), 2)
        if cmp(packets[i], packets[i + 1]) < 0
))

packets.append([[2]])
packets.append([[6]])
packets.sort(key = ft.cmp_to_key(cmp))

print("Part 2:", math.prod(
    i for i, packet in enumerate(packets, 1)
        if packet in ([[2]], [[6]])
))