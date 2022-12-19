#!/usr/bin/env python3
""" 2022/16: Proboscidea Volcanium """

import collections as cl
import re
import sys

valves = {
    valve: (int(flowrate), tunnels.split(", "))
        for valve, flowrate, tunnels, *_
        in map(
            lambda x: \
                re.fullmatch(r"^Valve ([A-Z]{2}) has flow rate=(\d*); tunnels? leads? to valves? (([A-Z]{2})(, [A-Z]{2})*)$", x)
                    .groups(),
            sys.stdin.read().strip().split("\n")
        )
}

def p1(t = 30 - 1, p = "AA", state = {}, seen = {}):
    q = sum(
        v * valves[k][0]
            for k, v in state.items()
            if v is not None
    )
    if not t:
        return q
    
    # If we can get to this state faster, don't bother exploring further!
    if seen.get((t, p), -1) >= q:
        return 0
    seen[t, p] = q
    
    # Otherwise, consider all possible moves from here.
    m = 0
    for p0 in [ p ] + valves[p][1]:
        if p == p0:
            if state.get(p) is None and valves[p][0] > 0:
                state[p] = t
            else:
                continue
                
        m = max(m, p1(t - 1, p0, state, seen))
        
        if p == p0:
            state[p] = None
    
    return m

# This is slow, and can probably be optimized quite a bit.
def p2(t = 26 - 1, pA = "AA", pB = "AA", state = {}, seen = {}):
    q = sum(
        v * valves[k][0]
            for k, v in state.items()
            if v is not None
    )
    if not t:
        return q
    
    # If we can get to this state faster, don't bother exploring further!
    if seen.get((t, pA, pB), -1) >= q:
        return 0
    seen[t, pA, pB] = q
    
    # Otherwise, consider all possible moves from here.
    m = 0
    for pA0 in [ pA ] + valves[pA][1]:
        if pA0 == pA:
            if state.get(pA) is None and valves[pA][0] > 0:
                state[pA] = t
            else:
                continue
        
        for pB0 in [ pB ] + valves[pB][1]:
            if pB0 == pB:
                if state.get(pB) is None and valves[pB][0] > 0:
                    state[pB] = t
                else:
                    continue
              
            m = max(m, p2(t - 1, pA0, pB0, state, seen))
            
            if pB0 == pB:
                state[pB] = None
                
        if pA0 == pA:
            state[pA] = None
    
    return m

print("Part 1:", p1())
print("Part 2:", p2())