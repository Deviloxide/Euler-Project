month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def counting_sundays(start, end, weekday):
    day = weekday
    sunday_count = 0

    for year in range(start, end):
        for length in month_lengths:
            day += length

            if length == 28 and year % 4 == 0:
                day += 1
            if day % 7 == 0:
                sunday_count += 1

    return sunday_count


print(counting_sundays(1901, 2001, 2))
