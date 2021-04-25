def largest_palindrome_product(n):

    up_digits = "1" + n * "0"
    low_digits = "1" + (n-1) * "0"

    num_up_digits = int(up_digits)
    num_low_digits = int(low_digits)

    x = range(num_low_digits, num_up_digits)
    largest_num = 0
    for i in x:
        for j in x:
            multi = i * j
            str_multi = str(multi)
            if str_multi == str_multi[::-1] and largest_num < multi:
                largest_num = multi

    return largest_num


print(largest_palindrome_product(3))
