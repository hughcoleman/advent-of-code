#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/02: Password Philosophy")
problem.preprocessor = lambda entries: [
    re.findall(r"[a-z0-9]+", entry)
    for entry in entries.split("\n")
    if entry.strip()
]

import re


@problem.solver(part=1)
def part1(entries):
    valid = 0
    for entry in entries:
        lo, hi, letter, password = entry

        if int(lo) <= password.count(letter) <= int(hi):
            valid = valid + 1

    return valid


@problem.solver(part=2)
def part2(entries):
    valid = 0
    for entry in entries:
        i1, i2, letter, password = entry

        if (password[int(i1) - 1] == letter) ^ (
            password[int(i2) - 1] == letter
        ):
            valid = valid + 1

    return valid


if __name__ == "__main__":
    problem.solve()
