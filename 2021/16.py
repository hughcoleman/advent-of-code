#!/usr/bin/env python3
""" 2021/16: Packet Decoder """

import sys
import dataclasses as dc
import functools as ft
from operator import add, mul, gt, lt, eq

message = (
    (int(nibble, 16) >> s) & 1
        for nibble in sys.stdin.read().strip()
        for s in range(3, -1, -1)
)

@dc.dataclass
class Packet:
    version: ...
    tid: ...
    n: ...
    subpackets: ...

    @classmethod
    def parse(cls, message):
        def consume(n):
            return sum(next(message) << i for i in range(n - 1, -1, -1))

        version = consume(3)
        tid = consume(3)

        n, subpackets = 0, []
        if tid == 4:
            while consume(1):
                n = (n << 4) | consume(4)
            n = (n << 4) | consume(4)
        else:
            if consume(1):
                for _ in range(consume(11)):
                    subpackets.append(Packet.parse(message))
            else:
                chunk = (
                    consume(1) for _ in range(consume(15))
                )
                while True:
                    try:
                        subpackets.append(Packet.parse(chunk))
                    except RuntimeError: # "generator raised StopIteration"
                        break

        return Packet(version=version, tid=tid, n=n, subpackets=subpackets)

    def checksum(self):
        return self.version + sum(subpacket.checksum() for subpacket in self.subpackets)

    def eval(self):
        if self.tid == 4:
            return self.n

        return ft.reduce(
            [add, mul, min, max, None, gt, lt, eq][self.tid], (
                subpacket.eval() for subpacket in self.subpackets
            )
        )

p = Packet.parse(message)

print("Part 1:", p.checksum())
print("Part 2:", p.eval())
