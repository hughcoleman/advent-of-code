#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/20: Particle Swarm")
problem.preprocessor = lambda particles: {
    i: Particle(
        tuple(int(x) for x in particle.split(", ")[0][3:-1].split(",")),
        tuple(int(x) for x in particle.split(", ")[1][3:-1].split(",")),
        tuple(int(x) for x in particle.split(", ")[2][3:-1].split(",")),
    )
    for i, particle in enumerate(particles.strip().split("\n"))
}


import collections as cl


class Particle:
    """ Represents a single particle in 3d-space. """

    def update(self):
        self.v = tuple(v + a for v, a in zip(self.v, self.a))
        self.p = tuple(p + v for p, v in zip(self.p, self.v))

    @property
    def distance(self):
        return sum(abs(coordinate) for coordinate in self.p)

    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a


@problem.solver(part=1)
def p1_farthest(particles):
    # it's probably enough just to step through a thousand ticks, and to find
    # the closest particle after that
    for ts in range(1000):
        for i, particle in particles.items():
            particle.update()

    return min(particles.items(), key=lambda x: x[1].distance)[0]


@problem.solver(part=2)
def p2_collisions(particles):
    # it's probably enough just to step through a thousand ticks, and to count
    # still-existing particles after that
    for ts in range(1000):
        positions = cl.defaultdict(list)
        for i, particle in particles.items():
            particle.update()
            positions[particle.p].append(i)

        for position, particles_ in positions.items():
            if len(particles_) > 1:
                for particle in particles_:
                    del particles[particle]

    return len(particles.keys())


if __name__ == "__main__":
    problem.solve()
