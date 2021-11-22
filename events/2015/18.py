from lib import *
problem = aoc.Problem("2015/18: Like a GIF For Your Yard")
problem.preprocessor = ppr.grid

import collections as cl

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

@problem.solver(part=1)
def p1(yard):
    on = set()
    for y, row in enumerate(yard):
        for x, char in enumerate(row):
            if char == "#":
                on.add((x, y))

    for _ in range(100):
        neighbours = cl.defaultdict(int, {c: 0 for c in on})
        for cell in on:
            x, y = cell
            for dx, dy in DELTAS:
                neighbours[x + dx, y + dy] += 1

        nx = set()
        for cell, n in neighbours.items():
            x, y = cell
            if (x < 0) or (y < 0) or (x >= 100) or (y >= 100):
                continue

            if (cell in on) and (2 <= n <= 3):
                nx.add(cell)
            elif (cell not in on) and (n == 3):
                nx.add(cell)

        on = nx

    return len(on)

@problem.solver(part=2)
def p2(yard):
    on = set()
    for y, row in enumerate(yard):
        for x, char in enumerate(row):
            if char == "#":
                on.add((x, y))

    for _ in range(100):
        on.add((0, 0))
        on.add((0, 99))
        on.add((99, 0))
        on.add((99, 99))

        neighbours = cl.defaultdict(int, {c: 0 for c in on})
        for cell in on:
            x, y = cell
            for dx, dy in DELTAS:
                neighbours[x + dx, y + dy] += 1

        nx = set()
        for cell, n in neighbours.items():
            x, y = cell
            if (x < 0) or (y < 0) or (x >= 100) or (y >= 100):
                continue

            if (cell in on) and (2 <= n <= 3):
                nx.add(cell)
            elif (cell not in on) and (n == 3):
                nx.add(cell)

        on = nx

    on.add((0, 0))
    on.add((0, 99))
    on.add((99, 0))
    on.add((99, 99))
    return len(on)


if __name__ == "__main__":
    problem.solve()
