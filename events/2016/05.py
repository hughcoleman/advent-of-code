#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/05: How About a Nice Game of Chess?")
problem.preprocessor = ppr.identity


import hashlib


def lockpicker(identifier):
    i = 0
    while True:
        digest = hashlib.md5((identifier + str(i)).encode()).hexdigest()
        if digest.startswith("0" * 5):
            yield (digest[5], digest[6])
        i = i + 1


@problem.solver()
def solve(identifier):
    lockpick = lockpicker(identifier.strip())
    
    naive  = ""
    secure = [None] * 8
    while True:
        p, q = next(lockpick)

        # the naive password is simply the sixth character of the digest, p
        if len(naive) < 8:
            naive = naive + p

        # the secure password uses the sixth character, p, as an index for the
        # seventh character, q
        if int(p, 16) <= 7 and not secure[int(p, 16)]:
            secure[int(p, 16)] = q
        
        # if the secure code has been determined then so must the naive
        if all(c for c in secure):
            break

    return (naive, "".join(secure))


if __name__ == "__main__":
    problem.solve()
