def digit_factorials(limit):
    new_list = []
    ahh = {"1": 1, "2": 2, "3": 6, "4": 24, "5": 120, "6": 720, "7": 5040, "8": 40320, "9": 362880, "0": 1}

    for num in range(0, limit):
        grand_total = 0

        for char in str(num):
            grand_total += ahh[char]

        if grand_total == num:
            new_list.append(num)

    return new_list


total = 0

for i in digit_factorials(100000)[2:]:
    total += i

print(total)
