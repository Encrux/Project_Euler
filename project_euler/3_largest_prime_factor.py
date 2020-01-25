import math
import numpy as np
import sympy
from sympy import sieve


def isPrime(n):
    if n == 1:
        return False

    for i in range(2, n - 1):
        if (n % i == 0):
            return False
    return True


def largestprimefactor(n):
    for i in range(2, n + 1):
        if isPrime(i):
            if i == n:
                return i

            if n % i == 0:
                return largestprimefactor(round(n / i))