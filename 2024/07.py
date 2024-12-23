#!/usr/bin/env python3
""" 2024/07: Bridge Repair """

import re
import sys

equations = [
    list(map(int, re.findall("\d+", equation)))
        for equation in sys.stdin.read().strip().split("\n")
]

def test(X, xs, p2):
    if len(xs) == 1:
        return X == xs[0]
    else:
        x0, x1, xs = xs[0], xs[1], xs[2:]
        return (
            test(X, [x0 + x1] + xs, p2)
            or test(X, [x0 * x1] + xs, p2)
            or (p2 and test(X, [int(str(x0) + str(x1))] + xs, p2))
        )

print("Part 1:",
    sum(
        equation[0] for equation in equations
            if test(equation[0], equation[1:], False)
    )
)
print("Part 2:",
    sum(
        equation[0] for equation in equations
            if test(equation[0], equation[1:], True)
    )
)
