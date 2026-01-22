import itertools
import functools as f

bigboi = 2**1000
print(bigboi)

def sum(bigboi):
    return f.reduce(lambda a,b: a+b, [int(d) for d in str(bigboi)])