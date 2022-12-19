#!/usr/bin/env python3
""" 2022/06: Tuning Trouble """

import sys

signal = sys.stdin.read().strip()

scan = lambda N: \
    next(i for i in range(N, len(signal)) if len(set(signal[i - N:i])) == N)
print("Part 1:", scan(4))
print("Part 2:", scan(14))
