#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2020/20: Jurassic Jigsaw")
problem.preprocessor = ppr.llsv

from collections import defaultdict


def edges(grid):
    for edge in [
        [str(pixel) for pixel in grid[0]],  # top edge
        [str(pixel) for pixel in grid[-1]],  # bottom edge
        [str(row[0]) for row in grid],  # left edge
        [str(row[-1]) for row in grid],  # right edge
    ]:
        yield min(int("".join(edge), 2), int("".join(edge[::-1]), 2))


def flip_x(grid):  # flip over x-axis
    return grid[::-1]


def flip_y(grid):  # flip over y-axis
    return [row[::-1] for row in grid]


def rotate(grid):
    return [list(row) for row in zip(*grid[::-1])]


@problem.solver()
def solve(images):
    TILES = {}
    for image in images:
        header, content = image.split("\n", 1)

        # store the tiles in a dictionary by identification number, with the
        # pixels converted to a bit array
        TILES[int(header[5:-1])] = [
            [".#".index(pixel) for pixel in list(row)]
            for row in content.split("\n")
        ]

    # for each tile, get its "knobs" (borders), and associate it with the other
    # tiles with a matching knob pattern
    knobs = defaultdict(set)
    for tile, pixels in TILES.items():
        for edge in edges(pixels):
            knobs[edge].add(tile)

    # create a graph, where edges indicate two tiles that can be connected
    # also track the number of "lonely" edges on each tile
    G = {tile: set() for tile in TILES.keys()}
    lonelies = defaultdict(int)

    for edge, tiles in knobs.items():
        if len(tiles) <= 1:
            (tile,) = tiles
            lonelies[tile] += 1
        else:
            for i, a in enumerate(tiles):
                for j, b in enumerate(tiles):
                    if i == j:
                        continue  # tiles aren't their own neighbours

                    G[a].add((b, edge))

    # compute the product of the IDs of the four corner tiles, which are going
    # to be the tiles with two lone edges. also pick one of the corners to be
    # the initial "anchor" in the top-left.
    p1, anchor = 1, 0
    for tile, lones in lonelies.items():
        p1 *= ((lones - 1) * tile) - (lones - 2)
        anchor = max((lones - 1) * tile, anchor)

    # now, we can begin setting all the tiles in the ocean
    ocean = []
    for _ in range(12):
        ocean.append([None] * 12)

    # first, set the top-left tile, by rotating it until its bottom- and right-
    # edges agree with its known neighbours
    ocean[0][0] = anchor
    while True:
        _, bottom, _, right = edges(TILES[anchor])
        if set([bottom, right]) == set(n[1] for n in G[anchor]):
            break

        TILES[anchor] = rotate(TILES[anchor])

    # now, set the rest of the tiles, in a breadth-first style
    for d in range(22):
        for x in range(d + 1):
            x, y = x, d - x

            if (x < 0) or (y < 0) or (x >= 12) or (y >= 12):
                continue

            # determine the tile that we're searching from, and get its bottom
            # and right-hand edges.
            r = ocean[y][x]
            R = TILES[r]
            _, bottom, _, right = edges(R)

            # now, set tile one cell down
            if (y + 1 <= 11) and (ocean[y + 1][x] == None):
                # first, figure out what tile goes there (shares a common edge
                # with the root)
                for candidate, edge in G[r]:
                    # if that common edge is also the bottom of the root, then
                    # it is the tile that goes below
                    if edge == bottom:
                        break
                else:
                    assert RuntimeError("could not place tile")

                ocean[y + 1][x] = candidate
                while True:
                    top, _, _, _ = edges(TILES[candidate])
                    if top == bottom:
                        break

                    TILES[candidate] = rotate(TILES[candidate])

                # now, check if they match exactly, and flip over the y-axis
                # if they don't
                if R[-1] != TILES[candidate][0]:
                    TILES[candidate] = flip_y(TILES[candidate])

            # and also set tile one cell right
            if (x + 1 <= 11) and (ocean[y][x + 1] == None):
                # first, figure out what tile goes there (shares a common edge
                # with the root)
                for candidate, edge in G[r]:
                    # if that common edge is also the right side of the root,
                    # then it is the tile that goes to the right
                    if edge == right:
                        break
                else:
                    assert RuntimeError("could not place tile")

                ocean[y][x + 1] = candidate
                while True:
                    _, _, left, _ = edges(TILES[candidate])
                    if left == right:
                        break

                    TILES[candidate] = rotate(TILES[candidate])

                # now, check if they match exactly, and flip over the x-axis
                # if they don't
                if [row[-1] for row in R] != [
                    row[0] for row in TILES[candidate]
                ]:
                    TILES[candidate] = flip_x(TILES[candidate])

    # assemble the complete image (and pretty-print in the process!)
    image = []
    print("")
    print("Here is the assembled image!", end="\n\n")
    for y in range(120):
        row = []
        print("\t", end="")
        for x in range(120):
            c = ".#"[TILES[ocean[y // 10][x // 10]][y % 10][x % 10]]

            # remember to strip the borders!
            if x % 10 not in [0, 9]:
                row.append(c)
            print(c, end="")

            if (x != 119) and (x % 10 == 9):
                print("|", end="")

        # remember to strip the borders!
        if y % 10 not in [0, 9]:
            image.append(row)
        print("")

        if (y != 119) and (y % 10 == 9):
            print("\t" + ("----------*" * 12)[:-1])

    # Find Nessie(s)!
    nessie = [
        list(r)
        for r in [
            "                  . ",
            "\    __    __    /O>",
            " \  /  \  /  \  /   ",
        ]
    ]

    for flipped in [False, True]:
        for rotation in range(4):
            monsters = set()
            for y in range(8 * 12 - len(nessie) - 1):
                for x in range(8 * 12 - len(nessie[0]) - 1):
                    hit = True
                    for dy in range(len(nessie)):
                        for dx in range(len(nessie[0])):
                            if (
                                nessie[dy][dx] != " "
                                and image[y + dy][x + dx] != "#"
                            ):
                                hit = False

                    if hit:
                        monsters.add((x, y))

            # if there was more than one monster, then we've identified the
            # correct rotation of the image
            if len(monsters) > 0:
                # debug
                print("")
                print(
                    "{} Nessies were found after {} rotation{}{}!".format(
                        len(monsters),
                        rotation,
                        "s" if rotation != 1 else "",  # the English language
                        # is annoying.
                        " and a vertical flip" if flipped else "",
                    ),
                    end="\n\n",
                )

                # in theory, we could just do (image.count("#") - 15*monsters)
                # to get the number of non-monster octothorpes, because the
                # monsters will never overlap. but let's do this properly!
                for x, y in monsters:
                    for dy in range(len(nessie)):
                        for dx in range(len(nessie[0])):
                            if nessie[dy][dx] != " ":
                                image[y + dy][x + dx] = "\u001b[32mO\u001b[0m"

                # pretty print the completed image, with spotlights on Nessy!
                print("\n".join("\t" + "".join(row) for row in image) + "\n")

                roughness = 0
                for y in range(8 * 12):
                    for x in range(8 * 12):
                        if image[y][x] == "#":
                            roughness = roughness + 1

                return (p1, roughness)

            image = rotate(image)
        image = flip_x(image)

    raise RuntimeError("unreachable state (puzzle not solvable?)")


# tests?

if __name__ == "__main__":
    problem.solve()
