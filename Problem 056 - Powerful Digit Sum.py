def pow_digit_sum(start, end):
    grand_total = 0

    for a in range(start, end + 1):
        for b in range(start, end + 1):
            total = 0
            num = a ** b
            for char in str(num):
                total += int(char)

            if total > grand_total:
                grand_total = total

    return grand_total


print(pow_digit_sum(1, 100))
