#!/usr/bin/env python3
""" 2024/24: Crossed Wires """

import itertools as it
import functools as ft
import sys
from z3 import *

inputs, gates = sys.stdin.read().strip().split("\n\n")
inputs = {
    i: True if c == "1" else False
        for i, c in map(lambda i: i.split(": "), inputs.split("\n"))
}
gates = {
    g: a.split()
        for a, g in map(lambda g: g.split(" -> "), gates.split("\n"))
}

def evaluator(inputs, swaps = {}):
    @ft.cache
    def _eval(register):
        if register in inputs.keys():
            return inputs[register]
        else:
            if register in swaps.keys():
                # The `swaps` dictionary contains both directions.
                register = swaps[register]

            arg1, op, arg2 = gates[register]
            match op:
                case "AND": return _eval(arg1) & _eval(arg2)
                case "OR" : return _eval(arg1) | _eval(arg2)
                case "XOR": return _eval(arg1) ^ _eval(arg2)

    return _eval

e = evaluator(inputs)
print("Part 1:", 
    ft.reduce(
        lambda acc, g: acc + (1 << int(g.removeprefix("z"))) * e(g),
        filter(lambda g: g.startswith("z"), gates.keys()),
        0
    )
)

# Identify the (least-significant) output bit whose definition is incorrect. We
# can find this by asking z3, for each bit i, if there exists x, y, and z such
# that x + y == z but z[i] != e(z[i]).
def find_smallest_error(swaps = {}):
    x, y, z = BitVecs("x y z", 45)
    inputs_x = {
        f"x{i:02d}": Extract(i, i, x) for i in range(45)
    }
    inputs_y = {
        f"y{i:02d}": Extract(i, i, y) for i in range(45)
    }
    e = evaluator(inputs_x | inputs_y, swaps=swaps)

    for i in range(45):
        s = Solver()
        s.add(x + y == z)
        s.add(e(f"z{i:02d}") != Extract(i, i, z))
        if s.check() == sat:
            return i
    else:
        # There exists no counterexample, ie. the derived expressions are
        # correct.
        print("Part 2:", ",".join(sorted(swaps.keys())))
        exit()

def descendants(register, swaps = {}):
    if register not in inputs.keys():
        yield register
        if register in swaps.keys():
            register = swaps[register]
            yield register 

        arg1, _, arg2 = gates[register]
        yield from descendants(arg1)
        yield from descendants(arg2)

# Identify a swap which increases the position of the least-significant
# incorrect output bit. We can reduce the search space by noticing that the
# registers that z[i0 - 1] depends on are necessarily correct, and that at
# least one of the registers that z[i0] depends on is necessarily incorrect.
def find_swap(i0, swaps = {}):
    is_correct = set(descendants(f"z{i0 - 1:02d}", swaps=swaps))
    for c1, c2 in it.product(
        descendants(f"z{i0:02d}", swaps=swaps),
        descendants(f"z45"      , swaps=swaps),
    ):
        if c1 in is_correct or c2 in is_correct or c1 in descendants(c2, swaps=swaps):
            continue

        s = swaps | { c1: c2, c2: c1 }
        i = find_smallest_error(s)
        if i > i0:
            find_swap(i, s)

find_swap(find_smallest_error())
