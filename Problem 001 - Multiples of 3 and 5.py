def multiples_of_3_and_5(num, type):
    fizzy_list = []

    for i in range(3, num):
        if i % 3 == 0:
            fizzy_list.append(i)
        elif i % 5 == 0:
            fizzy_list.append(i)
        else:
            pass

    if type == "sum":
        answer = fizzy_list.sum()
    else:
        answer = fizzy_list

    return answer


print(multiples_of_3_and_5(1000, list))

print(multiples_of_3_and_5(1000, sum))

print(multiples_of_3_and_5(1000, "Thanh"))
