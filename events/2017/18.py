#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import *
problem = aoc.Problem("2017/18: Duet")
problem.preprocessor = lambda program: [
    (instruction.split(" ")[0], instruction.split(" ", 1)[1].split(" "))
    for instruction in program.strip().split("\n")
]


import collections as cl


class Computer:
    """ Simulate a single Duet computer. """

    def run(self):
        # run the virtual machine, until the instruction pointer leaves the
        # bounds of addressable memory
        while 0 <= self.ip < len(self.rom):
            op, args = self.rom[self.ip]

            offset = 1
            if op == "snd":
                self.snd(self.get(args[0]))
            elif op == "set":
                self.registers[args[0]] = self.get(args[1])
            elif op == "add":
                self.registers[args[0]] += self.get(args[1])
            elif op == "mul":
                self.registers[args[0]] *= self.get(args[1])
            elif op == "mod":
                self.registers[args[0]] %= self.get(args[1])
            elif op == "rcv":
                if len(self.inq) <= 0:
                    return
                self.registers[args[0]] = self.inq.pop(0)
            elif op == "jgz":
                if self.get(args[0]) > 0:
                    offset = self.get(args[1])

            self.ip = self.ip + offset

    def get(self, r):
        if r.isalpha():
            return self.registers[r]
        return int(r)

    def __init__(self, instructions, override={}):
        self.rom = instructions
        self.ip = 0

        # registers are unknown (but known to be referred to using
        # one-character strings.
        self.registers = cl.defaultdict(lambda: 0)
        for register, value in override.items():
            self.registers[register] = value

        # input queue
        self.inq = []


@problem.solver(part=1)
def p1(instructions):
    computer = Computer(instructions)

    output = []
    def snd(frequency):
        output.append(frequency)

    # bind to the send function of the Computer
    computer.snd = snd
    computer.run()

    return output[-1]


@problem.solver(part=2)
def p2(instructions):
    c1 = Computer(instructions, override={"p": 0})
    c2 = Computer(instructions, override={"p": 1})

    def c1_snd(x):
        c2.inq.append(x)

    s = 0
    def c2_snd(x):
        nonlocal s
        c1.inq.append(x)
        s = s + 1

    c1.snd = c1_snd
    c2.snd = c2_snd

    while True:
        # run computer 1 until failure, then computer 2 until failure
        c1.run()
        c2.run()

        # if both input queues are empty, then the program has deadlocked
        if len(c1.inq) <= 0 and len(c2.inq) <= 0:
            break

    return s


if __name__ == "__main__":
    problem.solve()
