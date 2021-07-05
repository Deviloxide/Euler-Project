def distinct_powers(start, end):
    total_list = []

    for i in range(start, end + 1):
        for num in range(start, end + 1):
            total_list.append(num ** i)

    return set(total_list)


print(distinct_powers(2, 100))
