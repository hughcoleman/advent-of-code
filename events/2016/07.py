#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2016/07: Internet Protocol Version 7")
problem.preprocessor = ppr.lsv


def tls(supernet, hypernet):
    def abba(ip):
        return any(
            c1 == c4 and c2 == c3 and c1 != c2
            for c1, c2, c3, c4 in zip(ip, ip[1:], ip[2:], ip[3:])
        )

    return any(abba(s) for s in supernet) and all(
        not abba(s) for s in hypernet
    )


def ssl(supernet, hypernet):
    def aba(sn, hn):
        return any(
            c1 == c3 and c1 != c2 and c2 + c1 + c2 in hn
            for c1, c2, c3 in zip(sn, sn[1:], sn[2:])
        )

    return any(aba(sn, hn) for sn in supernet for hn in hypernet)


@problem.solver()
def solve(ips):
    p1, p2 = 0, 0
    for ip in ips:
        supernet, hypernet = [], []
        token = ""

        depth = 0
        for i, char in enumerate(ip):
            if char in ["[", "]"]:
                if depth <= 0:
                    supernet.append(token)
                else:
                    hypernet.append(token)
                token = ""

                depth = depth + "] [".index(char) - 1
            else:
                token = token + char

        # assuming that all of the addresses are valid, then the last token
        # must be "outside"
        supernet.append(token)

        if tls(supernet, hypernet):
            p1 = p1 + 1

        if ssl(supernet, hypernet):
            p2 = p2 + 1

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()
