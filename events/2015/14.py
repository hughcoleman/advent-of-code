from lib import *
problem = aoc.Problem("2015/14: Reindeer Olympics")
problem.preprocessor = ppr.lsv

import dataclasses as dc
import re

@dc.dataclass
class Reindeer:
    speed: int
    active: int
    rest: int
    position: int
    points: int

@problem.solver()
def solve(speeds):

    reindeers = {}
    for reindeer in speeds:
        name, speed, duration, rest = re.match(
            r"(\w+) .*? (\d+) .*? (\d+) .*? (\d+) .*?.", reindeer
        ).groups()

        reindeers[name] = Reindeer(int(speed), int(duration), int(rest), 0, 0)

    for ts in range(2503):
        for name, R in reindeers.items():
            if ts % (R.active + R.rest) < R.active:
                R.position = R.position + R.speed

        leader = max(R.position for R in reindeers.values())
        for _, R in reindeers.items():
            if R.position == leader:
                R.points += 1

    distance = 0
    points = 0
    for _, R in reindeers.items():
        distance = max(distance, R.position)
        points = max(points, R.points)

    return (distance, points)


if __name__ == "__main__":
    problem.solve()
