for num in range (1380000000, 1400000000):
    ahh = str(num ** 2)
    if ahh[::2] == '1234567890':
        print(num)
        break
