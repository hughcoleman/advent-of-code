#!/usr/bin/env python
# -*- coding: utf-8 -*-

identity = lambda s: s
csv =  lambda s: [    v.strip()  for v in s.split(",")    if v.strip()]
cai =  lambda s: [int(v.strip()) for v in s.split(",")    if v.strip()]
lsv =  lambda s: [    l.strip()  for l in s.split("\n")   if l.strip()]
llsv = lambda s: [    l.strip()  for l in s.split("\n\n") if l.strip()]
lsi =  lambda s: [int(l.strip()) for l in s.split("\n")   if l.strip()]
ssv =  lambda s: [    v.strip()  for v in s.split(" ")    if v.strip()]
ssi =  lambda s: [int(v.strip()) for v in s.split(" ")    if v.strip()]
grid = lambda s: [list(l)        for l in s.split("\n")   if l.strip()]