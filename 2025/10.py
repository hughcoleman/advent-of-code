#!/usr/bin/env python3
""" 2025/10: Factory """

import itertools as it
import sys
import z3

part1, part2 = 0, 0
for machine in iter(sys.stdin.readline, ""):
    pattern, *buttons, joltages = machine.split()

    # Parse the pattern, buttons, and joltages into appropriate structures.
    pattern = pattern[1:-1]
    buttons = [
        set(map(int, button[1:-1].split(',')))
            for button in buttons
    ]
    joltages = list(map(int, joltages[1:-1].split(',')))

    # For Part 1, we'll just brute-force over the possible choices of buttons
    # to press.
    part1 = part1 + next(
        N   for N in it.count(0)
            for pressed in it.combinations(buttons, N)
            if (
                "".join(
                    ".#"[sum((i in btn for btn in pressed)) % 2]
                        for i in range(len(pattern))
                )
                == pattern
            )
    )

    # For Part 2, we'll pass to z3-solver to identify the optimal solution. It
    # (hopefully) recognizes that this is an integer linear programming
    # problem and applies a suitable algorithm.
    presses = [
        z3.Int(f"press{i}") for i in range(len(buttons))
    ]

    s = z3.Optimize()
    s.add(z3.And([press >= 0 for press in presses]))
    s.add(z3.And([
        sum(presses[j] for j, button in enumerate(buttons) if i in button) == joltage
            for i, joltage in enumerate(joltages)
    ]))
    s.minimize(sum(presses))
    assert s.check() == z3.sat

    m = s.model()
    for press in presses:
        part2 = part2 + m[press].as_long()

print("Part 1:", part1)
print("Part 2:", part2)
