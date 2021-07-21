def number_spiral_diagonals(grid):
    num = 1
    grand_count = 0
    cycles = int(grid / 2)
    total = 1

    while grand_count < cycles:
        count = 0

        diff = (num ** .5) + 1

        while count < 4:
            num += diff
            total += num
            count += 1

        grand_count += 1

    return int(total)


print(number_spiral_diagonals(99))
