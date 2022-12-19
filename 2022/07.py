#!/usr/bin/env python3
""" 2022/07: No Space Left On Device """

import collections as cl
import pathlib
import sys

T = sys.stdin.read().strip().split("\n")

fs, cwd = cl.defaultdict(int), pathlib.Path("/")
for t in T:
    if t.startswith("$ cd"):
        arg = t.split()[-1]
        cwd = {
            "/": pathlib.Path("/"),
            "..": cwd.parent, 
        }.get(arg, cwd / arg)
    elif t[0].isdigit():
        _cwd = cwd / t.split()[1]
        while _cwd != pathlib.Path("/"):
            _cwd = _cwd.parent
            fs[_cwd] += int(t.split()[0])
        
print("Part 1:", sum(size for size in fs.values() if size <= 100000))
print("Part 2:", min(
    size for size in fs.values()
        if size >= fs.get(pathlib.Path("/")) - 40000000
))
