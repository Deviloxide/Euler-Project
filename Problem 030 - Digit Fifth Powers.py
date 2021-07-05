def digit_fifth_powers(expo, start, stop):
    new_list = []
    result = 0

    for num in range(start, stop + 1):
        total = 0
        for char in str(num):
            total += int(char) ** expo
        if num == total:
            new_list.append(num)

    for num in new_list:
        result += num

    return result


print(digit_fifth_powers(5, 2, 999999))
