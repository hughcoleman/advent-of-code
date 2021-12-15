#!/usr/bin/env python3
""" 2021/14: Extended Polymerization """

import sys
import collections as cl

polymer, rules = sys.stdin.read().strip().split("\n\n")

rules = {
    tuple(rule.split()[0]): rule.split()[2]
        for rule in rules.strip().split("\n")
}

pairs = cl.Counter(
    polymer[i:i+2] for i in range(len(polymer) - 1)
)
for step in range(1, 40 + 1):
    _pairs = cl.Counter()
    for (l, r), n in pairs.items():
        m = rules[l, r]
        _pairs[l + m] += n
        _pairs[m + r] += n

    pairs = _pairs

    if step == 10 or step == 40:
        elements = cl.Counter()
        for (l, r), n in pairs.items():
            elements[l] += n
        elements[polymer[-1]] += 1

        print("Part {}:".format({10: "1", 40: "2"}[step]),
            max(elements.values()) - min(elements.values())
        )
