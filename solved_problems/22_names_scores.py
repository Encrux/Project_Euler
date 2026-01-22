import functools

name_file = open("p022_names.txt", 'r')
names = name_file.readlines()[0].replace("\"", "").split(",")
names.sort()

def name_score(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    for char in name:
        score += alphabet.index(char) + 1
    return score

def solve(names):
    return functools.reduce(lambda a, b: a + b, [name_score(name) * (names.index(name) + 1) for name in names])