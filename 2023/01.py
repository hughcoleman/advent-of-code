#!/usr/bin/env python3
""" 2023/01: Trebuchet?! """

import sys

document = sys.stdin.read().strip()

def calibrate(d):
    return sum(
        int((k := [c for c in d0 if c.isdigit()])[0] + k[-1])
            for d0 in d.split("\n")
    )

print("Part 1:", calibrate(document))
print("Part 2:",
    calibrate(
        document.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
    )
)
