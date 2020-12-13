#!/usr/bin/env python
# -*- coding: utf-8 -*-

identity = lambda s: s

# space/comma/line separated values/integers
ssv =  lambda s: [    v.strip()  for v in s.strip().split(" ")   ]
ssi =  lambda s: [int(v.strip()) for v in s.strip().split(" ")   ]
csv =  lambda s: [    v.strip()  for v in s.strip().split(",")   ]
csi =  lambda s: [int(v.strip()) for v in s.strip().split(",")   ]
lsv =  lambda s: [    l.strip()  for l in s.strip().split("\n")  ]
lsi =  lambda s: [int(l.strip()) for l in s.strip().split("\n")  ]
llsv = lambda s: [    l.strip()  for l in s.strip().split("\n\n")]

# grids
grid = lambda s: [list(l) for l in s.strip().split("\n")]

# characters/digit strings
characters = lambda s: [    c  for c in list(s.strip())]
digits     = lambda s: [int(d) for d in list(s.strip())] 