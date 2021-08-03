def square_digit_chains(limit, choice):
    total = 0

    for num in range(1, limit):
        while num != 1:
            if num != 89:
                num_str = str(num)
                subtotal = 0

                for char in num_str:
                    subtotal += int(char) ** 2

                num = subtotal
            else:
                total += 1
                break

    if choice == 89:
        return total
    elif choice == 1:
        return limit - total - 1
    else:
        return 0


print(square_digit_chains(10000000, 89))
