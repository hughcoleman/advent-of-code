from lib import *
problem = aoc.Problem("2015/13: Knights of the Dinner Table")
problem.preprocessor = ppr.lsv

import collections as cl
import itertools as it
import re

parser = re.compile(r"(\w+?) .*? (gain|lose) (\d+) .*? (\w+?)\.")

@problem.solver()
def solve(relations):
    rules = cl.defaultdict(dict)
    for relation in relations:
        person, direction, score, neighbour = re.match(
            parser, relation
        ).groups()

        rules[person][neighbour] = (
            int(score) * {"gain": 1, "lose": -1}[direction]
        )

    def happiness(ordering):
        return sum(
            rules[p][q] + rules[q][p]
            for p, q in zip(ordering, ordering[1:] + ordering[:1])
        )

    p1 = max(happiness(ordering) for ordering in it.permutations(rules.keys()))

    # Add self!
    for person in list(rules.keys()):
        rules["self"][person] = 0
        rules[person]["self"] = 0

    p2 = max(happiness(ordering) for ordering in it.permutations(rules.keys()))

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
