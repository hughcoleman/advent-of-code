#!/usr/bin/env python3
""" 2021/08: Seven Segment Search """

import sys

displays = [
   tuple(
       [ frozenset(digit) for digit in section.split() ]
           for section in display.split(" | ")
   )
       for display in sys.stdin.read().strip().split("\n")
]

print("Part 1:",
   sum(
       sum(len(digit) in {2, 3, 4, 7} for digit in display[1])
           for display in displays
   )
)

total = 0
for clues, challenge in displays:
   # This is a really clever way to pull the known numbers out; thanks
   # u/RodericTheRed!
   _1, _7, _4, *unknown, _8 = sorted(clues, key=len)

   _9 = next(d for d in unknown if len(_4 & d) == 4); unknown.remove(_9)
   _3 = next(d for d in unknown if len(d - _7) == 2); unknown.remove(_3)
   _2 = next(d for d in unknown if len(_9 & d) == 4); unknown.remove(_2)
   _0 = next(d for d in unknown if len(_1 & d) == 2); unknown.remove(_0)
   _6 = next(d for d in unknown if len(d     ) == 6); unknown.remove(_6)
   _5 = next(d for d in unknown                    ); unknown.remove(_5)

   # Now, it's easy to figure out what the four-digit "challenge" decodes to.
   digits = {
       v: str(i)
           for i, v in enumerate([_0, _1, _2, _3, _4, _5, _6, _7, _8, _9])
   }

   total = total + int(
       "".join(digits[digit] for digit in challenge)
   )

print("Part 2:", total)
