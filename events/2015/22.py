from lib import *
problem = aoc.Problem("2015/22: Wizard Simulator 20XX")
problem.preprocessor = ppr.lsv

import heapq as hq
import math

def simulate(B_HEALTH, B_ATTACK, P_HEALTH, P_MANA, hard=False):
    cheapest = math.inf

    Q = [(B_HEALTH, P_HEALTH, P_MANA, 0x000, 0, 0, hard)]
    hq.heapify(Q)

    while len(Q) > 0:
        boss, player, mana, effects, turn, expended, hard = hq.heappop(Q)

        # If we've expended more mana than the known minimum, skip.
        if expended > cheapest:
            continue

        # Handle hard mode.
        if hard and turn % 2 == 0:
            player = player - 1

            if player <= 0:
                continue

        # Apply the consequences of any effects that are currently active, and
        # cooldown.
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

        # Check boss health (died from POISON?)
        if boss <= 0:
            cheapest = min(cheapest, expended)

        # Even-numbered turns are the player's turns.
        if turn % 2 <= 0:
            # Cast all castable spells, and simulate out those cases until
            # failiure.
            if mana >= 53:  # MAGIC_MISSILE
                hq.heappush(Q,
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
                hq.heappush(Q,
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
                hq.heappush(Q,
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
                hq.heappush(Q,
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
                hq.heappush(Q,
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

        # Odd-numbered turns are the boss' turns.
        else:
            player = player - max(1, B_ATTACK - armor)
            if player > 0:
                hq.heappush(Q,
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
