import math

def square_root_convergents(limit):
    a = 1
    b = 1
    check_count = 0

    for i in range(0,limit):
        new_a = 2 * b + a
        new_b = b + a

        check = int(math.log10(new_a)) > int(math.log10(new_b))
        if check == True:
            check_count += 1

        a = new_a
        b = new_b

    return check_count

print(square_root_convergents(1000))
