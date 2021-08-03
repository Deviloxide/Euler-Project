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


def circular_primes(limit):
    empty_list = []

    for num in range(0, limit):
        boo = True
        str_num = str(num)
        length = len(str_num)

        for i in range(0, length):
            boo *= is_prime(int(str_num[-i:] + str_num[:-i]))

        if boo:
            empty_list.append(num)

    return empty_list


print(circular_primes(1000000))
