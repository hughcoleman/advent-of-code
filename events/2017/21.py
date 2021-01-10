#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/21: Fractal Art")
problem.preprocessor = lambda rules: (
    # rules for 2-by-2 tiles
    {
        _hash(
            [
                [".#".index(c) for c in row]
                for row in rule.split(" => ")[0].split("/")
            ]
        ): [
            [".#".index(c) for c in row]
            for row in rule.split(" => ")[1].split("/")
        ]
        for rule in rules.strip().split("\n")[:6]
    },

    # rules for 3-by-3 tiles
    {
        _hash(
            [
                [".#".index(c) for c in row]
                for row in rule.split(" => ")[0].split("/")
            ]
        ): [
            [".#".index(c) for c in row]
            for row in rule.split(" => ")[1].split("/")
        ]
        for rule in rules.strip().split("\n")[6:]
    },
)


def _hash(tile):
    """Generate a unique, but consistent, identifier for a given tile,
    disregarding rotations and flips."""

    # transpose a matrix by flipping over the diagonal
    def transpose(matrix):
        return [*zip(*matrix)]

    # flip a matrix over the horizontal/x-axis
    def flip(matrix):
        return matrix[::-1]

    # generate a hash of a binary grid, by interpreting the matrix as a binary
    # number in row-major order
    def __hash(grid):
        n = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                n = (n << 1) | cell
        return n

    n = pow(2, 17) + 1

    # consider all eight possible orientations of this tile, and pick the one
    # with the minimal hash value
    for _ in range(4):
        tile = transpose(tile)
        n = min(n, __hash(tile))

        tile = flip(tile)
        n = min(n, __hash(tile))

    return n


def simulate(rules, iterations):
    _2_rules, _3_rules = rules

    fractal = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    for iteration in range(iterations):
        # determine ruleset
        rules, size = {0: (_2_rules, 2), 1: (_3_rules, 3)}[len(fractal) % 2]

        # create enlarged image
        _fractal = []
        for i in range(len(fractal) * (size + 1) // size):
            _fractal.append([None] * (len(fractal) * (size + 1) // size))

        # enhance!
        for y in range(0, len(fractal), size):
            for x in range(0, len(fractal), size):
                tile = [fractal[y + d][x : x + size] for d in range(size)]

                _tile = rules[_hash(tile)]
                for dy in range(len(_tile)):
                    for dx in range(len(_tile)):
                        _fractal[y // size * len(_tile) + dy][
                            x // size * len(_tile) + dx
                        ] = _tile[dy][dx]

        fractal = _fractal

    return sum(sum(row) for row in fractal)


@problem.solver()
def solve(rules):
    return (simulate(rules, 5), simulate(rules, 18))


if __name__ == "__main__":
    problem.solve()
