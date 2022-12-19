#!/usr/bin/env python3
""" 2022/19: Not Enough Minerals """

import collections as cl
import re
import sys

blueprints = [
    tuple(map(int, re.findall(r"\d+", blueprint)))
        for blueprint in sys.stdin.read().strip().split("\n")
]
assert all(len(blueprint) == 7 for blueprint in blueprints)

def solve(oo, co, Oo, Oc, go, gO, T = 24):
    Q = cl.deque()
    Q.append((0, (0, 0, 0, 0, 1, 0, 0, 0)))
    S = set()
    
    G = 0
    while len(Q) > 0:
        t, (o, c, O, g, No, Nc, NO, Ng) = Q.popleft()
        G = max(G, g)
        
        if t == T or (o, c, O, g, No, Nc, NO, Ng) in S:
            continue
        S.add((o, c, O, g, No, Nc, NO, Ng))
        
        # Could we possibly beat the current best score?
        if (g + Ng*(T - t) + (T - t) * (T - t + 1) // 2) <= G:
            continue
        
        # I believe that the optimizations marked (*) are too aggressive in the
        # general case, but permissive enough to function on the Advent of Code
        # inputs.
        if (
            o >= oo
            and No < max(oo, co, Oo, go)
            and o + (T - t) * No < (T - t) * max(oo, co, Oo, go) # (*)
        ):
            Q.append((t + 1, (o - oo + No, c + Nc, O + NO, g + Ng, No + 1, Nc, NO, Ng)))
        if (
            o >= co
            and Nc < Oc
            and c + (T - t) * Nc < (T - t) * Oc # (*)
        ):
            Q.append((t + 1, (o - co + No, c + Nc, O + NO, g + Ng, No, Nc + 1, NO, Ng)))
        if (
            o >= Oo and c >= Oc
            and NO < gO
            and O + (T - t) * NO < (T - t) * gO # (*)
        ):
            Q.append((t + 1, (o - Oo + No, c - Oc + Nc, O + NO, g + Ng, No, Nc, NO + 1, Ng)))
        if (o >= go and O >= gO):
            Q.append((t + 1, (o - go + No, c + Nc, O - gO + NO, g + Ng, No, Nc, NO, Ng + 1)))
        else:
            Q.append((t + 1, (o + No, c + Nc, O + NO, g + Ng, No, Nc, NO, Ng)))
    
    return G

print("Part 1:", sum(
    i * solve(*blueprint, T = 24)
        for i, *blueprint in blueprints
))
print("Part 2:", (
    solve(*blueprints[0][1:], T = 32)
    * solve(*blueprints[1][1:], T = 32)
    * solve(*blueprints[2][1:], T = 32)
))
