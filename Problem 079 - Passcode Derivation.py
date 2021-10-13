def passcode_derivation(file):
    text_file = open(file, "r")
    lines = text_file.read().split()

    b0 = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []

    for line in lines:
        num_list = b0
        num_str = "0"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b1
        num_str = "1"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b2
        num_str = "2"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b3
        num_str = "3"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b4
        num_str = "4"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b5
        num_str = "5"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b6
        num_str = "6"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b7
        num_str = "7"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b8
        num_str = "8"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

        num_list = b9
        num_str = "9"

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

    super_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]

    count = 0
    order = {}

    for i_list in super_list:
        order[count] = len(set(i_list))
        count += 1

    return sorted(order, key=order.get)


print(passcode_derivation("Additional Files\p079_keylog.txt"))
