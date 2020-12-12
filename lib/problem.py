#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import datetime as dt
import pathlib
import traceback

from .net import fetch

class Problem:

    def __init__(self, *args, **kwargs):
        
        if (match := re.fullmatch(
            re.compile(r"(?P<year>[0-9]{4})\/(?P<day>0?[1-9]|1[0-9]|2[0-5])\: " + 
                       r"(?P<name>[\w ]*)"), 
            "".join(args)
        )):
            self.year = int(match.group("year"))
            self.day  = int(match.group("day"))
            self.name = str(match.group("name"))
        else:
            raise ValueError(f"could not parse arguments to Problem constructor.")

        self.preprocessor = lambda x: x
        self.fns = {}

    def solver(self, part="both"):
        def register(fn):
            # register the solver function in the instance dictionary variable 
            # `self.fns`.
            self.fns[part] = fn
            return fn

        return register

    def solve(self):
        # print a neat little header for the problem
        print(f"--- Day {self.day}: {self.name} ---")

        # setup the path to the local cache
        fp = pathlib.Path(f"~/.cache/adventofcode.com/{str(self.year)}/" + 
                          f"{str(self.day).zfill(2)}/input").expanduser()

        # if the input isn't cached, download from the adventofcode.com server
        # and cache
        if not fp.exists():
            print("No cached input; downloading from " + 
                    "\u001b[4madventofcode.com\u001b[0m...")

            # first check the current time to ensure that it is past midnight 
            # est before fetching problem input from server
            est = dt.timezone(dt.timedelta(hours=-5))
            delta = dt.datetime(self.year, 12, self.day, tzinfo=est) -\
                    dt.datetime.now(tz=est)
            
            if dt.timedelta(seconds=0) < delta <= dt.timedelta(seconds=15):
                print("Less than fifteen seconds remaining, will sleep...")
                time.sleep(delta.seconds + 1)

            elif delta > dt.timedelta(seconds=0):
                # determine time remaining until unlock and display a formatted
                # countdown timer
                d =  delta.days
                h = (delta.seconds // 3600) % 24
                m = (delta.seconds // 60  ) % 60
                s = (delta.seconds        ) % 60

                countdown = (f"{str(d).zfill(2)}d" if d > 0 else "") +\
                            (f"{str(h).zfill(2)}h" if h > 0 else "") +\
                            (f"{str(m).zfill(2)}m" if m > 0 else "") +\
                            (f"{str(s).zfill(2)}s")

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
                "https://adventofcode.com/{}/day/{}/input".format(self.year, self.day),
                headers={
                    "Cookie": f"session={token};",
                    "User-Agent": "python"
                }
            )

            # write the input data to the local cache
            fp.parent.mkdir(parents=True, exist_ok=True)
            with open(fp, "wb") as fh:
                fh.write(response)

        # now, read the input from the local cache
        with open(fp, "r") as fh:
            inp = fh.read()

        # apply the preprocessor
        inp = self.preprocessor(inp)
        
        for part, fn in self.fns.items():
            # run the solver and time the runtime
            start = time.perf_counter()
            try:
                out = fn(inp)
            except Exception as err:
                traceback.print_tb(err.__traceback__)
                out = "FAIL"
            finally:
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
