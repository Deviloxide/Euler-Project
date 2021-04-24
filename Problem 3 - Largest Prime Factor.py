def largest_prime_factor(n):
    prime_factor = 1
    i = 2

    if n == 0:
        return "0 has no greatest prime factor."

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor

print(largest_prime_factor(60085546657761475143))