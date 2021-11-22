from lib import *
problem = aoc.Problem("2015/05: Doesn't He Have Intern-Elves For This?")
problem.preprocessor = ppr.lsv

import re

@problem.solver(part=1)
def p1(strings):
    valid = 0
    for string in strings:
        if (
            (sum(string.count(vowel) for vowel in "aeiou") >= 3)
            and (all(bl not in string for bl in ["ab", "cd", "pq", "xy"]))
            and (any(c1 == c2 for c1, c2 in zip(string, string[1:])))
        ):
            valid = valid + 1

    return valid

@problem.solver(part=2)
def p2(strings):
    valid = 0
    for string in strings:
        # I tried to write a Python-ic solution, but gave up. Regex!
        if re.search(r"(..).*\1", string) and re.search(r"(.).\1", string):
            valid = valid + 1

    return valid


if __name__ == "__main__":
    problem.solve()
