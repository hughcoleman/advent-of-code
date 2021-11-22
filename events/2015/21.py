from lib import *
problem = aoc.Problem("2015/21: RPG Simulator 20XX")
problem.preprocessor = ppr.lsv

import math
import itertools

# The number of hits that it will take a given entity to perish is.
#
#     math.ceil(PLAYER_HEALTH / max(BOSS_ATTACK - PLAYER_DEFENCE, 1))
#     math.ceil(BOSS_HEALTH / max(PLAYER_ATTACK - BOSS_DEFENCE, 1))
#
# Because the player always goes first, as long as
# PLAYER_RESILIENCE >= BOSS_RESILIENCE, then we can guarantee victory.

WEAPONS = [
    (8, 4, 0),   # Dagger
    (10, 5, 0),  # Shortsword
    (25, 6, 0),  # Warhammer
    (40, 7, 0),  # Longsword
    (74, 8, 0),  # Greataxe
]

ARMOR = [
    (13, 0, 1),   # Leather
    (31, 0, 2),   # Chainmail
    (53, 0, 3),   # Splintmail
    (75, 0, 4),   # Bandedmail
    (102, 0, 5),  # Platemail
]

RINGS = [
    (25, 1, 0),   # Damage I
    (50, 2, 0),   # Damage II
    (100, 3, 0),  # Damage III
    (20, 0, 1),   # Defense I
    (40, 0, 2),   # Defense II
    (80, 0, 3),   # Defense III
]

# Add no-armor options.
ARMOR.append((0, 0, 0))

# Compute ring pairings.
for pairing in itertools.combinations(RINGS, 2):
    RINGS.append(tuple(sum(i) for i in zip(*pairing)))
RINGS.append((0, 0, 0))

@problem.solver()
def solve(inp):
    p1, p2 = math.inf, -math.inf

    BOSS_HEALTH = float(inp[0].split(": ")[1])
    BOSS_ATTACK = float(inp[1].split(": ")[1])
    BOSS_DEFENSE = float(inp[2].split(": ")[1])

    PLAYER_HEALTH = float(100)
    PLAYER_ATTACK = float(0)
    PLAYER_DEFENSE = float(0)

    for weapon in WEAPONS:
        for armor in ARMOR:
            for ring in RINGS:
                PLAYER_ATTACK = weapon[1] + armor[1] + ring[1]
                PLAYER_DEFENSE = weapon[2] + armor[2] + ring[2]

                PLAYER_RESILIENCE = math.ceil(
                    PLAYER_HEALTH / max(BOSS_ATTACK - PLAYER_DEFENSE, 1)
                )

                BOSS_RESILIENCE = math.ceil(
                    BOSS_HEALTH / max(PLAYER_ATTACK - BOSS_DEFENSE, 1)
                )

                cost = weapon[0] + armor[0] + ring[0]
                if PLAYER_RESILIENCE >= BOSS_RESILIENCE:
                    p1 = min(p1, cost)
                else:
                    p2 = max(p2, cost)

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
