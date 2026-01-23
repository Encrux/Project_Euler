

def permutations(input: str) -> list[str]:

    res = []

    if len(input) == 1:
        return input

    if len(input) == 2:
        return [input[0] + input[1], input[1] + input[0]]

    for prefix in input:
        rest = input.replace(prefix, "")
        postfixes = permutations(rest)

        res.extend([prefix + postfix for postfix in postfixes])
        
    return res


perms = permutations("0123456789")

print(perms[999999])