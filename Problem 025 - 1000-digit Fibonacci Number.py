def fibonacci_number_digits(num):
    index = 1

    x = 0
    y = 1
    z = 0

    if num == 1:
        return 1, 1
    else:
        while len(str(z)) < num:
            z = x + y
            x = y
            y = z
            index += 1

        return index, z


print(fibonacci_number_digits(1000))
