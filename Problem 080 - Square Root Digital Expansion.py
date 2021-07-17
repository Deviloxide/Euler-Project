import decimal

def square_root_expansion(start, end, prec):
    total = 0

    for num in range(start, end + 1):
        decimal.getcontext().prec = prec

        root = decimal.Decimal(num).sqrt()
        str_root = str(root)

        if len(str_root) > end:

            subtotal = int(str_root[0])

            for i in range(0, 99):
                subtotal += int(str_root[i + 2])

            total += subtotal

    return total


print(square_root_expansion(1, 100, 110))
