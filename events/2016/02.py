#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/02: Bathroom Security")
problem.preprocessor = ppr.lsv


KEYPAD_SIMPLE = {
    -1 + 1j: 1,
    0 + 1j: 2,
    1 + 1j: 3,
    -1 + 0j: 4,
    0 + 0j: 5,
    1 + 0j: 6,
    -1 - 1j: 7,
    0 - 1j: 8,
    1 - 1j: 9,
}

KEYPAD_COMPLEX = {
    0 + 2j: 1,
    -1 + 1j: 2,
    0 + 1j: 3,
    1 + 1j: 4,
    -2 + 0j: 5,
    -1 + 0j: 6,
    0 + 0j: 7,
    1 + 0j: 8,
    2 + 0j: 9,
    -1 - 1j: 0xA,
    0 - 1j: 0xB,
    1 - 1j: 0xC,
    0 - 2j: 0xD,
}

DIRECTIONS = {"U": 0 + 1j, "D": 0 - 1j, "L": -1, "R": 1}


@problem.solver(part=1)
def naive(instructions):
    code = 0

    finger = 0 + 0j
    for instruction in instructions:
        for move in instruction:
            # as long as the move doesn't cause our finger to leave the keypad,
            # then take it
            if finger + DIRECTIONS[move] in KEYPAD_SIMPLE.keys():
                finger = finger + DIRECTIONS[move]

        # "0" is not a key on the keypad, so we don't need to worry about
        # keeping track of leading zeroes
        code = 10 * code + KEYPAD_SIMPLE[finger]

    return code


@problem.solver(part=2)
def actual(instructions):
    code = 0

    finger = 0 + 0j
    for instruction in instructions:
        for move in instruction:
            # as long as the move doesn't cause our finger to leave the keypad,
            # then take it
            if finger + DIRECTIONS[move] in KEYPAD_COMPLEX.keys():
                finger = finger + DIRECTIONS[move]

        # "0" is not a key on the keypad, so we don't need to worry about
        # keeping track of leading zeroes
        code = 16 * code + KEYPAD_COMPLEX[finger]

    return hex(code)[2:]


if __name__ == "__main__":
    problem.solve()
