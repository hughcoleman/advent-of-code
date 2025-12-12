#!/usr/bin/env python3
""" 2025/12: Christmas Tree Farm """

import re
import sys

*shapes, regions = sys.stdin.read().strip().split('\n\n')

regions = [
    list(map(int, re.findall(r'\d+', region)))
        for region in regions.split('\n')
]

# This problem is a massive fakeout; each problem either "obviously" fits or
# "obviously" does not. Merry Christmas!?
def fail():
    assert False, "Failed to determine if presents fit under tree."

print("Part 1:", sum(
         1      if (w // 3) * (h // 3) >= sum(nums)
    else 0      if sum(num*shape.count('#') for num, shape in zip(nums, shapes)) > w * h
    else fail()
        for w, h, *nums in regions
))
print("Part 2:", "Finish Decorating the North Pole")
