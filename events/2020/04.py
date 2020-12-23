#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/04: Passport Processing")
problem.preprocessor = lambda records: [
    # this parses the list of records into a list dictionaries, with key:value
    # pairs corresponding to the fields of the given passport
    dict(field.split(":") for field in re.split(r"\s", passport) if field)
    for passport in records.split("\n\n")
]

import re

PROTOCOL = {
    "byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
    "iyr": re.compile(r"^(201[0-9]|2020)$"),
    "eyr": re.compile(r"^(202[0-9]|2030)$"),
    "hgt": re.compile(r"^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$"),
    "hcl": re.compile(r"^#[0-9a-f]{6}$"),
    "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
    "pid": re.compile(r"^\d{9}$"),
    "cid": re.compile(r"^.*$"),
}


@problem.solver()
def solve(passports):
    complete, valid = 0, 0
    for passport in passports:
        # first, check if passport is complete
        is_complete = True
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if field not in passport.keys():
                is_complete = False

        # if passport is incomplete, then just skip it
        if not is_complete:
            continue

        complete = complete + 1

        # then, check if passport fields are valid
        is_valid = True
        for field, value in passport.items():
            if not PROTOCOL[field].match(value):
                is_valid = False

        if is_valid:
            valid = valid + 1

    return (complete, valid)


if __name__ == "__main__":
    problem.solve()
