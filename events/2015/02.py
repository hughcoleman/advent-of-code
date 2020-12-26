#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/02: I Was Told There Would Be No Math")
problem.preprocessor = lambda boxes: [
    (int(dimension) for dimension in box.split("x"))
    for box in boxes.strip().split("\n")
]


@problem.solver()
def solve(boxes):
    paper, ribbon = 0, 0
    for box in boxes:
        # the dimensions associated with each length don't actually matter, 
        # so sort them smallest to largest
        l, w, h = sorted(box)

        paper += (2 * l * w + 2 * w * h + 2 * h * l) + (l * w)
        ribbon += (2 * l + 2 * w) + (l * w * h)

    return (paper, ribbon)


if __name__ == "__main__":
    problem.solve()
