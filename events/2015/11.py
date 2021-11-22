from lib import *
problem = aoc.Problem("2015/11: Corporate Policy")
problem.preprocessor = lambda password: passgen(
    sum(
        "abcdefghijklmnopqrstuvwxyz".index(c) * 26**i
            for i, c in enumerate(reversed(password.strip()))
    )
)

import itertools as it
import re
from string import ascii_lowercase

def passgen(password):
    for i in it.count():
        n = password + i

        s = ""
        while n > 0:
            s = ascii_lowercase[n % 26] + s
            n = n // 26

        yield s

def valid(password):
    return (
        any(
            ord(c1) + 2 == ord(c2) + 1 == ord(c3)
            for c1, c2, c3 in zip(password, password[1:], password[2:])
        )
        and all(confusing not in password for confusing in ["i", "o", "l"])
        and bool(re.search(r"(.)\1.*(.)\2", password))
    )

@problem.solver()
def solve(G):
    password = next(G)
    while not valid(password):
        password = next(G)

    p1 = password

    password = next(G)
    while not valid(password):
        password = next(G)

    return (p1, password)


if __name__ == "__main__":
    problem.solve()
