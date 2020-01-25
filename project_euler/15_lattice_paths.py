import math

def lattice_path(n):
    return int(math.factorial(2*n) / math.factorial(n)**2)