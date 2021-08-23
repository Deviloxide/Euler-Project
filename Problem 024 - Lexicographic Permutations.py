from itertools import permutations


def lex_permutations(start, end, pos):
    perm = permutations(range(start, end + 1))
    perm_list = []

    for item in list(perm):
        num = ""
        for char in item:
            num += str(char)
        perm_list.append(int(num))

    perm_list.sort()

    return perm_list[pos - 1]


print(lex_permutations(0, 9, 1000000))
