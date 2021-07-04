def factorial_digit_sum(num):
    fact_total = 1

    while num != 1:
        fact_total *= num
        num -= 1

    fact_total_str = str(fact_total)
    total_list = []
    sum_total = 0

    for i in fact_total_str:
        total_list.append(i)

    for i in total_list:
        sum_total += int(i)

    return sum_total


print(factorial_digit_sum(100))
