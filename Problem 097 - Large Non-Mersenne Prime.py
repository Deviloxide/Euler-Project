def last_digits(base, exp, digits, mult=1, add=0):
    dec = "1" + "0" * digits
    result = str(mult * pow(base, exp, int(dec)) + add)
    return result[-digits:]


print(last_digits(2, 7830457, 10, 28433, 1))
