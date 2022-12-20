#!/usr/bin/env python3
""" 2022/20: Grove Positioning System """

import collections as cl
import sys

message = list(
    enumerate(map(int, sys.stdin.read().strip().split()))
)
for i, x in message * 1:
    j = message.index((i, x))
    message.pop(j)
    message.insert((j + x) % len(message), (i, x))

i = next(i for i, (_, x) in enumerate(message) if x == 0)
print("Part 1:", sum(
    message[(i + 1000*p) % len(message)][1] for p in (1, 2, 3)
))

message = [
    (i, x * 811589153)
        for i, x in sorted(message) # We need to restore the message!
]
for i, x in message * 10:
    j = message.index((i, x))
    message.pop(j)
    message.insert((j + x) % len(message), (i, x))

i = next(i for i, (_, x) in enumerate(message) if x == 0)
print("Part 2:", sum(
    message[(i + 1000*p) % len(message)][1] for p in (1, 2, 3)
))
