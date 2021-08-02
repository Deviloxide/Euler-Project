def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n ** .5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False

    return True


def number_spiral_diagonals(stop):
    prime_count = 0
    diff_list = []
    num = 1
    grand_count = 0
    diag = 1
    percent = 1
    side = 1

    while percent > stop:
        side += 2
        count = 0

        diff = (num ** .5) + 1

        while count < 4:
            num += diff
            count += 1
            diag += 1
            if is_prime(num):
                prime_count += 1
            diff_list.append(num)

        percent = prime_count / diag

        grand_count += 1

    return prime_count, diag, side


print(number_spiral_diagonals(.1))
