def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

def combinatoric_selections(limit):
    count = 0

    for n in range(1, limit + 1):
        for r in range(1, n):
            if factorial(n) / (factorial(r) * (factorial(n - r))) > 1000000:
                count += 1

    return count

print(combinatoric_selections(100))
