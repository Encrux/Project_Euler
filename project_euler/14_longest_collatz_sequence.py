import time


def collatz_step(n):
    if n % 2 == 0:
        return int(n/2)
    return int(3*n + 1)


def stepcount(n):
    next = n
    count = 0
    while next != 1:
        next = collatz_step(next)
        count += 1
    return count


def solve(n):
    start = time.time()

    stepcache = [0] * n
    max_step_count = 0
    max = 0

    for i in range(2, n):
        if stepcache[i] != 0:
            current_step_count = stepcache[i]
        else:
            current_step_count = stepcount(i)
            stepcache[i] = current_step_count

        if current_step_count > max_step_count:
            max = i
            max_step_count = current_step_count
    end = time.time()
    print(end - start, 'seconds')
    return max