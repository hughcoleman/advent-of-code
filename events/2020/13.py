#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/13: Shuttle Search")
problem.preprocessor = lambda schedule: (
    # parse the input to (arrival time, [(int)bus time, None if irrelevant])
    int(schedule.strip().split("\n")[0]),
    [
        int(bus) if bus != "x" else None
        for bus in schedule.strip().split("\n")[1].split(",")
    ],
)

import functools


@problem.solver(part=1)
def p1(schedule):
    # our arrival time, and the bus frequencies
    arrival, buses = schedule

    # the next departure times of each bus line
    departures = [
        (bus, arrival + bus - (arrival % bus)) for bus in buses if bus
    ]

    earliest = min(departures, key=lambda s: s[1])
    return earliest[0] * (earliest[1] - arrival)


@problem.solver(part=2)
def p2(schedule):
    _, buses = schedule

    # We can use the Chinese Remainder Theorem to efficiently compute the
    # offset at which the bus departure times "line up."

    n = 0
    product = functools.reduce(
        lambda p, q: p * q, [bus for bus in buses if bus]
    )
    for offset, bus in enumerate(buses):
        if not bus:
            continue

        p = product // bus

        # This solution assumes that all the bus departure frequencies are
        # prime (after reviewing the subreddit, this appears to be an
        # intentional decision by the author.) This allows us to apply Fermat's
        # Little Theorem to efficiently compute the modular inverse of
        # p (mod bus).
        #
        # That said, it is entirely possible for the problem to contain
        # composite bus departure frequencies, in which case, the line below
        # needs to be modified - replace `pow(p, bus - 2, bus)` with
        # `modinv(p, bus)`.
        n += (bus - offset) * pow(p, bus - 2, bus) * p

    return n % product


if __name__ == "__main__":
    problem.solve()
