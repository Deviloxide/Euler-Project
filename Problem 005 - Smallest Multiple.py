def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    low = (abs(a * b)) / (gcd(a, b))

    return low


def lcm_list(x, y, ):
    top = ""

    for i in range(x, y + 1):
        if i < y:
            top += "lcm(" + str(i) + ","
        else:
            top += str(i) + ")" * (y - x)

    top_final = eval(top)

    return int(top_final)


print(lcm_list(1, 20))
