#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/12: Rain Risk")
problem.preprocessor = lambda instructions: [
    # parse each instruction into (action, (int)magnitude)
    (instruction[:1], int(instruction[1:]))
    for instruction in instructions.split("\n")
    if instruction.strip()
]

COMPLEX_DIRECTIONS = {
    # cardinal directions
    "N": 0 + 1j,
    "S": 0 - 1j,
    "E": 1 + 0j,
    "W": -1 + 0j,
    
    # relative directions
    "L": 0 + 1j,
    "R": 0 - 1j,
}


@problem.solver(part=1)
def p1(instructions):
    # track ship position and direction as complex numbers
    ship, direction = 0 + 0j, 1 + 0j
    for action, magnitude in instructions:
        if action in "NSEW":
            ship += magnitude * COMPLEX_DIRECTIONS[action]
        elif action in "LR":
            direction *= COMPLEX_DIRECTIONS[action] ** (magnitude // 90)
        else:
            ship += magnitude * direction

    return int(abs(ship.real) + abs(ship.imag))


@problem.solver(part=2)
def p2(instructions):
    # track ship position and relative offset of waypoint as complex numbers
    ship, waypoint = 0 + 0j, 10 + 1j
    for action, magnitude in instructions:
        if action in "NSEW":
            waypoint += magnitude * COMPLEX_DIRECTIONS[action]
        elif action in "LR":
            waypoint *= COMPLEX_DIRECTIONS[action] ** (magnitude // 90)
        else:
            ship += magnitude * waypoint

    return int(abs(ship.real) + abs(ship.imag))


if __name__ == "__main__":
    problem.solve()
