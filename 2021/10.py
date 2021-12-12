#!/usr/bin/env python3
""" 2021/10: Syntax Scoring """

import sys

lines = sys.stdin.read().strip().split("\n")

syntax, completion = [], []
for line in lines:
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            if (stack[-1] + c) in ("()", "[]", "{}", "<>"):
                stack = stack[:-1]
            else:
                syntax.append({
                    ")": 3,
                    "]": 57,
                    "}": 1197,
                    ">": 25137
                }[c])
                break
        else:
            assert False
    else:
        # Otherwise, this line is valid but incomplete.
        score = 0
        for c in reversed(stack):
            score = 5 * score + " ([{<".index(c)

        completion.append(score)

print("Part 1:", sum(syntax))
print("Part 2:", sorted(completion)[len(completion) // 2])
