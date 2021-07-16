def tri_penta_hex(limit):
    hex_list = []
    final = []

    for i in range(1, limit):
        hex_list.append(i * (2 * i - 1))

    for num in hex_list:
        if ((1 + (1 + 24 * num) ** .5) / 6).is_integer() and (
                (-1 + (1 + 8 * num) ** .5) / 2).is_integer():
            final.append(num)

    return final


print(tri_penta_hex(99999))
