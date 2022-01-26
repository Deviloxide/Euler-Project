def proper_factors(x):
    result = []
    i = 1

    while i * i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1

    result.pop(1)

    return result


def proper_enumerator(num):
    count = 0

    for i in proper_factors(num):
        count += i

    return count


def nonabundant_sums(limit):
    abundants = []

    sums = []

    for num in range(12, limit + 1):
        if proper_enumerator(num) > num:
            abundants.append(num)

    for a in range(0, (len(abundants))):
        for b in range(a, (len(abundants))):
            sums.append(abundants[a] + abundants[b])

    count = 0

    sums = set(sums)

    for test in range(1, limit + 1):
        if test in sums:
            pass
        else:
            count += test

    return count


print(nonabundant_sums(28123))
