def sum_of_square(n):
    sum_sqr = "0"

    for i in range(1, n + 1):
        sum_sqr += "+" + str(i ** 2)

    sum_sqr_final = eval(sum_sqr)

    return int(sum_sqr_final)


def square_of_sum(n):
    sqr_sum = "0"

    for i in range(1, n + 1):
        sqr_sum += " + " + str(i)

    sqr_sum_solve = eval(sqr_sum)
    sqr_sum_final = sqr_sum_solve ** 2

    return sqr_sum_final


def sum_square_difference(n):
    diff = sum_of_square(n) - square_of_sum(n)
    diff_abs = abs(diff)

    return diff_abs


print(sum_of_square(100))

print(square_of_sum(100))

print(sum_square_difference(100))
