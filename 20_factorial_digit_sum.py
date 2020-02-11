import functools as f

def digit_sum(n):
    return f.reduce(lambda a, b: a + b, [int(d) for d in str(n)])
