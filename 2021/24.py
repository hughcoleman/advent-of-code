#!/usr/bin/env python3
""" 2021/24: Arithmetic Logic Unit """

import sys
import re

monad = [
    tuple(map(int, x))
        for x in re.findall(
            (
                "inp w"         "\n"
                "mul x 0"       "\n"
                "add x z"       "\n"
                "mod x 26"      "\n"
                "div z (1|26)"  "\n"
                "add x (-?\d+)" "\n"
                "eql x w"       "\n"
                "eql x 0"       "\n"
                "mul y 0"       "\n"
                "add y 25"      "\n"
                "mul y x"       "\n"
                "add y 1"       "\n"
                "mul z y"       "\n"
                "mul y 0"       "\n"
                "add y w"       "\n"
                "add y (\d+)"   "\n"
                "mul y x"       "\n"
                "add z y"       "\n?"
            ),
            sys.stdin.read()
        )
]

# Determine the constraints that our program imposes.
constraints = []

stack = []
for i, (divisor, a, b) in enumerate(monad):
    if divisor == 1:
        assert a >= 10
        stack.append((i, b))
    else:
        assert a <= 0
        _i, _b = stack.pop()
        constraints.append(((_i, i), _b + a))

assert len(stack) == 0

def reverse(constraints, f):
    number = [
        None for _ in range(14)
    ]
    for (a, b), d in constraints:
        number[a], number[b] = f(
            (i, i + d)
                for i in range(1, 10)
                if 0 < (i + d) < 10
        )

    return "".join(str(n) for n in number)

print("Part 1:", reverse(constraints, max))
print("Part 2:", reverse(constraints, min))
