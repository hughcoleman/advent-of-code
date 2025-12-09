#!/usr/bin/env python3
""" 2025/09: Movie Theater """

import itertools as it
import sys

polygon = list(
    tuple(map(int, ln.split(",")))
        for ln in iter(sys.stdin.readline, "")
)

print("Part 1:", max(
    (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        for (x1, y1), (x2, y2) in it.combinations(polygon, 2)
))

# To determine if the polygon contains a particular rectangle, we'll just check
# if any of the edges of the polygon intersect the rectangle. This turns out to
# be "good enough" for Advent of Code, but it is worth noticing that in general
# this is not correct because the polygon may contain "redundant" edges. For
# example, consider:
#
#     #-----#
#     |.....|
#     #--#..|
#     #--#..|
#     |.....|
#     #-----#
#
# Purely geometrically, this polygon does *not* contain the square S whose
# corners are (0, 0)/(6, 5). However, the problem asks us to work with grid
# squares, and so the small notch at y=2.5 "vanishes" and we do in fact
# consider S to be contained within the polygon.

def is_inside(pt1, pt2, polygon):
    xmin, xmax = sorted([ pt1[0], pt2[0] ])
    ymin, ymax = sorted([ pt1[1], pt2[1] ])
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if y1 == y2:
            if ymin < y1 < ymax and (min(x1, x2) <= xmin < max(x1, x2) or min(x1, x2) < xmax <= max(x1, x2)):
                return False
        elif x1 == x2:
            if xmin < x1 < xmax and (min(y1, y2) <= ymin < max(y1, y2) or min(y1, y2) < ymax <= max(y1, y2)):
                return False
        else:
            assert False, "Expected polygon to be rectilinear."
    return True

print("Part 2:", max(
    (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        for (x1, y1), (x2, y2) in it.combinations(polygon, 2)
        if is_inside((x1, y1), (x2, y2), polygon)
))

