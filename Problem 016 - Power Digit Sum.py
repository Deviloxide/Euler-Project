def power_digit_sum(base, expo):
    num = base ** expo
    num_str = str(num)
    num_list = []
    total = 0

    for i in num_str:
        num_list.append(i)

    for i in num_list:
        total += int(i)

    return total


print(power_digit_sum(2, 1000))
