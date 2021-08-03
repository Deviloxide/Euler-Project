def closest_rectangle(target, limit):
    closest = target
    area = 0

    for width in range(1, limit):
        for height in range(1, limit):
            total = 0

            for a in range(1, width + 1):
                for b in range(1, height + 1):
                    total += ((width - a) + 1) * ((height - b) + 1)

            if abs(target - total) < closest:
                pair = [width, height]
                closest = abs(target - total)
                area = width * height

    return "Sides: {}".format(pair), "Off-Target by {}".format(closest), "Area: {}".format(area)


print(closest_rectangle(2000000, 100))
