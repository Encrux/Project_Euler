

def is_pythagorean_triplet(a,b,c):
    if a*a + b*b == c*c:
        return True
    return False


def find_triplets_of_sum(n):
    list = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i + j + k == n:
                    list.append([i, j, k])
                    list.append([i, k, j])
                    list.append([j, k, i])
                    list.append([i, j, k])
                    list.append([k, j, i])
                    list.append([k, i, j])
                    print(i)
    return list


def check_for_pythagorean_triplet(list):
    for x in list:
        if is_pythagorean_triplet(x[0], x[1], x[2]):
            return x
    return -1