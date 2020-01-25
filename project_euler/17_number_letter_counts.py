import itertools as iter
import functools as f

m = [  [0, "zero"],
       [1, "one"],
       [2, "two"],
       [3, "three"],
       [4, "four"],
       [5, "five"],
       [6, "six"],
       [7, "seven"],
       [8, "eight"],
       [9, "nine"],
       [10, "ten"],
       [11, "eleven"],
       [12, "twelve"],
       [13, "thirteen"],
       [14, "fourteen"],
       [15, "fifteen"],
       [16, "sixteen"],
       [17, "seventeen"],
       [18, "eighteen"],
       [19, "nineteen"],
       [20, "twenty"],
       [30, "thirty"],
       [40, "forty"],
       [50, "fifty"],
       [60, "sixty"],
       [70, "seventy"],
       [80, "eighty"],
       [90, "ninety"],
       [100, "hundred"],
       [1000, "thousand"]]

def map_value(n):
    if n == 0:
        return ""
    return list(filter(lambda token: token[0] == n, m))[0][1]

def decompose(n):
    decomposed = list(iter.chain.from_iterable([d for d in str(n)]))
    while len(decomposed) < 4:
        decomposed.insert(0, 0)
    return [int(d) for d in decomposed]

def process_ones(n):
    return map_value(n)

def process_tens(n):
    if n < 20:
        return map_value(n)
    return map_value(decompose(n)[2]*10) + ' ' + process_ones(decompose(n)[3])

def process_hundreds(n):
    if decompose(n)[2] == 0 and decompose(n)[3] == 0:
        return map_value(decompose(n)[1]) + ' hundred'
    return map_value(decompose(n)[1]) + ' hundred and ' + process_tens(decompose(n)[2]*10 + decompose(n)[3])

#natural language num_to_str
def num_to_str(n):
    if n < 10:
        return process_ones(n)
    if n < 100:
        return process_tens(n)
    if n < 1000:
        return process_hundreds(n)
    return 'one thousand'

def num_letter_cnt(a, b):
    return len(list(iter.chain.from_iterable([num_str.replace(" ", "") for num_str in list(map(lambda n: num_to_str(n), range(a, b)))])))