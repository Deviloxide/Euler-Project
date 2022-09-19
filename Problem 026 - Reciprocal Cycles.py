def reciprocal_cycles(numerator, start, limit, print_nums):
    highest = 0
    num = numerator

    if not print_nums:
        for denominator in range(start, limit):
            repeat_string = ""
            checked_values = []
            digits = 0
            numerator = num

            while True:
                n = numerator // denominator
                value = (numerator, denominator)

                if value in checked_values:
                    highest = max(highest, digits)
                    break

                checked_values.append(value)
                repeat_string += str(n)

                numerator = numerator % denominator * 10

                digits += 1
    else:
        for denominator in range(start, limit):
            repeat_string = ""
            checked_values = []
            digits = 0
            numerator = num

            while True:
                n = numerator // denominator
                value = (numerator, denominator)

                if value in checked_values:
                    if repeat_string[-1] == "0":
                        print(numerator, "/", denominator, "=", repeat_string[0] + "." + repeat_string[1:-1])
                    else:
                        print(numerator, "/", denominator, "=", repeat_string[0] + "." + repeat_string[1:] + "(r)")
                        highest = max(highest, digits)
                    break

                checked_values.append(value)
                repeat_string += str(n)

                numerator = numerator % denominator * 10

                digits += 1

    return highest


print(reciprocal_cycles(1, 2, 1000, False))
