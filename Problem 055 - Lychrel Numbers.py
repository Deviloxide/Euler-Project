def lychrel_numbers(limit, length):
    ahh_list = []
    lychrel_list = []

    for nam in range(0, limit):
        num = nam
        count = 1

        while count < length:
            ahh_list.append(num)

            for_str = str(num)
            rev = str(num)[::-1]

            num_list = [int(i) for i in for_str]

            rev_strings = str(num)[::-1]
            rev_integer = int("".join(rev_strings))

            resulting_integer = num + rev_integer

            num = resulting_integer

            if count > 1 and rev == for_str:
                break

            count += 1

        if count > length - 3:
            lychrel_list.append(nam)

    return lychrel_list


print(len(lychrel_numbers(10000, 50)))
