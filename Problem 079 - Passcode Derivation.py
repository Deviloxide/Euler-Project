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

    bool_0 = [False]
    bool_1 = [False]
    bool_2 = [False]
    bool_3 = [False]
    bool_4 = [False]
    bool_5 = [False]
    bool_6 = [False]
    bool_7 = [False]
    bool_8 = [False]
    bool_9 = [False]

    for line in lines:
        num_list = b0
        num_str = "0"
        booly = bool_0

        if num_str in line:
            booly = [True]

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
        booly = bool_1

        if num_str in line:
            booly = [True]

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
        booly = bool_2

        if num_str in line:
            booly = [True]

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
        booly = bool_3

        if num_str in line:
            booly = [True]

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
        booly = bool_4

        if num_str in line:
            booly = [True]

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
        booly = bool_5

        if num_str in line:
            booly = [True]

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
        booly = bool_6

        if num_str in line:
            booly = [True]

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
        booly = bool_7

        if num_str in line:
            booly = [True]

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
        booly = bool_8

        if num_str in line:
            booly = [True]

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
        booly = bool_9

        if num_str == line[0] or num_str == line[1] or num_str == line[2]:
            booly = [True]

        if line[2] == num_str:
            if line[0] not in num_list:
                num_list.append(line[0])
            if line[1] not in num_list:
                num_list.append(line[1])
        elif line[1] == num_str:
            if line[1] not in num_list:
                num_list.append(line[0])

    super_bool = [bool_0, bool_1, bool_2, bool_3, bool_4, bool_5, bool_6, bool_7, bool_8, bool_9]
    super_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]
    mega_list = []

    count = 0
    order = {}

    for i_list in super_list:
        order[count] = len(set(i_list))
        count += 1

    return sorted(order, key=order.get)

print(passcode_derivation("Additional Files\p079_keylog.txt"))

#for i in range(0,10):
#    if super_bool[i][0] == True:
#        print(super_list)
#

