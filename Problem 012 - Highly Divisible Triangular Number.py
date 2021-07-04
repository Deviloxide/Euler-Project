def number_of_factors(x):
    result = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1

    return len(result)


def triangle_number_generator(limit):
    added = 0
    ahh = []
    for i in range(0, limit + 1):
        added += i
        ahh.append(added)
    return ahh


# Faster for smaller limits, but can exceed memory with larger limits
def first_triangle_number_factor_generator(limit, length):
    tri_list = triangle_number_generator(limit)
    for i in tri_list:
        while number_of_factors(i) > length:
            return i


# Slower for smaller limits, but doesn't exceed memory as quickly with larger limits
def second_triangle_number_factor_generator(limit, length):
    for i in range(0, limit + 1):
        num = i * (i + 1) / 2
        if number_of_factors(num) > length:
            return int(num)


print(second_triangle_number_factor_generator(999999999999, 500))
