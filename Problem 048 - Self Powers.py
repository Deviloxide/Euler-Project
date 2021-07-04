def self_powers_sum(end):
    num = 1
    total = 0

    while num < end + 1:
        total += num ** num
        num += 1

    return total


print(self_powers_sum(1000))
