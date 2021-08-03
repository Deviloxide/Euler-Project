def largest_exponential(file):
    text_file = open(file, "r")

    lines = text_file.read().splitlines()

    greatest = 0
    count = 0

    split_list = []

    for elem in lines:
        seperated = elem.split(',')
        split_list.append(seperated)

    for i in range(0, len(split_list)):
        count += 1
        base = int(split_list[i][0])
        exp = float(split_list[i][1][:-len(split_list[i][1]) + 1] + "." + split_list[i][1][-len(split_list[i][1]) + 1:])
        result = base ** exp

        if result > greatest:
            greatest = result
            new_list = [base, exp, count]

    return new_list


print(largest_exponential("Additional Files/p099_base_exp.txt"))
