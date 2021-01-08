#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/04: High-Entropy Passphrases")
problem.preprocessor = ppr.lsv


import collections as cl


@problem.solver(part=1)
def naive_policy(passphrases):
    valid = 0
    for passphrase in passphrases:
        words = passphrase.split(" ")
        if any(count > 1 for word, count in cl.Counter(words).most_common()): 
            continue
        valid = valid + 1

    return valid


@problem.solver(part=2)
def strict_policy(passphrases):
    valid = 0
    for passphrase in passphrases:
        # a cheap "hack" for anagram comparison is just to sort all letters in
        # the words alphabetically before counting.
        words = ["".join(sorted(list(word))) for word in passphrase.split(" ")]
        if any(count > 1 for word, count in cl.Counter(words).most_common()):
            continue
        valid = valid + 1

    return valid


if __name__ == "__main__":
    problem.solve()
