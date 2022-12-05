#!/usr/bin/env python3
""" 2022/05: Supply Stacks """

import re
import sys

stacks, instructions = sys.stdin.read().split("\n\n")

stacks = list(
    "".join(x).strip()[1:]
        for i, x in enumerate(
            zip(*map(list, stacks.split("\n")[::-1]))
        )
        if i % 4 == 1
)
instructions = [
    tuple(map(int, re.findall(r"\d+", instruction)))
        for instruction in instructions.strip().split("\n")
]
    
def cratemover(m9001 = False):
    _stacks = [ None ] + stacks[:]
    for N, a, b in instructions:
        _stacks[a], m = _stacks[a][:-N], _stacks[a][-N:]
        if not m9001:
            m = m[::-1]
        _stacks[b] = _stacks[b] + m
        
    return "".join(stack[-1] for stack in _stacks[1:])
    
print("Part 1:", cratemover())
print("Part 2:", cratemover(True))
