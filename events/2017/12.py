#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/12: Digital Plumber")
problem.preprocessor = ppr.lsv


import networkx as nx


@problem.solver()
def solve(pipes):
    G = nx.Graph()

    for pipe in pipes:
        source, _, destinations = pipe.split(" ", 2)

        for destination in destinations.split(", "):
            G.add_edge(int(source), int(destination))

    # find number of groups, and number of computers in group containing
    # computer #0.
    p1 = 0
    p2 = 0
    for group in nx.connected_components(G):
        if 0 in group:
            p1 = len(group)
        p2 = p2 + 1

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
