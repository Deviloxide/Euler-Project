def digit_factorials(start, stop):
    new_list = []

    for num in range(start, stop):
        sup_total = 0
        for char in str(num):
            total = 1
            end = int(char)
            for i in range(1, end + 1):
                total *= i
            sup_total += total
        if sup_total == num:
            new_list.append(num)

    return new_list


print(digit_factorials(0, 100000))
