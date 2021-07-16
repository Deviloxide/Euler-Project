def pentagon_sub_plus(limit):
    penta_list = []

    for i in range(1, limit):
        penta_list.append(i * (3 * i - 1) / 2)

    for a in penta_list:
        for b in penta_list:
            if ((1 + (1 + 24 * (a + b)) ** .5) / 6).is_integer() and \
                    abs(((1 + (1 + 24 * (a - b)) ** .5) / 6)).is_integer():
                return [int(a) - int(b)]


print(pentagon_sub_plus(3162))
