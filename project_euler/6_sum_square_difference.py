

def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i*i
    return sum

def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum*sum
