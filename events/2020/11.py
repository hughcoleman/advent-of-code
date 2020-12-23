#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/11: Seating System")
problem.preprocessor = ppr.grid

from collections import defaultdict

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def neighbours(position):
    x, y = position
    for dx, dy in DELTAS:
        yield (x + dx, y + dy)


def visible(seats, position):
    x, y = position
    for dx, dy in DELTAS:
        nx, ny = x + dx, y + dy
        while (nx, ny) not in seats:
            nx, ny = nx + dx, ny + dy

            if nx < 0 or ny < 0 or nx > 100 or ny > 100:
                break

        if (nx, ny) in seats:
            yield (nx, ny)


@problem.solver(part=1)
def p1(seating):
    seats = set()
    occupied = set()

    for y in range(len(seating)):
        for x in range(len(seating[y])):
            if seating[y][x] in ["L", "#"]:
                seats.add((x, y))
            elif seating[y][x] in ["#"]:
                occupied.add((x, y))

    while True:
        activities = defaultdict(int, {seat: 0 for seat in seats})
        for seat in occupied:
            for neighbour in neighbours(seat):
                if neighbour in seats:
                    activities[neighbour] += 1

        _occupied = set()
        for seat, activity in activities.items():
            if (seat not in occupied) and (activity <= 0):
                _occupied.add(seat)
            elif (seat in occupied) and (activity < 4):
                _occupied.add(seat)

        if occupied == _occupied:
            break

        occupied = _occupied

    return len(occupied)


@problem.solver(part=2)
def p2(seating):
    seats = set()
    occupied = set()

    for y in range(len(seating)):
        for x in range(len(seating[y])):
            if seating[y][x] in ["L", "#"]:
                seats.add((x, y))
            elif seating[y][x] in ["#"]:
                occupied.add((x, y))

    while True:
        activities = defaultdict(int, {seat: 0 for seat in seats})
        for seat in occupied:
            for neighbour in visible(seats, seat):
                if neighbour in seats:
                    activities[neighbour] += 1

        _occupied = set()
        for seat, activity in activities.items():
            if (seat not in occupied) and (activity <= 0):
                _occupied.add(seat)
            elif (seat in occupied) and (activity < 5):
                _occupied.add(seat)

        if occupied == _occupied:
            break

        occupied = _occupied

    return len(occupied)


if __name__ == "__main__":
    problem.solve()
