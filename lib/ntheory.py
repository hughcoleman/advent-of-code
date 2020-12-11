#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def _gcd(a, b):
    return math.gcd(a, b)

def _lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def gcd(ns):
    while len(ns) > 1:
        a, b = ns.pop(), ns.pop()
        while b:
            a, b = b, a%b
        ns.append(a)
    return ns[0]

def lcm(ns):
    while len(ns) > 1:
        a, b = ns.pop(), ns.pop()
        ns.append(_lcm(a, b))
    return ns[0]

def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n//10)

def factor(n):
    factors = {}
    
    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n = n // i
            if i not in factors.keys():
                factors[i] = 0
            factors[i] = factors[i] + 1

    if n > 1:
        if n not in factors.keys():
            factors[n] = 0
        factors[n] = factors[n] + 1
    
    return factors

triangular = lambda n: n in [0, 1] or any(i*(i+1)/2 == n for i in range(n))
fibonacci  = lambda n: square(5*n*n + 4) or square(5*n*n - 4)
square     = lambda n: int(math.sqrt(n))**2 == n
sphenic    = lambda n: list(factor(n).values()) == [1, 1, 1]
achilles   = lambda n: n >= 2 and all(e >= 2 for e in factor(n).values()) and \
                       gcd(list(factor(n).values())) == 1
prime      = lambda n: n not in [0, 1] and all(n % i > 0 for i in range(2, n-1))
emirp      = lambda n: prime(n) and prime(int(str(n)[::-1]))