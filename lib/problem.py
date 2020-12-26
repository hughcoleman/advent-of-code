#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import time
import pathlib
import fileinput


class Problem:
    """class Problem

    Represents and provides methods relating to a single Advent of Code
    problem.
    """

    def __init__(self, *args, **kwargs):
        """constructor()

        Pass the year, month, and problem name to the constructor to
        instantiate a new Problem.

            Problem("2015/01: Not Quite Lisp")
            Problem(year=2015, day=1, name="Not Quite Lisp")
        """

        if (
            match := re.fullmatch(  # noqa: E231
                re.compile(
                    r"(?P<year>[0-9]{4})\/"
                    + r"(?P<day>0?[1-9]|1[0-9]|2[0-5])\: "
                    + r"(?P<name>.+)"
                ),
                "".join(args),
            )
        ) :
            self.year = int(match.group("year"))
            self.day = int(match.group("day"))
            self.name = str(match.group("name"))
        elif all(field in kwargs.keys() for field in ["year", "day", "name"]):
            self.year = int(kwargs.get("year", 0))
            self.day = int(kwargs.get("day", 0))
            self.name = str(kwargs.get("name", "???"))
        else:
            raise ValueError(
                "could not parse arguments to Problem " + "constructor."
            )

        # the solver functions, and the input preprocessor, are stored as class
        # fields.
        self.fns = {}
        self.preprocessor = lambda x: x

        # all tests are user-defined
        self.tests = {}

    def solver(self, part="both"):
        """Decorates a function to mark it as a solving method. Optionally
        specify the part being solved using the `part` keyword argument.
        """

        def register(fn):
            # register the solver function in the instance dictionary variable
            # `self.fns`.
            self.fns[part] = fn
            return fn

        return register

    def solve(self):
        """ Run the solver functions and pretty-print the output. """

        # print a neat little header for the problem
        print(f"--- Day {self.day}: {self.name} ---")

        # setup the path to the local cache
        fp = pathlib.Path(
            f"~/.cache/adventofcode.com/{str(self.year)}/"
            + f"{str(self.day).zfill(2)}/input"
        ).expanduser()

        # if the input isn't cached, or an overwrite is forced, check stdin and
        # argv for the input data
        if not fp.exists() or ("--overwrite" in sys.argv):
            if "--overwrite" in sys.argv:
                # because fileinput will try to read from a file called
                # "--overwrite" otherwise
                sys.argv.remove("--overwrite")
                print("[!] Overwriting input file using stdin...")
            else:
                print("[!] Writing to input file from stdin...")

            # fileinput automatically checks sys.stdin as well as argv[1:]
            with fileinput.input() as fh:
                inp_s = ""
                for ln in fh:
                    inp_s = inp_s + ln

            # easy sanity checking
            print(repr(inp_s)[:32] + "..." + repr(inp_s)[-32:])

            # write the input data to the local cache
            fp.parent.mkdir(parents=True, exist_ok=True)
            with open(fp, "w") as fh:
                fh.write(inp_s)
        else:
            print("Reading input from local cache...")

            # now, read the input from the local cache
            with open(fp, "r") as fh:
                inp_s = fh.read()

        # run each solver in the self.fns field.
        for part, fn in self.fns.items():
            # apply the preprocessor
            inp = self.preprocessor(inp_s)

            # run the solver on the input and time the runtime
            start = time.perf_counter()
            out = fn(inp)
            end = time.perf_counter()

            # compute runtime and appropriate time unit
            delta, unit = (end - start), 0
            while delta < 1 and unit <= 3:
                delta, unit = 1000 * delta, unit + 1
            delta, unit = round(delta, 5), ["s", "ms", "us", "ns"][unit]

            # print answers
            if (part in ["both"]) and (type(out) is tuple) and (len(out) >= 2):
                print(f"Part 1: {out[0]}")
                print(f"Part 2: {out[1]} (total runtime: {delta}{unit})")
            else:
                print(f"Part {part}: {out} (runtime: {delta}{unit})")

        return
