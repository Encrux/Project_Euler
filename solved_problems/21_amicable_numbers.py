

def d(n) -> list[int]:
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i and n // i != n:
                divs.append(n // i)
    return sum(divs)



divs_dict = {}

# calculate all divs
for i in range(1, 10000):
    divs_dict[i] = d(i)

amicable_numbers = []
for n, dn in divs_dict.items():
    if dn in divs_dict and divs_dict[dn] == n and n != dn:
        amicable_numbers.append(n)


print(sum(amicable_numbers))