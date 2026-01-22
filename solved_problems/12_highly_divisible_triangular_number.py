import time
import math

def amount_of_factors(n):
    res = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            res += 1
    return res + 1


# function to count the divisors
def countDivisors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):

            # If divisors are equal,
            # count only one
            if (n / i == i):
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2
    return cnt


def get_sum_of_n(n):
    res = (n * (n + 1)) / 2
    return int(res)


def solve(n):
    i = 1

    start = time.time()
    while countDivisors(get_sum_of_n(i)) <= n:
        countDivisors(get_sum_of_n(i))
        i += 1

    end = time.time()
    print(end - start, 'seconds')
    return get_sum_of_n(i)