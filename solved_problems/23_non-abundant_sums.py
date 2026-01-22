
def d(n) -> list[int]:
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i and n // i != n:
                divs.append(n // i)
    return sum(divs)


def abundants(n, m):
    abundants = []
    for i in range(n, m+1):
        if d(i) > i:
            abundants.append(i)
    
    return abundants


n = 28123

abundant_numbers = abundants(1, n)

numbers = list(range(0, n+1))

for a1 in abundant_numbers:
    for a2 in abundant_numbers:
        if a1 + a2 > n:
            continue
        numbers[a1+a2] = 0

print(sum(numbers))
