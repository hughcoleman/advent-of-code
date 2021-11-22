from lib import *
problem = aoc.Problem("2015/19: Medicine for Rudolph")
problem.preprocessor = lambda inp: (
    # Extract all possible reactions...
    [
        (reaction.split(" => ")[0], split(reaction.split(" => ")[1]))
            for reaction in inp.strip().split("\n\n")[0].split("\n")
    ],
    # ...and the formula.
    split(inp.strip().split("\n\n")[1]),
)

def split(compound):
    terms = []

    term = ""
    for c in compound:
        if c.isupper() and len(term) > 0:
            terms.append(term)
            term = ""
        term = term + c

    terms.append(term)
    return terms

@problem.solver(part=1)
def p1(inp):
    reactions, medicine = inp

    compounds = set()
    for i, element in enumerate(medicine):
        for reactant, products in reactions:
            if reactant != element:
                continue

            compounds.add(tuple(medicine[:i] + products + medicine[i + 1 :]))

    return len(compounds)

@problem.solver(part=2)
def p2(inp):
    reactions, medicine = inp

    medicine = "".join(medicine)

    # Because of the way that the input is crafted, we can greedily just
    # reverse any reaction we see until we are left with one election.
    #
    # Personally, I'm not a fan of this solution; I'd much rather have written
    # a clever algorithm that carefully considered which reactions to do... but
    # I'll live with this.
    n = 0
    while medicine != "e":
        for reactant, products in reactions:
            if "".join(products) in medicine:
                medicine = medicine.replace("".join(products), reactant, 1)
                n = n + 1

    return n


if __name__ == "__main__":
    problem.solve()
