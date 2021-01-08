#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/04: Security Through Obscurity")
problem.preprocessor = ppr.lsv


import re
import collections as cl

parser = re.compile(r"([a-z\-]+)\-([\d]+)\[([a-z]{5})\]")


def caesar(ciphertext, shift):
    plaintext = []
    for char in ciphertext:
        if char in [" ", "-"]:
            plaintext.append(" ")
        else:
            plaintext.append(chr((ord(char) + shift - 97) % 26 + 97))

    return "".join(plaintext)


@problem.solver()
def solve(rooms):
    total = 0
    storage = None

    for room in rooms:
        name, sector, checksum = re.fullmatch(parser, room).groups()

        computed = "".join(
            k
            for k, v in sorted(
                cl.Counter(name.replace("-", "")).most_common(),
                key=lambda e: (-e[1], e[0]),
            )[:5]
        )

        if computed == checksum:
            total = total + int(sector)

            # is this the north pole object storage?
            if "northpole object storage" == caesar(name, int(sector)):
                storage = sector

    return (total, storage)


if __name__ == "__main__":
    problem.solve()
