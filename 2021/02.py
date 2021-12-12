#!/usr/bin/env python3
""" 2021/02: Dive! """

import sys

commands = [
    (command, int(argument))
        for command, argument in map(str.split, sys.stdin.read().strip().split("\n"))
]

position, depth = 0, 0
for command, argument in commands:
    if command == "forward":
        position += argument
    elif command == "up":
        depth -= argument
    elif command == "down":
        depth += argument

print("Part 1:", position * depth)

position, depth, aim = 0, 0, 0
for command, argument in commands:
    if command == "forward":
        position += argument
        depth += aim * argument
    elif command == "up":
        aim -= argument
    elif command == "down":
        aim += argument

print("Part 2:", position * depth)
