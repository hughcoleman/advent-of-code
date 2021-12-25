#!/usr/bin/env python3
""" 2021/18: Snailfish """

import sys
import collections as cl
import functools as ft

Number = cl.namedtuple(
    "Number",
    [
        "l",    # = int | Number
        "r"     # = int | Number
    ]
)

numbers = list(
    eval(ln.replace("[", "Number(").replace("]", ")"))
        for ln in sys.stdin.read().strip().split("\n")
)

def add_l(n, a):
    if isinstance(n, int):
        return n + a
    return Number(add_l(n.l, a), n.r)

def add_r(n, a):
    if isinstance(n, int):
        return n + a
    return Number(n.l, add_r(n.r, a))

def explode(n, depth=0):
    if isinstance(n, Number):
        if depth == 4:
            assert \
                isinstance(n.l, int) and isinstance(n.r, int), \
                "Can't explode this pair."
            return True, (n.l, n.r), 0

        exploded, (l, r), child = explode(n.l, depth + 1)
        if exploded:
            return True, (l, None), Number(child, add_l(n.r, r) if r else n.r)

        exploded, (l, r), child = explode(n.r, depth + 1)
        if exploded:
            return True, (None, r), Number(add_r(n.l, l) if l else n.l, child)

    return False, (None, None), n

def split(n):
    if isinstance(n, int):
        if n >= 10:
            return True, Number(n // 2, (n + 1) // 2)
    else:
        splitted, child = split(n.l)
        if splitted:
            return True, Number(child, n.r)

        splitted, child = split(n.r)
        return splitted, Number(n.l, child)

    return False, n

def add(a, b):
    s = Number(a, b)
    while True:
        exploded, _, s = explode(s)
        if exploded:
            continue

        splitted, s = split(s)
        if not splitted:
            break

    return s

def magnitude(n):
    if isinstance(n, int):
        return n
    return 3*magnitude(n.l) + 2*magnitude(n.r)

print("Part 1:", magnitude(ft.reduce(add, numbers)))

print("Part 2:",
    max(
        magnitude(add(n1, n2))
            for i, n1 in enumerate(numbers)
            for j, n2 in enumerate(numbers)
            if i != j
    )
)
