import itertools


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n ** .5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False

    return True


def largest_pandigital(digits):
    permutations = itertools.permutations(digits)

    for i in list(permutations)[::-1]:
        num = int(''.join(map(str, i)))

        if is_prime(num):
            return num


print(largest_pandigital("1234567"))
