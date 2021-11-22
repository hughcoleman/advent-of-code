from lib import *
problem = aoc.Problem("2015/20: Infinite Elves and Infinite Houses")
problem.preprocessor = int

import math
import itertools

def robin(N):
    # Consider the inequality;
    #
    #     sum_of_divisors(n) < e^EULER_MASCHERONI*n*ln(ln(n))
    #
    # Robin's theorem states that truth of this inequality for all n >= 5040 is
    # equivalent to the Riemann Hypothesis.

    return (
        math.exp(0.57721566490153286060651209008240243104215933593992)
        * N
        * math.log(math.log(N))
    )

# Originally, this function implemented a naive brute-force algorithm that
# looped n from n=1 to infinity, and computed the sum of the factors of each n.
#
# After peeking at the Reddit thread, I discovered Robin's inequality, which
# allows us to implement this a lot more efficiently.
@problem.solver(part=1)
def p1(threshold):
    # Perform a binary search to find the smallest n such that
    # robin(n) > N // 10.
    lo, hi = 5040, threshold // 10
    while lo != hi:
        mid = (lo + hi) // 2

        f = robin(mid)
        if f < threshold // 10:
            lo = mid + 1
        elif f > threshold // 10:
            hi = mid

    # Find house in the range [lo, lo*1.1) whose sum-of-factors exceeds the
    # desired number
    while True:
        lo, hi = hi, int(lo * 1.1)

        visits = [0] * (hi - lo)
        for elf in range(hi, 1, -1):
            # Determine smallest multiple of elf that is within the range
            # [lo, lo*1.1)
            start = elf * math.ceil(lo / elf) - lo
            for j in range(start, hi - lo, elf):
                visits[j] += elf

        for i, s in enumerate(visits):
            if s > threshold // 10:
                return lo + i

# Originally, this function too implemented a naive brute-force algorithm
# similar to the one described above.
#
# After peeking at the Reddit thread, I realized that the more efficient method
# would be to generate integers with large numbers of factors (ie. lots of
# prime factors, and large exponents on each of the prime factors) and check
# only those.

PRIMES = [2, 3, 5, 7, 11]
EXPONENTS = [13, 5, 4, 4, 3]  # Largest "reasonable" value of an exponent for
                              # the corresponding prime base.

def evaluate(exponents):
    product = 1
    for base, exponent in zip(PRIMES, exponents):
        product = product * pow(base, exponent)
    return product

@problem.solver(part=2)
def p2(threshold):
    lowest = math.inf
    for candidate in itertools.product(*[range(i) for i in EXPONENTS]):
        house = evaluate(candidate)

        # Compute the number of presents delivered to this house - we already
        # know the prime factorization of house, so this is easy.
        presents = 0
        for factor in itertools.product(
            *[range(prime + 1) for prime in candidate]
        ):
            factor = evaluate(factor)
            if house // factor <= 50:  # Elves only deliver to first 50 houses.
                presents = presents + factor

        if presents * 11 >= threshold:
            lowest = min(lowest, house)

    return lowest


if __name__ == "__main__":
    problem.solve()
