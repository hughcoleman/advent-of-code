#!/usr/bin/env python3
""" 2023/02: Cube Conundrum """

import math
import sys

games = {
    int(_id): [
        {
            colour: int(n)
                for n, colour in map(lambda k: k.split(" "), draws)
        }
            for draws in map(lambda k: k.split(", "), game.strip().split("; "))
    ]
        for _id, game in map(lambda k: k[5:].split(": "), sys.stdin.readlines())
}

print("Part 1:",
    sum(
        _id for _id, game in games.items()
            if all(
                draw.get("red", 0) <= 12
                and draw.get("green", 0) <= 13
                and draw.get("blue", 0) <= 14
                    for draw in game
            )
    )
)
print("Part 2:",
    sum(
        max(draw.get("red", 0) for draw in game)
        * max(draw.get("green", 0) for draw in game)
        * max(draw.get("blue", 0) for draw in game)
            for _, game in games.items()
    )
)
