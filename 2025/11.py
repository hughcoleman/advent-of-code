#!/usr/bin/env python3
""" 2025/11: Reactor """

import functools as ft
import sys

G = {
    ln[0:3]: ln[5:].split()
        for ln in iter(sys.stdin.readline, "")
}

@ft.cache
def paths(src, dest):
    if src == dest:
        return 1
    return sum(paths(src_, dest) for src_ in G.get(src, []))

print("Part 1:", paths("you", "out"))
print("Part 2:",
    # paths("dac", "fft") and paths("fft", "dac") can't both be non-zero; else
    # the graph fails to be acyclic.
    paths("svr", "dac") * paths("dac", "fft") * paths("fft", "out")
    + paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out")
)
