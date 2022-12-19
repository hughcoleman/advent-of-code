#!/usr/bin/env python3
""" 2022/08: Treetop Tree House """

import itertools as it
import math
import sys

trees = [
    list(map(int, g))
        for g in sys.stdin.read().strip().split("\n")
]
w, h = len(trees[0]), len(trees)

visible_n, best_scenic_score = 0, -math.inf
for x, y in it.product(range(w), range(h)):
    visible, scenic_score = False, 1
    for dx, dy in [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]:
        x0, y0 = x, y
        for s0 in it.count(0):
            x0, y0 = x0 + dx, y0 + dy
            k = (0 <= x0 < w and 0 <= y0 < h)
            if k and trees[y0][x0] < trees[y][x]:
                continue

            visible, scenic_score = visible or not k, scenic_score * (s0 + k)
            break
            
    visible_n = visible_n + visible
    best_scenic_score = max(best_scenic_score, scenic_score)
    
print("Part 1:", visible_n)
print("Part 2:", best_scenic_score)