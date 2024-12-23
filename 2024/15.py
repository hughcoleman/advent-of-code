#!/usr/bin/env python3
""" 2024/15: Warehouse Woes """

import sys

warehouse, moves = sys.stdin.read().strip().split("\n\n")
moves = [
    { "^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1) }[move]
        for move in moves.replace("\n", "")
]

def push(W, r, c, dr, dc):
    if W[r + dr, c + dc] == ".":
        W[r, c], W[r + dr, c + dc] = W[r + dr, c + dc], W[r, c]
    elif W[r + dr, c + dc] == "#":
        raise "Cannot push wall."
    elif W[r + dr, c + dc] == "O":
        push(W, r + dr, c + dc, dr, dc)
        W[r, c], W[r + dr, c + dc] = W[r + dr, c + dc], W[r, c]
    elif W[r + dr, c + dc] == "[":
        push(W, r + dr, c + dc + 1, dr, dc)
        push(W, r + dr, c + dc    , dr, dc)
        W[r, c], W[r + dr, c + dc] = W[r + dr, c + dc], W[r, c]
    elif W[r + dr, c + dc] == "]":
        push(W, r + dr, c + dc - 1, dr, dc)
        push(W, r + dr, c + dc    , dr, dc)
        W[r, c], W[r + dr, c + dc] = W[r + dr, c + dc], W[r, c]

def execute(warehouse, moves):
    warehouse = {
        (r, c): ch
            for r, line in enumerate(warehouse.split("\n"))
            for c, ch in enumerate(line)
    }
    (r0, c0), = ((r, c) for (r, c), ch in warehouse.items() if ch == "@")

    # We'll always operate on a copy of `warehouse`, rolling back if we can't
    # push.
    r, c = r0, c0
    for (dr, dc) in moves:
        warehouse0 = warehouse.copy()
        try:
            push(warehouse, r, c, dr, dc)
            r, c = r + dr, c + dc
        except:
            warehouse = warehouse0

    return sum(100*r + c for (r, c), ch in warehouse.items() if ch in "O[")

print("Part 1:", execute(warehouse, moves))
print("Part 2:",
    execute(
        warehouse.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@."),
        moves,
    )
)
