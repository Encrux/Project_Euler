from sympy import sieve
import math


def sum_of_primes(n):
    i = 1
    res = 0
    while(sieve[i] <= n):
        res += sieve[i]
        i += 1
    return res
