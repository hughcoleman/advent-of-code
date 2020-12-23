#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import os
import pathlib
import re
import sys
import time

from .net import fetch


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

        if "--test" in sys.argv:
            self.test()

        # print a neat little header for the problem
        print(f"--- Day {self.day}: {self.name} ---")

        # setup the path to the local cache
        fp = pathlib.Path(
            f"~/.cache/adventofcode.com/{str(self.year)}/"
            + f"{str(self.day).zfill(2)}/input"
        ).expanduser()

        # if the input isn't cached, download from the adventofcode.com server
        # and cache
        if not fp.exists():
            print(
                "No cached input; downloading from "
                + "\u001b[4madventofcode.com\u001b[0m..."
            )

            # first check the current time to ensure that it is past midnight
            # est before fetching problem input from server
            est = dt.timezone(dt.timedelta(hours=-5))
            delta = dt.datetime(
                self.year, 12, self.day, tzinfo=est
            ) - dt.datetime.now(tz=est)

            if dt.timedelta(seconds=0) < delta <= dt.timedelta(seconds=15):
                print("Less than fifteen seconds remaining, will sleep...")
                sys.stdout.flush()
                time.sleep(delta.seconds + 1)

            elif delta > dt.timedelta(seconds=0):
                # determine time remaining until unlock and display a formatted
                # countdown timer
                d = delta.days
                h = (delta.seconds // 3600) % 24
                m = (delta.seconds // 60) % 60
                s = (delta.seconds) % 60

                countdown = (
                    (f"{str(d).zfill(2)}d" if d > 0 else "")
                    + (f"{str(h).zfill(2)}h" if h > 0 else "")
                    + (f"{str(m).zfill(2)}m" if m > 0 else "")
                    + (f"{str(s).zfill(2)}s")
                )

                print("Problem hasn't unlocked;", countdown, "remaining.")
                return

            # read the session token from environment variable, or, if not set,
            # from a secret file
            token = os.environ.get("AOC_TOKEN", None)
            if not token:
                with open(os.path.expanduser("~/.aoc/token"), "r") as fh:
                    token = fh.read()

            token = token.strip()

            # fetch input from the server
            response = fetch(
                "https://adventofcode.com/{}/day/{}/input".format(
                    self.year, self.day
                ),
                headers={
                    "Cookie": f"session={token};",
                    "User-Agent": "python",
                },
            )

            # write the input data to the local cache
            fp.parent.mkdir(parents=True, exist_ok=True)
            with open(fp, "wb") as fh:
                fh.write(response)

        # now, read the input from the local cache
        with open(fp, "r") as fh:
            inp_s = fh.read()

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
