def prime_set(n):
    if n == 1 or n == 2:
        return 0

    sieve = [True] * n

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    primes = [2] + [i for i in range(3, n, 2) if sieve[i]]

    return set(primes)


def truncatable_primes(primes):
    trunc_primes = []

    for num in primes:
        count = 0
        num_str = str(num)
        length = len(num_str)

        for a in range(length):
            if int(num_str[a:]) in primes:
                count += 1
            else:
                break
        for b in range(length - 1):
            if int(num_str[:b + 1]) in primes:
                count += 1
            else:
                break
        if count == length * 2 - 1:
            trunc_primes.append(num)

    return trunc_primes


n_list = prime_set(999999)

print(sum(truncatable_primes(n_list)) - sum([2, 3, 5, 7]))
