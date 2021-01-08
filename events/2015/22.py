#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2015/22: Wizard Simulator 20XX")
problem.preprocessor = ppr.lsv


import math


def simulate(B_HEALTH, B_ATTACK, P_HEALTH, P_MANA, hard=False):
    cheapest = math.inf

    horizon = [(B_HEALTH, P_HEALTH, P_MANA, 0x000, 0, 0, hard)]
    while len(horizon) > 0:
        boss, player, mana, effects, turn, expended, hard = horizon.pop(0)

        # if we've expended more mana than the known minimum, skip
        if expended > cheapest:
            continue

        # handle hard mode
        if hard and turn % 2 == 0:
            player = player - 1

            if player <= 0:
                continue

        # apply the consequences of any effects that are currently active, and
        # cooldown
        armor = 0
        if effects & 0xF00 > 0:  # SHIELD
            armor = 7
            effects = effects - 0x100
        if effects & 0x0F0 > 0:  # POISON
            boss = boss - 3
            effects = effects - 0x010
        if effects & 0x00F > 0:  # RECHARGE
            mana = mana + 101
            effects = effects - 0x001

        # check boss health (died from POISON?)
        if boss <= 0:
            cheapest = min(cheapest, expended)

        # even-numbered turns are the player's turns
        if turn % 2 <= 0:
            # cast all castable spells, and simulate out those cases until
            # failiure
            if mana >= 53:  # MAGIC_MISSILE
                horizon.append(
                    (
                        boss - 4,
                        player,
                        mana - 53,
                        effects,
                        turn + 1,
                        expended + 53,
                        hard,
                    )
                )

            if mana >= 73:  # DRAIN
                horizon.append(
                    (
                        boss - 2,
                        player + 2,
                        mana - 73,
                        effects,
                        turn + 1,
                        expended + 73,
                        hard,
                    )
                )

            if mana >= 113 and effects & 0xF00 <= 0:  # SHIELD
                horizon.append(
                    (
                        boss,
                        player,
                        mana - 113,
                        effects + 0x600,
                        turn + 1,
                        expended + 113,
                        hard,
                    )
                )

            if mana >= 173 and effects & 0x0F0 <= 0:  # POISON
                horizon.append(
                    (
                        boss,
                        player,
                        mana - 173,
                        effects + 0x060,
                        turn + 1,
                        expended + 173,
                        hard,
                    )
                )

            if mana >= 229 and effects & 0x00F <= 0:  # RECHARGE
                horizon.append(
                    (
                        boss,
                        player,
                        mana - 229,
                        effects + 0x005,
                        turn + 1,
                        expended + 229,
                        hard,
                    )
                )

        # odd-numbered turns are the boss' turns
        else:
            player = player - max(1, B_ATTACK - armor)
            if player > 0:
                horizon.append(
                    (boss, player, mana, effects, turn + 1, expended, hard)
                )

    return cheapest


@problem.solver()
def solve(inp):
    BOSS_HEALTH = int(inp[0].split(": ")[1])
    BOSS_ATTACK = int(inp[1].split(": ")[1])

    return (
        simulate(BOSS_HEALTH, BOSS_ATTACK, 50, 500),
        simulate(BOSS_HEALTH, BOSS_ATTACK, 50, 500, hard=True),
    )


if __name__ == "__main__":
    problem.solve()
