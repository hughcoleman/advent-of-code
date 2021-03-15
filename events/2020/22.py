#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *

problem = aoc.Problem("2020/22: Crab Combat")
problem.preprocessor = lambda cards: (
    deque(int(c) for c in cards.strip().split("\n\n")[0].split("\n")[1:]),
    deque(int(c) for c in cards.strip().split("\n\n")[1].split("\n")[1:]),
)

from collections import deque


def score(cards):
    score = 0
    for position, card in enumerate(list(cards)[::-1], 1):
        score += position * card

    return score


@problem.solver(part=1)
def combat(cards):
    p1, p2 = cards
    while len(p1) > 0 and len(p2) > 0:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            winner = p1
        elif c2 > c1:
            winner = p2

        assert winner != None
        winner.extend([max(c1, c2), min(c1, c2)])

    return score(p1 or p2)


@problem.solver(part=2)
def recursive_combat(cards):
    p1, p2 = cards

    def play(p1, p2, depth=1):
        # if Player 1 has the higher card, and this isn't the top-level game,
        # then we can break out early because Player 1 must win (via
        # repetition or via normal combat; will never recurse if 50 is played.)
        if (depth > 1) and (50 in p1):
            return deque([1]), deque([])

        played = set()
        while len(p1) > 0 and len(p2) > 0:
            if (tuple(p1), tuple(p2)) in played:
                return 1, p1
            played.add((tuple(p1), tuple(p2)))

            c1, c2 = p1.popleft(), p2.popleft()
            if len(p1) >= c1 and len(p2) >= c2:
                # the beauty of recursive combat...
                _p1, _p2 = play(
                    deque(list(p1)[:c1]), deque(list(p2)[:c2]), depth + 1
                )

                winner = (_p1 and p1) or (_p2 and p2)
            else:
                if c1 > c2:
                    winner = p1
                elif c2 > c1:
                    winner = p2

            # always append winner's card first
            winner.append(c1 if winner is p1 else c2)
            winner.append(c2 if winner is p1 else c1)

        return (p1, p2)

    p1, p2 = play(p1, p2)
    return score(p1 or p2)


# tests?

if __name__ == "__main__":
    problem.solve()
