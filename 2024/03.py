#!/usr/bin/env python3
""" 2024/03: Mull It Over """

import re
import sys

program = sys.stdin.read()

p1, p2 = 0, 0
s = True
for o, arg1, arg2 in re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", program):
    if o == "do()":
        s = True
    elif o == "don't()":
        s = False
    else:
        p1 = p1 + int(arg1)*int(arg2)
        if s:
            p2 = p2 + int(arg1)*int(arg2)

print("Part 1:", p1)
print("Part 2:", p2)
