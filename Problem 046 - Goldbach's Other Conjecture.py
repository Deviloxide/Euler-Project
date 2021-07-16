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

    lst = [2] + [i for i in range(3, n, 2) if sieve[i]]

    return lst


def disprove_goldbach(prime_limit, int_limit):
    low = float("inf")
    hmm = []
    maaa = []

    for i in prime_list(10000):
        for num in range(0, 100):
            ahh = i + 2 * (num ** 2)
            if ahh % 2 == 1:
                hmm.append(ahh)

    hmm = bubble_sort(list(set(hmm)))

    for i in range(3, 10000, 2):
        maaa.append(i)

    for i in range(0, 10000):
        if maaa[i] != hmm[i]:
            return maaa[i]


print(disprove_goldbach(10000, 10000))
