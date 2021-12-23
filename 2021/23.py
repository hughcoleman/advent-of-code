#!/usr/bin/env python3
""" 2021/23: Amphipod """

import sys
import heapq as hq

ROOM_X = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

MOVE_COST = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

STOPPABLE = [0, 1, 3, 5, 7, 9, 10]

def dijkstra(amphipods):
    Q = [
        (0, 0, (amphipods, (None, None, None, None, None, None, None, None, None, None, None)))
    ]
    hq.heapify(Q)

    seen = set()
    while len(Q):
        cost, _, (rooms, hallway) = hq.heappop(Q)
        if all(
            all(amphipod == chr(i + 65) for amphipod in room)
                for i, room in enumerate(rooms)
        ):
            return cost

        # Already been here?
        if (rooms, hallway) in seen:
            continue
        seen.add((rooms, hallway))

        # Move an amphipod from a room into the hallway.
        for i, room in enumerate(rooms):
            # We can only move the first amphipod in each room; the others are
            # stuck.
            try:
                j, amphipod = next((j, amphipod) for j, amphipod in enumerate(room) if amphipod)
            except StopIteration:
                continue

            # If this amphipod, and all others behind it, are in the correct
            # room, then don't move.
            if all(room[k] == chr(i + 65) for k in range(j, len(room))):
               continue

            # We can move to any non-junction cell in the hallway.
            for p in STOPPABLE:
                # Check if path is obstructed.
                p1, p2 = 2*i + 2, p
                if p1 > p2:
                    p1, p2 = p2, p1

                if any(hallway[k] is not None for k in range(p1, p2 + 1)):
                    continue

                _cost = cost + MOVE_COST[amphipod]*(j + p2 - p1 + 1)
                _rooms = tuple(
                    tuple(
                        None if (i_ == i and j_ == j) else amphipod
                            for j_, amphipod in enumerate(room)
                    )
                        for i_, room in enumerate(rooms)
                )
                _hallway = tuple(
                    amphipod if p_ == p else h
                        for p_, h in enumerate(hallway)
                )

                hq.heappush(
                    Q, (_cost, id(_rooms), (_rooms, _hallway))
                )

        # Move an amphibian from the hallway into their room.
        for p in STOPPABLE:
            amphipod = hallway[p]
            if amphipod is None:
                continue

            # Check if path is obstructed.
            p1, p2 = ROOM_X[amphipod], p
            if p < ROOM_X[amphipod]:
                p1, p2 = p2 + 1, p1 + 1

            if all(hallway[k] is None for k in range(p1, p2)):
                i = ord(amphipod) - 65
                room = rooms[i]

                # Check if the room is safe to enter.
                if any(c is not None and c != amphipod for c in room):
                    continue

                # Go as far in as possible!
                try:
                    j = next(j for j, c in enumerate(room) if c is not None) - 1
                except StopIteration:
                    j = len(room) - 1

                _cost = cost + MOVE_COST[amphipod]*(j + abs(ROOM_X[amphipod] - p) + 1)
                _rooms = tuple(
                    tuple(
                        amphipod if (k == i and l == j) else h
                            for l, h in enumerate(room)
                    )
                        for k, room in enumerate(rooms)
                )
                _hallway = tuple(
                    None if k == p else h
                        for k, h in enumerate(hallway)
                )

                hq.heappush(
                    Q, (_cost, id(_rooms), (_rooms, _hallway))
                )

burrow = [
    list(ln) for ln in sys.stdin.read().strip().split("\n")
]

rooms = tuple(
    (burrow[2][i], burrow[3][i])
        for i in [3, 5, 7, 9]
)

print("Part 1:", dijkstra(rooms))

print("Part 2:",
    dijkstra(
        tuple(
            (rooms[i][0], *fold, rooms[i][1])
                for i, fold in enumerate(["DD", "CB", "BA", "AC"])
        )
    )
)
