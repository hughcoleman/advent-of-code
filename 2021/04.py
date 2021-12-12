#!/usr/bin/env python3
""" 2021/04: Giant Squid """

import sys

calls, *boards = sys.stdin.read().strip().split("\n\n")

calls = [int(n) for n in calls.split(",")]
boards = [
    [
        [ int(el) for el in ln.split() ]
            for ln in board.strip().split("\n")
    ]
        for board in boards
]

def score(board, calls):
    return (
        sum(
            board[i][j] if board[i][j] not in calls else 0
                for i in range(5)
                for j in range(5)
        )
      * calls[-1] # assume: `calls` isn't longer than it needs to be
    )

winners = {}
for i in range(len(calls)):
    called = set(calls[:i])

    for j, board in enumerate(boards):
        if j in winners.keys():
            continue

        # Does this board score a bingo after `i` calls are called?
        if (
            any(all(board[k][l] in called for k in range(5)) for l in range(5))
         or any(all(board[l][k] in called for k in range(5)) for l in range(5))
        ):
            winners[j] = i

first = min(winners, key=winners.get)
last  = max(winners, key=winners.get)

print("Part 1:", score(boards[first], calls[:winners[first]]))
print("Part 2:", score(boards[last ], calls[:winners[last ]]))
