import argparse
import datetime
import os
import pathlib
import re
import subprocess
import sys
import time

ANSI_BG_RED = "\x1b[48;5;1m\x1b[38;5;16m"
ANSI_BG_YELLOW = "\x1b[48;5;3m\x1b[38;5;16m"
ANSI_BG_GREEN = "\x1b[48;5;2m\x1b[38;5;16m"
ANSI_BG_BLUE = "\x1b[48;5;4m\x1b[38;5;16m"
ANSI_CLEAR = "\x1b[0m"

PREFIX_ERR  = f"{ANSI_BG_RED} ERR! {ANSI_CLEAR}"
PREFIX_WARN = f"{ANSI_BG_YELLOW} WARN {ANSI_CLEAR}"
PREFIX_INFO = f"{ANSI_BG_BLUE} INFO {ANSI_CLEAR}"

try:
    import requests
except ModuleNotFoundError:
    print(PREFIX_ERR,
        f"Couldn't import module 'requests'.",
        f"(Have you activated the right virtualenv?)"
    )
    sys.exit(1)

parser = argparse.ArgumentParser(prog="santa",
    description="A little helper for solving Advent of Code puzzles.")
subparsers = parser.add_subparsers()

subparser_run = subparsers.add_parser("run", help="run a script")
subparser_run.add_argument("script", nargs="?", default=None)
subparser_run.add_argument("--invalidate-cached-input", default=False,
    action="store_true",
    help="invalidate the cached input; fetch again from server.")
subparser_run.add_argument("--test", default=False, action="store_true",
    help="pass '--test' to the script.")
subparser_run.add_argument("--timeout", type=int, default=10,
    help="kill script after (default: 10) seconds.")

def get_input(year, day, invalidate_cached_input=False):
    """ Fetch the input, downloading from the Advent of Code website if the
    input isn't in the cache.
    """

    fp = pathlib.Path(
        f".cache/{year:04}/{day:02}/input"
    ).resolve()

    if not fp.is_file() or invalidate_cached_input:
        # Wait until after midnight, eastern. We don't want to spam the
        # servers before the puzzle unlocks!
        waiting = 0
        while True:
            est = datetime.timezone(datetime.timedelta(hours=-5))
            delta = (
                datetime.datetime(year, 12, day, tzinfo=est) - datetime.datetime.now(tz=est)
            )

            if delta < datetime.timedelta(seconds=0):
                break

            # Determine the time remaining until unlock, and display a
            # formatted countdown timer.

            d = delta.days
            h = (delta.seconds // 3600) % 24
            m = (delta.seconds // 60) % 60
            s = (delta.seconds) % 60

            countdown = (
                (f"{d}d"    if d > 0 else "")
              + (f"{h:02}h" if h > 0 else "")
              + (f"{m:02}m" if m > 0 else "")
              + (f"{s:02}s")
            )

            if waiting > 0:
                print("\x1b[A", end="")
            print(PREFIX_WARN,
                f"Puzzle hasn't unlocked; {countdown} remaining."
            )

            waiting = waiting + 1
            time.sleep(1)

        print(PREFIX_INFO, "Downloading input from adventofcode.com...")

        # Read the session token from an environment variable, or, from
        # a secret file.
        _token = os.environ.get("AOC_TOKEN")
        if not _token:
            token_fps = [
                pathlib.Path(".AOC_TOKEN"),
                pathlib.Path(".TOKEN"),
                pathlib.Path("~/.AOC_TOKEN").expanduser(),
                pathlib.Path("~/.TOKEN").expanduser()
            ]
            for token_fp in token_fps:
                if not token_fp.is_file():
                    continue

                print(PREFIX_INFO, f"Reading token from '{token_fp}'.")

                with token_fp.open(mode="r") as fh:
                    _token = fh.read()

                break
            else:
                print(PREFIX_ERR, "Couldn't locate token.")
                sys.exit(1)

        _token = _token.strip()

        # Fetch the input, using the token.
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            headers={
                "Cookie": f"session={_token};",
                "User-Agent": "github.com/hughcoleman/advent-of-code",
            }
        )

        assert response.status_code == 200
        _token = None # just a precaution

        # Cache the input.
        fp.parent.mkdir(parents=True, exist_ok=True)
        with fp.open(mode="wb") as fh:
            fh.write(response.content)

    with fp.open(mode="rb") as fh:
        inp_s = fh.read()

    return inp_s

def run(fp, invalidate_cached_input=False, test=False, timeout=10):
    """ Run script `fp`. """

    # Determine the year and day associated with this script. This information
    # is (should be) embedded in the """ docstring """ of the script, on line
    # 2.
    with fp.open(mode="r") as fh:
        fh.readline() # ignore the shebang; the docstring is on line 2.
        ln = fh.readline().strip()

        try:
            year, day, name = re.fullmatch(
                r"\"\"\"\s+\b(\d{4})\b.*\b(\d{1,2})\b[^\s]*\s*(.*)\s+\"\"\"",
                ln
            ).groups()
            if len(name) <= 0:
                name = None

        except:
            # If we can't extract the year and day from the docstring, attempt
            # to infer the year and day from the path to `fp`.
            year, day = re.fullmatch(
                r".*[aA].*[oO].*[cC].*\b(\d\d\d\d)\b.*\b(\d\d)\b.*",
                str(
                    fp.resolve()
                )
            ).groups()
            name = None

            print(PREFIX_WARN,
                f"Inferred year \"{year}\" and day \"{day}\" from path.",
                f"Is this what you want?"
            )

        finally:
            year = int(year); assert 2015 <= year
            day  = int(day ); assert 1 <= day <= 25

    # Print a little header.
    print(
        "---",
        f"{year:04}/{day:02}{f': {name}' if name else ''}",
        f"({fp.relative_to(pathlib.Path.cwd())})",
        "---"
    )

    # Run the script.
    if sys.stdin.isatty():
        inp_s = get_input(year, day, invalidate_cached_input)
    else:
        print(PREFIX_WARN,
            "Standard input isn't interactive; assuming input data is piped."
        )
        inp_s = sys.stdin.read().encode()

    try:
        process = subprocess.run(
            # TODO: Properly "activate" the virtualenv.
            [
                "./.venv/bin/python3", str(fp), "--test" if test else ""
            ],
            input=inp_s,
            stdout=sys.stdout, # we need to see the output!
            timeout=timeout
        )
    except subprocess.TimeoutExpired:
        print(PREFIX_ERR, f"Timed out! (timeout was {args.timeout}s)")

    return

if __name__ == "__main__":
    args = parser.parse_args()

    # Locate the script.
    if args.script is None:
        run(
            pathlib.Path.cwd() / "main.py",
            invalidate_cached_input=args.invalidate_cached_input,
            test=args.test,
            timeout=args.timeout
        )

    else:
        for p in sorted(pathlib.Path.cwd().glob(f"{args.script}*")):
            if p.is_dir():
                # Run all scripts in the directory.
                for fp in sorted(p.glob("*.py")):
                    run(
                        fp,
                        invalidate_cached_input=args.invalidate_cached_input,
                        test=args.test,
                        timeout=args.timeout
                    )
            elif p.is_file():
                # Run script.
                run(
                    p,
                    invalidate_cached_input=args.invalidate_cached_input,
                    test=args.test,
                    timeout=args.timeout
                )
