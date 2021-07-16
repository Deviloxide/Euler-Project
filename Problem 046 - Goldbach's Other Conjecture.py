def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array


def prime_list(n):
    if n == 1 or n == 2:
        return 0

    sieve = [True] * n

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    primes = [2] + [i for i in range(3, n, 2) if sieve[i]]

    return primes


def disprove_goldbach(prime_limit, int_limit):
    bach_list = []
    composite_list = []

    for i in prime_list(prime_limit):
        for num in range(0, 100):
            ahh = i + 2 * (num ** 2)
            if ahh % 2 == 1:
                bach_list.append(ahh)

    bach_list = bubble_sort(list(set(bach_list)))

    for i in range(3, int_limit, 2):
        composite_list.append(i)

    for i in range(0, 10000):
        if composite_list[i] != bach_list[i]:
            return composite_list[i]


print(disprove_goldbach(10000, 10000))
