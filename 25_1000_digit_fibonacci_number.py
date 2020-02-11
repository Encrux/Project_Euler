import math
import functools as f
import itertools as it

cache = [0, 1]


def fibonacci(n):
    if len(cache) >= n + 1:
        return cache[n]
    cache.append(fibonacci(n - 1) + fibonacci(n - 2))
    return cache[n]


# upper bound of range might need some adjustment depending on how big length is
def first_of_len_n(length):
    return next(filter(lambda i: len(str(fibonacci(i))) >= length, [i for i in range(0, 10000)]))
