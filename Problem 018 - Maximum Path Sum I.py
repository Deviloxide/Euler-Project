def triangle_formatter(file):
    text_file = open(file, "r")

    lines = text_file.read().split("\n")

    triangle_sublists = []
    count = 0

    for i in lines:
        count += 1

        split_lines = i.split(" ")

        for missio in range(count):
            split_lines[missio] = int(split_lines[missio].lstrip("0"))

        triangle_sublists.append(split_lines)

    return triangle_sublists


def solution(tri):
    length = len(tri)

    for row in range(length - 2, -1, -1):
        for column in range(0, row + 1):
            tri[row][column] += max(tri[row + 1][column], tri[row + 1][column + 1])
    return tri[0][0]


triangle = triangle_formatter("Additional Files\p018_triangle.txt")

print(solution(triangle))
