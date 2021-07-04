def longest_collatz_sequence(limit):
    big_num = 0
    big_count = 0

    for i in range(int(limit / 2), limit + 1):
        count = 0
        num = i

        while True:
            if num % 2 == 0:
                count += 1
                num = num / 2
            elif num == 1:
                count += 1
                break
            else:
                count += 1
                num = 3 * num + 1

        if count > big_count:
            big_num = i
            big_count = count

    return big_num, big_count


print(longest_collatz_sequence(99999))
