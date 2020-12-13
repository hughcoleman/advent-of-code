#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2015/01: ???")
problem.preprocessor = ppr.lsv

# == NETWORKX ==
# import networkx as nx
# G = nx.Graph() # nx.DiGraph()

# G.add_edge("A", "B", weight=1)
# G.add_edge("B", "D", weight=4)
# G.add_edge("A", "C", weight=2)
# G.add_edge("C", "E", weight=1)
# G.add_edge("B", "E", weight=5)
# G.add_edge("H", "Z")

# print(nx.shortest_path(G, "A", "E", weight="weight"))
# print(list(nx.connected_components(G)))

# == Z3-SOLVER ==
# from z3 import *
# s = Solver()
#
# a, b = Int('a'), Int('b')
# s.add(a + b == 18)
# s.add(a - b == -4)
#
# if s.check() == sat:
#     model = s.model()
# else:
#     print("problem is unsolvable")

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0
    for v in inp:
        print(v)

    return (p1, p2)

# tests?

if __name__ == "__main__":
    problem.solve()
