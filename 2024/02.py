#!/usr/bin/env python3
""" 2024/02: Red-Nosed Reports """

import sys

reports = [
    list(map(int, report.split()))
        for report in sys.stdin.read().strip().split("\n")
]

def is_safe(report):
    is_incr = all(x1 < x2 for x1, x2 in zip(report, report[1:]))
    is_decr = all(x1 > x2 for x1, x2 in zip(report, report[1:]))
    return (
        (is_incr or is_decr)
        and all(1 <= abs(x1 - x2) <= 3 for x1, x2 in zip(report, report[1:]))
    )

print("Part 1:", sum(is_safe(report) for report in reports))
print("Part 2:",
    sum(
        is_safe(report) or any(is_safe(report[:i] + report[i+1:]) for i in range(0, len(report)))
            for report in reports
    )
)
