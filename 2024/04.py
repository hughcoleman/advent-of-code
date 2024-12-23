#!/usr/bin/env python3
""" 2024/04: Ceres Search """

import itertools as it
import sys

wordsearch = {
    (r, c): ch
        for r, line in enumerate(sys.stdin.read().strip().split("\n"))
        for c, ch in enumerate(line)
}

print("Part 1:",
    sum(
        (dr != 0 or dc != 0) and all(wordsearch.get((r + dr*i, c + dc*i)) == "XMAS"[i] for i in range(4))
            for (r, c) in wordsearch.keys()
            for (dr, dc) in it.product((-1, 0, 1), repeat=2)
    )
)
print("Part 2:",
    sum(
        ch == "A"
        and { wordsearch.get((r - 1, c - 1)), wordsearch.get((r + 1, c + 1)) } == { "M", "S" }
        and { wordsearch.get((r + 1, c - 1)), wordsearch.get((r - 1, c + 1)) } == { "M", "S" }
            for (r, c), ch in wordsearch.items()
    )
)
