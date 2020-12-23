#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/07: Handy Haversacks")
problem.preprocessor = ppr.lsv

from collections import defaultdict
import re


@problem.solver()
def solve(rules):
    RULES = defaultdict(lambda: [])
    for rule in rules:
        container = re.match(r"(.+?) bags contain", rule)[1]
        for n, containee in re.findall(r"([0-9]+) (.+?) bags?[,.]", rule):
            RULES[container].append((int(n), containee))

    C = set()  # can it carry a shiny gold bag?
    while True:
        grown = False
        for container, containees in RULES.items():
            if (container not in C) and any(
                containee == "shiny gold" or containee in C
                for _, containee in containees
            ):
                C.add(container)
                grown = True

        if not grown:
            break

    def contents(parent):
        children = 0
        for n, child in RULES[parent]:
            children += n + (n * contents(child))
        return children

    return (len(C), contents("shiny gold"))


if __name__ == "__main__":
    problem.solve()
