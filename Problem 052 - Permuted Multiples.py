def permutated_multiples(limit):
    for num in range(1,limit):
        value = sorted(str(num))
        t2 = sorted(str(num * 2))
        t3 = sorted(str(num * 3))
        t4 = sorted(str(num * 4))
        t5 = sorted(str(num * 5))
        t6 = sorted(str(num * 6))

        if value == t2 and value == t3 and value == t3 and value == t4 and value == t5 and value == t6:
            return num, num * 2, num * 3, num * 4, num * 5, num * 6

print(permutated_multiples(999999))
