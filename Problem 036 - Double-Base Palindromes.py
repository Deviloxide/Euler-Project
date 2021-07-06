def double_base_palindromes_sum(end):
    total = 0
    b10_pal_list = []
    total_pal_list = []

    for num in range(0, end):
        str_num = str(num)
        rev = str(num)[::-1]

        if rev == str_num:
            b10_pal_list.append(num)

    for pal in b10_pal_list:
        binary = bin(pal)[2:]
        rev = binary[::-1]

        if rev == binary:
            total_pal_list.append(pal)

    for fin_pal in total_pal_list:
        total += fin_pal

    return total


print(double_base_palindromes_sum(1000000))
