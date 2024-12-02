""" 2024/01: Historian Hysteria """

import sys

left, right = zip(*(
    map(int, entry.split())
        for entry in sys.stdin.read().strip().split("\n")
))

print("Part 1:",
    sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
)
print("Part 2:", sum(l * right.count(l) for l in left))
