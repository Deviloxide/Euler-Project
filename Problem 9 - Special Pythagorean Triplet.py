def special_pythagorean_triplet_product(num):
    triplets = []

    for a in range(3, num):
        for b in range(a + 1, num - 1):
            cSquared = a ** 2 + b ** 2
            c = cSquared ** 0.5

            if a + b + c == num:
                triplets.append(([a, b, int(c)]))
                product = a * b * c

    return int(product)


def special_pythagorean_triplet(num):
    triplets = []

    for a in range(3, num):
        for b in range(a + 1, num - 1):
            cSquared = a ** 2 + b ** 2
            c = cSquared ** 0.5

            if a + b + c == num:
                triplets.append(a)
                triplets.append(b)
                triplets.append(int(c))

    return triplets


'''
def special_pythagorean_triplet_checker(limit):

    for i in range(1, limit + 1):
        if not special_pythagorean_triplet(i):
            print(i, "No")

        else:
            print(i, "Yes (" + str(special_pythagorean_triplet(i)[0]) + "^2 + " + str(
                special_pythagorean_triplet(i)[1]) + "^2 = " + str(special_pythagorean_triplet(i)[2]) + "^2)")
'''

print(special_pythagorean_triplet(444))

print(special_pythagorean_triplet_product(444))

# print(special_pythagorean_triplet_checker(444))
