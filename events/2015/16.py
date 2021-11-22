from lib import *
problem = aoc.Problem("2015/16: Aunt Sue")
problem.preprocessor = lambda aunts: {
    # Extract aunt number.
    int(aunt[aunt.index(" ") + 1 : aunt.index(":")]): {
        compound.split(": ")[0]: int(compound.split(": ")[1])
            for compound in aunt.split(": ", 1)[1].split(", ")
    }
        for aunt in aunts.strip().split("\n")
}

READINGS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

@problem.solver(part=1)
def naive(aunts):
    for n, aunt in aunts.items():
        for compound, amount in aunt.items():
            if READINGS[compound] != amount:
                break
        else:
            return n

    raise RuntimeError("Unsolvable! No matching aunts found.")

COMPARATORS = {
    # Conditions are inverted, because we're "accepting the negative."
    "cats": lambda e, a: e >= a,
    "trees": lambda e, a: e >= a,
    "pomeranians": lambda e, a: e <= a,
    "goldfish": lambda e, a: e <= a,
}

@problem.solver(part=2)
def actual(aunts):
    for n, aunt in aunts.items():
        for compound, amount in aunt.items():
            comparator = COMPARATORS.get(compound, lambda e, a: e != a)

            if comparator(READINGS[compound], amount):
                break
        else:
            return n

    raise RuntimeError("Unsolvable! No matching aunts found.")


if __name__ == "__main__":
    problem.solve()
