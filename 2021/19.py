#!/usr/bin/env python3
""" 2021/19: Beacon Scanner """

import sys
import itertools as it

scans = [
    [
        tuple(int(coordinate) for coordinate in point.split(","))
            for point in scanner.split("\n")[1:]
    ]
        for scanner in sys.stdin.read().strip().split("\n\n")
]

fingerprints = [ [] for _ in range(len(scans)) ]
for n, scan in enumerate(scans):
    for i, p1 in enumerate(scan):
        fingerprints[n].append(
            frozenset(
                tuple(sorted(abs(p1[l] - p2[l]) for l in range(3)))
                    for p2 in scan
            )
        )

def align(A, B):
    # Find the transformation (rotation and translation) that maps the points
    # in B to the corresponding points in A.
    #
    # This can be done easily with some linear algebra:
    #
    #     1. We construct three systems of equations that separately describe
    #        the translation along the x-, y-, and z-axes.
    #
    #            | b[0].x  b[0].y  b[0].z  1 |    | rxx |    | a[0].x |
    #            | b[1].x  b[1].y  b[1].z  1 | \/ | rxy | -- | a[1].x |
    #            | b[2].x  b[2].y  b[2].z  1 | /\ | rxx | -- | a[2].x |
    #            | b[3].x  b[3].y  b[3].z  1 |    | dx  |    | a[3].x |
    #
    #            | b[0].x  b[0].y  b[0].z  1 |    | ryx |    | a[0].y |
    #            | b[1].x  b[1].y  b[1].z  1 | \/ | ryy | -- | a[1].y |
    #            | b[2].x  b[2].y  b[2].z  1 | /\ | ryx | -- | a[2].y |
    #            | b[3].x  b[3].y  b[3].z  1 |    | dy  |    | a[3].y |
    #
    #            | b[0].x  b[0].y  b[0].z  1 |    | rzx |    | a[0].z |
    #            | b[1].x  b[1].y  b[1].z  1 | \/ | rzy | -- | a[1].z |
    #            | b[2].x  b[2].y  b[2].z  1 | /\ | rzz | -- | a[2].z |
    #            | b[3].x  b[3].y  b[3].z  1 |    | dx  |    | a[3].z |
    #
    #     2. Assuming that we have linear independence among the rows of the
    #        left-hand matrix, we can solve these systems and and use their
    #        solutions to construct the homogenous transformation matrix that
    #        transforms B to A.
    #
    #            | rxx  rxy  rxx  dx |
    #            | ryx  ryy  ryx  dx |
    #            | rzx  rzy  rzx  dx |
    #            |  0    0    0    1 |
    #
    # However, we don't need to "properly" solve these systems (via, say,
    # Gaussian elimination) due to additional restrictions that this puzzle
    # imposes (for example, only one of { rxx, rxy, rxx } can be non-zero and
    # this non-zero value must be +/- 1.)

    for (a1, b1), (a2, b2) in it.combinations(
        (
            (p1, p2)
                for (i, p1), (j, p2) in it.product(
                    enumerate(scans[A]), enumerate(scans[B])
                )
                if len(fingerprints[A][i] & fingerprints[B][j]) >= 12
        ), 2
    ):
        X = []
        for d1 in range(3):
            x = []
            d = a1[d1] - a2[d1]
            for d2 in range(3):
                if b2[d2] - b1[d2] == d:
                    x.append((-1, d2, a1[d1] + b1[d2]))
                if b1[d2] - b2[d2] == d:
                    x.append(( 1, d2, a1[d1] - b1[d2]))

            # More than one possible transformation?
            if len(x) != 1:
                break
            X.append(x[0])
        else:
            return X[0] + X[1] + X[2]

scanners = {
    0: (0, 0, 0)
}
beacons = set( scans[0] )

while len(scanners.keys()) < len(scans):
    for n in range(len(scans)):
        if n in scanners:
            continue

        fingerprint = frozenset().union(*fingerprints[n])
        for m in scanners.keys():
            # Skip this reference scan if the scans provably do not overlap.
            if (
                sum(
                    d in fingerprint
                        for d in it.chain.from_iterable(fingerprints[m])
                ) < 66
            ):
                continue

            h = align(m, n)
            if h:
                sx, ax, dx, sy, ay, dy, sz, az, dz = h

                # Transform this scan.
                scans[n] = [
                    (sx*p[ax] + dx, sy*p[ay] + dy, sz*p[az] + dz)
                        for p in scans[n]
                ]

                scanners[n] = (dx, dy, dz)
                beacons |= set(scans[n])
                break

print("Part 1:", len(beacons))

print("Part 2:",
    max(
        sum(abs(m[i] - n[i]) for i in range(3))
            for m, n in it.combinations(scanners.values(), 2)
    )
)
