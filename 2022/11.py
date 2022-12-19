#!/usr/bin/env python3
""" 2022/11: Monkey in the Middle """

import collections as cl
import copy
import math
import operator
import sys

def parse(expr):
    # A naive expression parser; just barely sufficient for the problem.
    lhs, op, rhs = expr.split()
    return (
        lambda x:
            (operator.add if op == "+" else operator.mul)
            (int(lhs) if lhs.isdigit() else x, int(rhs) if rhs.isdigit() else x)
    )

class Monkey:
    def __init__(self, inventory, op, modulus, a, d):
        self.inventory = list(inventory)
        self.op = op
        self.modulus = modulus
        self.a = a
        self.d = d
        
    @classmethod
    def from_str(cls, S):
        S = S.split("\n")
        return cls(
            map(int, S[1][18:].split(", ")),
            parse(S[2][19:]),
            int(S[3][21:]),
            int(S[4][29:]),
            int(S[5][30:])
        )
      
monkeys = [
    Monkey.from_str(m) for m in sys.stdin.read().strip().split("\n\n")
]

N = math.lcm(*(m.modulus for m in monkeys))
def play(monkeys, part = 1):
    activity = cl.Counter()
    for rnd in range([None, 20, 10000][part]):
        for i, monkey in enumerate(monkeys):
            activity[i] = activity[i] + len(monkey.inventory)
            while len(monkey.inventory) > 0:
                x = monkey.op(monkey.inventory.pop(0)) % N
                if part == 1:
                    x //= 3
                
                k = monkey.a if (x % monkey.modulus == 0) else monkey.d
                monkeys[k].inventory.append(x)

    return activity.most_common()[0][1] * activity.most_common()[1][1]
                
print("Part 1:", play(copy.deepcopy(monkeys)))
print("Part 2:", play(monkeys, part = 2))
