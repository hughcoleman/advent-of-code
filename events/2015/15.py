#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/15: Science for Hungry People")
problem.preprocessor = ppr.lsv


import collections as cl
import re
import itertools

Ingredient = cl.namedtuple(
    "Ingredient", ["capacity", "durability", "flavor", "texture", "calories"]
)


parser = re.compile(r"(.*):.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)")


def partition(n, k):
    if k <= 1:
        yield [n]
    else:
        for head in range(0, n + 1):
            for tail in partition(n - head, k - 1):
                yield [head] + tail


@problem.solver()
def solve(ingredients):
    X = {}
    for ingredient in ingredients:
        name, *properties = re.fullmatch(parser, ingredient).groups()
        X[name.lower()] = Ingredient(*[int(i) for i in properties])
    ingredients = X

    p1, p2 = 0, 0
    for amounts in partition(100, len(ingredients.items())):
        scores = cl.defaultdict(int)
        for p in ["capacity", "durability", "flavor", "texture", "calories"]:
            for amount, (_, ingredient) in zip(amounts, ingredients.items()):
                scores[p] += amount * getattr(ingredient, p)

        score = (
            max(scores["capacity"], 0)
            * max(scores["durability"], 0)
            * max(scores["flavor"], 0)
            * max(scores["texture"], 0)
        )

        p1 = max(p1, score)
        if scores["calories"] == 500:
            p2 = max(p2, score)

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
