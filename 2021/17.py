#!/usr/bin/env python3
""" 2021/17: Trick Shot """

import sys
import re

min_x, max_x, min_y, max_y = map(
    int, re.findall(r"-?\d+", sys.stdin.read())
)

print("Part 1:",
    -min_y * (-min_y - 1) // 2
)

def launch(vx, vy):
    x, y = 0, 0
    while x <= max_x and y >= min_y:
        x = x + vx; y = y + vy
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True

        vx = max(0, vx - 1)
        vy = vy - 1

    return False

print("Part 2:", sum(
    launch(vx, vy)
        for vx in range(int((2*min_x) ** 0.5), max_x + 1)
        for vy in range(min_y, -min_y)
))
