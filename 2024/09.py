#!/usr/bin/env python3
""" 2024/09: Disk Fragmenter """

import itertools as it
import sys

disk = [
    (int(c), None if i % 2 == 1 else i // 2)
        for i, c in enumerate(sys.stdin.readline().strip())
]

# For Part 1, we can just traverse the filesystem with two pointers.
filesystem = list(it.chain.from_iterable(
    [file_id]*length for (length, file_id) in disk
))

p1 = 0
i, j = 0, len(filesystem)
while i < j:
    if filesystem[i] is not None:
        p1 = p1 + filesystem[i]*i
    else:
        # Decrement `j` until it is pointing at a file.
        j = j - 1
        while filesystem[j] is None:
            j = j - 1
        p1 = p1 + filesystem[j]*i
    i = i + 1

print("Part 1:", p1)

# For Part 2, we'll operate on the disk "map" and then compute the checksum.
j = len(disk) - 1
while j >= 0:
    if disk[j][1] is not None:
        size = disk[j][0]
        try:
            i, gap = next(filter(
                lambda t: t[0] < j and t[1][0] >= size and t[1][1] is None,
                enumerate(disk)
            ))
            if gap[0] == size:
                disk = disk[:i] + [ disk[j] ] + disk[i + 1:j] + [ (size, None) ] + disk[j + 1:]
            else:
                disk = disk[:i] + [ disk[j], (gap[0] - size, None) ] + disk[i + 1:j] + [ (size, None) ] + disk[j + 1:]
                continue
        except StopIteration: # ...so, no sufficiently large gap.
            pass
    j = j - 1

print("Part 2:",
    sum(
        i*file_id
            for i, file_id in enumerate(it.chain.from_iterable([file_id] * length for (length, file_id) in disk))
            if file_id
    )
)
