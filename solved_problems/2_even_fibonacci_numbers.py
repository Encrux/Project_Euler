import numpy as np
import matplotlib as math
import pandas as pandas


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return fib(n-1) + fib(n-2)


sum = 0
i = 1
while fib(i) <= 4000000:
    i += 1
    if fib(i) % 2 == 0:
        sum += fib(i)

print(sum)