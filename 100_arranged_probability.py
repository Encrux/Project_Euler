import math

def squares():
    i = 1
    while True:
        yield i * i
        i += 1
