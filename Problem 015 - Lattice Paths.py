def lattice_path_possibilities(num):
    num_2 = 2 * num
    fact_total = 1
    fact_total_2 = 1

    while num != 1:
        fact_total *= num
        num -= 1

    while num_2 != 1:
        fact_total_2 *= num_2
        num_2 -= 1

    return int(fact_total_2 / (fact_total ** 2))


print(lattice_path_possibilities(20))
