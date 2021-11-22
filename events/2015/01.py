from lib import *
problem = aoc.Problem("2015/01: Not Quite Lisp")
problem.preprocessor = ppr.I

@problem.solver(part=1)
def p1(instructions):
    return instructions.count("(") - instructions.count(")")

@problem.solver(part=2)
def p2(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
        floor = floor + {"(": 1, ")": -1}[instruction]

        if floor < 0:
            # The instructions are indexed from 1.
            return i + 1


if __name__ == "__main__":
    problem.solve()
