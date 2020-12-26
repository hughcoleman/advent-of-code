#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/07: Some Assembly Required")
problem.preprocessor = ppr.lsv


OPERATIONS = {
    "AND": lambda o1, o2: o1 & o2,
    "OR": lambda o1, o2: o1 | o2,
    "NOT": lambda o: 0b1111111111111111 - o,
    "LSHIFT": lambda o, shift: o << shift,
    "RSHIFT": lambda o, shift: o >> shift,
}


def simulate(wires, override={}):
    # Given the wirings in the circuit, and overrides on the wires, compute the
    # signal ultimately passed to node "a."
    signals = {}
    for wire, signal in override.items():
        signals[wire] = signal

    while "a" not in signals.keys():
        for wire in wires:
            inputs, output = wire.split(" -> ")
            if output in signals.keys():
                continue

            terms = inputs.split(" ")
            if len(terms) == 1:  # ...then this is a "set"
                if terms[0].isdigit():
                    signals[output] = int(terms[0])
                elif terms[0] in signals.keys():
                    signals[output] = signals[terms[0]]

            elif len(terms) == 2:  # ...then this is a bitwise "NOT"
                assert terms[0] == "NOT"

                if terms[1] in signals.keys():
                    signals[output] = OPERATIONS["NOT"](signals[terms[1]])

            elif len(terms) == 3:  # ...then this is a bitwise operation
                assert terms[1] in OPERATIONS.keys()

                o1, operation, o2 = terms

                if o1.isdigit():
                    o1 = int(o1)
                elif o1 in signals.keys():
                    o1 = signals[o1]
                else:
                    # all terms in rule not fully resolved
                    continue

                if o2.isdigit():
                    o2 = int(o2)
                elif o2 in signals.keys():
                    o2 = signals[o2]
                else:
                    # all terms in rule not fully resolved
                    continue

                signals[output] = OPERATIONS[operation](o1, o2)

            else:
                raise RuntimeError("unreachable state?")

    return signals["a"]


@problem.solver()
def solve(wires):
    p1 = simulate(wires)
    p2 = simulate(wires, {"b": p1})

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
