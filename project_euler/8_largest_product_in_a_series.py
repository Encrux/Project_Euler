

def convert_to_list(n):
    return [int(x) for x in str(n)]


#i is the start index
#n is the amount of numbers to be multiplied with each other
def multiply_sequence(i, n, number):
    list = convert_to_list(number)
    product = 1
    for j in range(0, n):
        product *= list[i + j]
    return product



#n is the amount of adjacent digits to be checked
#n is the sequence of integers to be checked
def find_largest_product(n, number):
    list = convert_to_list(number)

    largest_product = 0
    for i in range(0, len(list) - 1):
        if i + n - 1 == len(list):
            print(i, n)
            break
        temp = multiply_sequence(i, n, number)
        if temp > largest_product:
            largest_product = temp

    return largest_product
