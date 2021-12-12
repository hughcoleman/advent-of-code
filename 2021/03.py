#!/usr/bin/env python3
""" 2021/03: Binary Diagnostic """

import sys

report = sys.stdin.read().strip().split("\n")

gamma, epsilon = (
    "".join(max(x, key=x.count) for x in zip(*report)),
    "".join(min(x, key=x.count) for x in zip(*report))
)

print("Part 1:", int(gamma, 2) * int(epsilon, 2))

def filter(report, fn):
    i = 0
    while len(report) > 1:
        bit = fn("".join(n[i] for n in report))

        # Remove values which don't meet the filtering criteria.
        report = [
            n for n in report if n[i] == bit
        ]

        i = i + 1

    return report[0]

o2  = filter(report, lambda x: "0" if x.count("0") >  x.count("1") else "1")
co2 = filter(report, lambda x: "0" if x.count("0") <= x.count("1") else "1")

print("Part 2:", int(o2, 2) * int(co2, 2))
