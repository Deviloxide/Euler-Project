def power_digit_count(power):
    count = 0

    for num in range(1,100):
        for exp in range(1,power):
            if len(str(num ** exp)) == exp:
                count += 1

    return count

print(power_digit_count(30))
