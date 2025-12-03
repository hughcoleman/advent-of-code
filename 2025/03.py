#!/usr/bin/env python3
""" 2025/03: Lobby """

import sys

banks = [
    list(map(int, bank.strip()))
        for bank in iter(sys.stdin.readline, "")
]

def best(joltages, l=2):
    if l == 1:
        return max(joltages)

    d = max(joltages[:-l + 1])
    i = joltages.index(d)
    return d * 10**(l - 1) + best(joltages[i + 1:], l - 1)

print("Part 1:", sum(map(best, banks)))
print("Part 2:", sum(best(bank, 12) for bank in banks))
