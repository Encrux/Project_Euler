import math
import sympy



def isPalindrome(n):
    list = [int(x) for x in str(n)]

    for i in range(0, len(list)):
        if i < len(list) / 2:
            if list[i] != list[len(list) - 1 - i]:
                return False
    return True


palindromes = []

for i in range(100,999):
    for j in range(100,999):
        product = i*j
        if isPalindrome(product):
            palindromes.append(product)
