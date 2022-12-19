#!/usr/bin/env python3
""" 2022/10: Cathode-Ray Tube """

import itertools as it
import sys

instructions = (
    instruction.split() for instruction in sys.stdin.read().strip().split("\n")
)

X, x = 1, None

S = 0
crt = [[" "] * 40 for _ in range(6)]
for cycle in it.count(1):
    if cycle in (20, 60, 100, 140, 180, 220):
        S = S + cycle * X
    
    k = cycle - 1
    if abs((k % 40) - X) <= 1:
        crt[k // 40][k % 40] = "#"
    
    # Now, we can handle the instruction.
    if x is not None:
        X, x = X + x, None
    else:
        try:
            op, *args = next(instructions)
        except StopIteration:
            break
        
        x = int(args[0]) if op == "addx" else None

print("Part 1:", S)
print("Part 2:")
print("\n".join("".join(ln) for ln in crt))