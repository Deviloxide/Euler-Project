def triangle_word_scores(file):
    text_file = open(file, "r")

    lines = text_file.read().split(',')
    sorted_lines = sorted(lines)

    total = 0

    for name in sorted_lines:
        word_total = 0

        for char in name[1:-1]:
            word_total += ord(char) - 64

        result = (((8 * word_total + 1) ** .5) - 1) / 2

        if result.is_integer():
            total += 1

    return total


print(triangle_word_scores("Additional Files/p042_words.txt"))
