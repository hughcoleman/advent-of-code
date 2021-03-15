#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/24: Lobby Layout")
problem.preprocessor = ppr.lsv

from collections import defaultdict
import re

DIRECTIONS = {
    # this uses axial coordinates to identify points/directions on a hexagonal
    # plane, with the secondary axis parallel to the nw-se direction. 
    #
    # https://www.redblobgames.com/grids/hexagons/#coordinates-axial
    
    "e": 1 + 0j,
    "w": -1 + 0j,
    "se": 0 - 1j,
    "sw": -1 - 1j,
    "nw": 0 + 1j,
    "ne": 1 + 1j
}


@problem.solver()
def solve(flips):

    tiles = defaultdict(lambda: False)
    for flip in flips:
        position = sum(
            DIRECTIONS[step] for step in re.findall("e|se|sw|w|nw|ne", flip)
        )

        tiles[position] = not tiles[position]

    p1 = list(tiles.values()).count(True) # alternatively; len(black)

    black = {c for c, v in tiles.items() if v}
    for generation in range(100):
        # count number of black-colored tiles neighbouring each tile
        neighbours = defaultdict(int, {coordinate: 0 for coordinate in black})

        for tile in black:
            for delta in DIRECTIONS.values():
                neighbours[tile + delta] += 1

        # determine cells that should be black in the next generation
        successor = set()
        for tile, count in neighbours.items():
            if (tile in black) and (1 <= count <= 2):
                successor.add(tile)
            elif (tile not in black) and (count == 2):
                successor.add(tile)

        black = successor

    return (p1, len(black))


if __name__ == "__main__":
    problem.solve()
