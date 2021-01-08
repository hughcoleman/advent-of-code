#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/07: Recursive Circus")
problem.preprocessor = ppr.lsv


import networkx as nx
import collections as cl
import statistics as stat
import re


parser = re.compile(r"([a-z]+) \(([0-9]+)\) ?-?>? ?([a-z]+(, [a-z]+)*)?")


@problem.solver()
def solve(disks):
    tower = nx.DiGraph()

    for disk in disks:
        disk, weight, children, _ = re.fullmatch(parser, disk).groups()

        tower.add_node(disk, weight=int(weight))
        if children:
            for child in children.split(", "):
                tower.add_edge(disk, child)

    # sort the graph using topological sort to obtain the root node
    ordered = list(nx.topological_sort(tower))

    # starting at the leaves, determine the weight of each disk (itself, plus
    # whatever children it's holding)
    weights = {}
    for disk in reversed(ordered):
        weight = tower.nodes[disk]["weight"]

        # determine the mode of the weights of the subtowers on this disk
        subtowers = [weights[subtower] for subtower in tower[disk]]
        for subtower in tower[disk]:
            # if the weight of this subtower is not equal to the mode of the
            # weights of the other sub-towers, then this is the program with
            # the wrong weight
            if weights[subtower] != stat.mode(subtowers):
                return (
                    ordered[0],
                    tower.nodes[subtower]["weight"]
                    - (weights[subtower] - stat.mode(subtowers)),
                )

            weight = weight + weights[subtower]

        weights[disk] = weight


if __name__ == "__main__":
    problem.solve()
