#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/09: Explosives in Cyberspace")
problem.preprocessor = lambda f: cl.deque(f.strip())


import collections as cl


def rle_decompress(stream, version=1):
    size = 0
    while stream:
        # if we encounter a marker, consume it and recurse as necessary
        if stream.popleft() == "(":
            width = 0
            while stream[0] != "x":
                width = 10 * width + int(stream.popleft())
            stream.popleft()  # pop "x"

            repetitions = 0
            while stream[0] != ")":
                repetitions = 10 * repetitions + int(stream.popleft())
            stream.popleft()  # pop ")"

            # based on the version, the rules for recursion/repetition are
            # different
            if version <= 1:
                for _ in range(width):
                    stream.popleft()
                size = size + width * repetitions
            elif version <= 2:
                r = cl.deque()
                for _ in range(width):
                    r.append(stream.popleft())
                size = size + repetitions * rle_decompress(r, version=2)
        else:
            size = size + 1

    return size


@problem.solver(part=1)
def p1(f):
    return rle_decompress(f)


@problem.solver(part=2)
def p2(f):
    # can't put this in the function above, because the first call to
    # rle_decompress will pollute the deque.
    return rle_decompress(f, version=2)


if __name__ == "__main__":
    problem.solve()
