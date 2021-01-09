#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/14: Disk Defragmentation")
problem.preprocessor = lambda key: key.strip()


import functools
import networkx as nx


def kh(lengths, rounds=1):
    knot = list(range(0, 256))
    current, skip = 0, 0

    for _ in range(rounds):
        for length in lengths:
            for i in range(0, length // 2):
                a = (current + i) % 256
                b = (current + length - i - 1) % 256

                knot[a], knot[b] = knot[b], knot[a]

            current = current + length + skip
            skip = skip + 1

    return knot


def kh2(content):
    digest = kh([ord(c) for c in content] + [17, 31, 73, 47, 23], rounds=64)

    return [
        functools.reduce(lambda l, r: l ^ r, digest[i : i + 16])
        for i in range(0, 256, 16)
    ]


@problem.solver()
def solve(key):
    # set up disks
    disks = []
    for _ in range(128):
        disks.append([0] * 128)

    # compute knot hashes
    for row in range(128):
        digest = kh2("{}-{}".format(key, row))

        for column in range(128):
            disks[row][column] = (
                digest[column // 8] >> (7 - (column % 8))
            ) & 1

    p1 = sum(sum(row) for row in disks)

    G = nx.Graph()
    for r in range(128):
        for c in range(128):
            if disks[r][c] <= 0:
                continue

            # only consider cells down and right; cells above/left are handled
            # by those cells
            for dr, dc in [(0, 1), (1, 0)]:
                if r + dr < 128 and disks[r + dr][c]:
                    G.add_edge((r, c), (r + dr, c))

                if c + dc < 128 and disks[r][c + dc]:
                    G.add_edge((r, c), (r, c + dc))

    p2 = sum(1 for region in nx.connected_components(G))

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
