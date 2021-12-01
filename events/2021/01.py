from lib import *
problem = aoc.Problem("2021/01: Sonar Sweep")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def p1(ns):
    return sum(
        (b > a) for a, b in zip(ns, ns[1:])
    )

@problem.solver(part=2)
def p2(ns):
    return sum(
        sum(ns[i + 1:i + 4]) > sum(ns[i:i + 3])
            for i in range(len(ns) - 3)
    )


if __name__ == "__main__":
    problem.solve()
