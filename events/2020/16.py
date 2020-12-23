#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2020/16: Ticket Translation")
problem.preprocessor = lambda tickets: (
    # shitty as-all-fuck input parsing for the win!
    # 1. Validation Rules
    #    Parses the list of validation rules for ticket fields into a
    #    dictionary, structured {name: ((lo_1, hi_1), (lo_2, hi_2), ...*)}
    #
    # *  in the input, all fields have two ranges... but this should nicely
    #    handle the cases where there are three/four/five different ranges for
    #    each of the fields.
    {
        field: tuple(
            tuple(int(d) for d in range_.split("-"))
            for range_ in ranges.split(" or ")
        )
        for field, ranges in [
            ticket.split(": ")
            for ticket in tickets.strip().split("\n\n")[0].split("\n")
        ]
    },
    # 2. Mine!
    #    Parses our train ticket into a list of its fields.
    [
        int(field)
        for field in tickets.strip().split("\n\n")[1].split("\n")[1].split(",")
    ],
    # 3. Others
    #    Parses the list of others' train tickets into a list of list of
    #    integers.
    [
        [int(field) for field in ticket.split(",")]
        for ticket in tickets.strip().split("\n\n")[2].split("\n")[1:]
    ],
)

from collections import defaultdict


@problem.solver()
def solve(tickets):
    rules, mine, others = tickets
    fields = len(mine)  # no. fields

    # some basic sanity-checking, because I don't exactly "trust" the spaghetti
    # preprocessor I wrote.
    assert len(rules.keys()) == len(mine)
    assert all(len(ticket) == len(mine) for ticket in others)

    valid = []
    errors = 0
    for ticket in others:
        # iterate over each field in the ticket, check if it meets at least one
        # of the rule ranges
        for field in ticket:
            for _, ranges in rules.items():
                for (lo, hi) in ranges:
                    if lo <= field <= hi:
                        # it's valid; is in the range (lo, hi)
                        break
                else:
                    # if it didn't meet any of the `ranges`, try the next \
                    # possible range
                    continue

                # this disaster for-else tree is "Exhibit A: Why this
                # validation routine needs to be in a separate function."
                break
            else:
                # field is invalid
                errors = errors + field
                break

        else:
            # if the /entire/ ticket is valid...
            valid.append(ticket)

    # keep track of possible positions that each field could represent.
    positions = {rule: set(range(fields)) for rule in rules.keys()}

    for field in range(fields):
        for rule, ranges in rules.items():

            # check that the candidate rule matches all the tickets
            for i, ticket in enumerate(valid):
                for (lo, hi) in ranges:
                    if lo <= ticket[field] <= hi:
                        break
                else:
                    # if the ranges of this rule doesn't validate one or more
                    # of the values in this "column", then that rule can't
                    # represent this field position.
                    if field in positions[rule]:
                        positions[rule].remove(field)

    resolved = {}
    while len(resolved.items()) < fields:
        progress = False

        # eliminate naked singles (ie. fields that represent only one column)
        for rule, candidates in positions.items():
            if rule in resolved.keys():
                continue

            positions[rule] = candidates - set(resolved.values())
            if len(positions[rule]) <= 1:
                (resolved[rule],) = positions[rule]
                progress = True

        # eliminate hidden singles (ie. columns that are only represented by
        # one field)
        references = defaultdict(int)
        for rule, candidates in positions.items():
            for candidate in candidates:
                references[candidate] += 1

        for i, count in references.items():
            if (count > 1) or (i in resolved.items()):
                continue

            for rule, candidates in positions.items():
                if i in candidates:
                    positions[rule] = (i,)
                    resolved[rule] = i
                    progress = True

        # this could probably be made more efficient by considering
        # naked/hidden doubles, triples, and quadruples, but I can't be
        # bothered to figure out how to implement that
        #
        # see https://www.reddit.com/r/adventofcode/comments/kf8mlu/2020_day_16_part_3_a_different_number_system/

        # we only need to resolve the six fields with "departure" in the name,
        # so if we are able to resolve all of those, just break out early
        if sum(1 if "departure" in r else 0 for r in resolved.keys()) >= 6:
            break

        # if no progress was made, then the grid is as deduced as it will be
        if not progress:
            raise RuntimeError("Solved as much as possible.")

    # now, compute the product of the six fields on our ticket that starts with
    # "departure"
    product = 1
    for field, position in resolved.items():
        if field.startswith("departure"):
            product *= mine[position]

    return (errors, product)


if __name__ == "__main__":
    problem.solve()
