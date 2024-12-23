#!/usr/bin/env python3
""" 2024/05: Print Queue """

import functools as ft
import sys

ordering_rules, updates = sys.stdin.read().strip().split("\n\n")
ordering_rules = [
    tuple(map(int, ordering_rule.split("|")))
        for ordering_rule in ordering_rules.split("\n")
]
updates = [
    list(map(int, update.split(",")))
        for update in updates.split("\n")
]

def cmp(x1, x2):
    return -1 if (x1, x2) in ordering_rules else 1

print("Part 1:",
    sum(
        update[len(update) // 2]
            for update in updates
            if update == sorted(update, key=ft.cmp_to_key(cmp))
    )
)
print("Part 2:",
    sum(
        sorted(update, key=ft.cmp_to_key(cmp))[len(update) // 2]
            for update in updates
            if update != sorted(update, key=ft.cmp_to_key(cmp))
    )
)
