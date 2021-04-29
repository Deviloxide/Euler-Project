def nth_prime_number(n):
    not_prime = set()
    prime = []

    while len(prime) < n:
        for i in range(2, n*100):
            if i in not_prime:
                continue

            for f in range(i*i, n*50, i):
                not_prime.add(f)

            prime.append(i)

    return prime[n - 1]


print(nth_prime_number(7))
