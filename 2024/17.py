#!/usr/bin/env python3
""" 2024/17: Chronospatial Computer """

import re
import sys
from z3 import *

A, B, C, *program = map(int, re.findall(r"\d+", sys.stdin.read()))

# Handling of the combo operand isn't entirely correct, here. But it'll do.
ip, out = 0, []
while ip < len(program):
    arg = program[ip + 1]
    match program[ip]:
        case 0: A >>= { 4: A, 5: B, 6: C }.get(arg, arg)
        case 1: B  ^= arg
        case 2: B   = { 4: A, 5: B, 6: C }.get(arg, arg) % 8
        case 3: ip  = arg - 2 if A != 0 else ip
        case 4: B  ^= C
        case 5: out.append({ 4: A, 5: B, 6: C }.get(arg, arg) % 8)
        case 6: B   = A >> { 4: A, 5: B, 6: C }.get(arg, arg)
        case 7: C   = A >> { 4: A, 5: B, 6: C }.get(arg, arg)
    ip = ip + 2
print("Part 1:", ",".join(map(str, out)))

# For Part 2, we'll use z3. This is currently hard-coded to my input; it would
# be nice to generalise it at some point.
o = Optimize()
i = BitVec("i", 64)
o.minimize(i)

A, B, C = i, 0, 0
for p in program:
    B   = A % 8
    B  ^= 5
    C   = A >> B
    B  ^= 6
    A >>= 3
    B  ^= C
    o.add((B % 8) == p)
o.add(A == 0)

assert o.check() == sat
print("Part 2:", o.model()[i])
