def champernowne_constant(limit):
    count = 1
    champ_cons = "."

    while len(champ_cons) <= limit:
        champ_cons += str(count)
        count += 1

    return champ_cons


constant = champernowne_constant(1000000)

print(int(constant[1]) * int(constant[10]) * int(constant[100]) * int(constant[1000]) * int(constant[10000]) * int(
    constant[100000]) * int(constant[1000000]))
