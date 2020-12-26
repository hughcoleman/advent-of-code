#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/14: Reindeer Olympics")
problem.preprocessor = ppr.lsv

import collections as cl
import re


class Reindeer:
    """ A single Reindeer. """

    def __init__(self, speed, active, rest, position, points):
        self.speed = speed
        self.active = active
        self.rest = rest
        self.position = position
        self.points = points


parser = re.compile(r"(\w+) .*? (\d+) .*? (\d+) .*? (\d+) .*?.")


@problem.solver()
def solve(speeds):

    reindeers = {}
    for reindeer in speeds:
        name, speed, duration, rest = re.match(parser, reindeer).groups()

        reindeers[name] = Reindeer(int(speed), int(duration), int(rest), 0, 0)

    for ts in range(2503):
        for name, R in reindeers.items():
            if ts % (R.active + R.rest) < R.active:
                R.position = R.position + R.speed

        leader = max(R.position for R in reindeers.values())
        for n, R in reindeers.items():
            if R.position == leader:
                R.points += 1

    distance = 0
    points = 0
    for n, R in reindeers.items():
        distance = max(distance, R.position)
        points = max(points, R.points)

    return (distance, points)


if __name__ == "__main__":
    problem.solve()
