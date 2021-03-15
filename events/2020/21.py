#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2020/21: Allergen Assessment")
problem.preprocessor = lambda foods: [
    (
        set(food.split(" (contains ")[0].split(" ")),
        set(food.split(" (contains ")[1][:-1].split(", ")),
    )
    for food in foods.strip().split("\n")
]


@problem.solver()
def solve(foods):
    ingredients, allergens = set(), set()
    for _is, _as in foods:
        ingredients.update(_is)
        allergens.update(_as)

    # potentially dangerous ingredients
    unsafe = {}
    for allergen in allergens:
        candidates = ingredients.copy()
        for _is, _as in foods:
            if allergen in _as:
                candidates = set.intersection(candidates, _is)

        unsafe[allergen] = candidates

    # count occurrences of safe ingredients in foods
    p1 = 0
    for inert in ingredients - set.union(*unsafe.values()):
        for _is, _ in foods:
            if inert in _is:
                p1 = p1 + 1

    # identify the deadly ingredients
    resolved = {}
    while len(resolved.keys()) < len(allergens):
        for allergen, candidates in unsafe.items():
            if allergen in resolved.keys():
                continue

            unsafe[allergen] = candidates - set(resolved.values())
            if len(unsafe[allergen]) <= 1:
                (resolved[allergen],) = unsafe[allergen]

    p2 = ",".join(resolved[allergen] for allergen in sorted(allergens))

    return (p1, p2)


# tests?

if __name__ == "__main__":
    problem.solve()
