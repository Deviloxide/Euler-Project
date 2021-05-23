def summation_of_primes(n):
    if n == 1 or n == 2:
        return 0

    sieve = [True] * n

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    lst = [2] + [i for i in range(3, n, 2) if sieve[i]]
    summation = sum(lst)

    return summation

def multiplication_of_primes(n):
    if n == 1 or n == 2:
        return 0

    sieve = [True] * n

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    lst = [2] + [i for i in range(3, n, 2) if sieve[i]]
    multiplication = 1
    for x in lst:
        multiplication = multiplication * x

    return multiplication


print(summation_of_primes(2000000))

print(multiplication_of_primes(1000))
