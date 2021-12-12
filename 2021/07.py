#!/usr/bin/env python3
""" 2021/07: The Treachery of Whales """

import sys
import math
import statistics

positions = [
    int(position) for position in sys.stdin.read().strip().split(",")
]

def cost(positions, f=lambda x: x):
    min_x = min(positions)
    max_x = max(positions)

    return min(
        sum(f(abs(position - d)) for position in positions)
            for d in range(min_x, max_x + 1)
    )

# Since there are only 1000 crabs, it's easy enough to brute-force -- it takes
# about a second.
if False:
    print("Part 1:", cost(positions))
    print("Part 2:", cost(positions, f=lambda x: x * (x + 1) // 2))

# ....however, we can do better!
#
#   - For Part 1, we can align the crabs to the median of all their positions,
#     since that will minimize the sum of the absolute deviations (which is
#     equivalent to the puzzle.) In the case that our median is not an integer,
#     we can arbitrarily round up or down; both will consume the same amount of
#     fuel.
#
#   - For Part 2, we can instead align the crabs to the mean of all their
#     positions, since that will minimize the sum of the squares of the
#     absolute differences.
#
#     NB: This isn't equivalent to the puzzle -- the puzzle asks us to minimize
#         quantity (n * (n + 1)) / 2 = (n^2 + n) / 2. However, it can easily
#         be shown that cheapest alignment point will fall within +/- 0.5 of
#         the mean. It is trivial to check both floor(mean) and ceil(mean) and
#         pick the cheaper one.
#

median = math.floor(statistics.median(positions))
print("Part 1:", sum(abs(position - median) for position in positions))

means = [
    f(statistics.mean(positions)) for f in [ math.floor, math.ceil ]
]
print("Part 2:",
    min(
        sum((lambda x: x * (x + 1) // 2)(abs(position - mean)) for position in positions)
            for mean in means
    )
)
