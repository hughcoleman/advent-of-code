#!/usr/bin/env python3
""" 2022/21: Monkey Math """

import operator
import sys
import z3

monkeys = [
    (monkey.split(": ")[0], monkey.split(": ")[1].split())
        for monkey in sys.stdin.read().strip().split("\n")
]

# Let's hand-roll Part 1, but we'll (ab)use z3 for Part 2.
V = {
    a: int(b[0])
        for a, b in monkeys
        if len(b) == 1
}
while "root" not in V.keys():
    for a, b in monkeys:
        if a in V.keys():
            continue

        l, op, r = b
        if (l in V.keys()) and (r in V.keys()):
            ops = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv
            }
            V[a] = int(ops.get(op)(V.get(l), V.get(r)))

print("Part 1:", V.get("root"))

s = z3.Solver()
for a, b in monkeys:
    if len(b) == 1 and a != "humn":
        s.add(z3.Real(a) == int(b[0]))
    elif len(b) == 3:
        l, op, r = b
        if a != "root":
            s.add(z3.Real(a) == ops.get(op)(z3.Real(l), z3.Real(r)))
        else:
            s.add(z3.Real(l) == z3.Real(r))

assert s.check() == z3.sat
model = s.model()
print("Part 2:", model[z3.Real("humn")].as_long())
