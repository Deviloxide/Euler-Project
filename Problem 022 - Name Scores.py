def name_scores(file):
    text_file = open(file, "r")

    lines = text_file.read().split(',')
    sorted_lines = sorted(lines)

    pos = 1
    total = 0

    for name in sorted_lines:
        name_total = 0

        for char in name[1:-1]:
            name_total += ord(char) - 64

        total += name_total * pos
        pos += 1

    return total


print(name_scores("Additional Files\p022_names.txt"))
