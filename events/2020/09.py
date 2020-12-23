#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/09: Encoding Error")
problem.preprocessor = ppr.lsi


@problem.solver()
def solve(numbers):
    for idx in range(25, len(numbers)):
        previous = numbers[idx - 25 : idx]

        valid = False
        for j1 in range(25):
            for j2 in range(j1 + 1, 25):
                if previous[j1] + previous[j2] == numbers[idx]:
                    valid = True
        if not valid:
            p1 = numbers[idx]

    left, right = 0, 2
    total = sum(numbers[left:right])
    while right < len(numbers) - 1:
        if total < p1:
            total = total + numbers[right]
            right = right + 1
        elif total > p1:
            total = total - numbers[left]
            left = left + 1
        else:
            window = numbers[left:right]
            p2 = min(window) + max(window)
            break

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
