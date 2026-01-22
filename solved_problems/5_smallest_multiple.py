# is potential multiple, i is potential divisor
def isMultiple(n, i):
    if n % i == 0:
        return True
    return False


def checkNum(num, n):
    for i in range(2, n):
        if not isMultiple(num, i):
            return False
    return True


# finds smallest number, which is divisble by all numbers between 1 and n
def findSmallestMultiple(n):
    currentNumber = 1
    while not checkNum(currentNumber, n):
        currentNumber += 1
    return currentNumber
