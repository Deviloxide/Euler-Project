def fibo_even_sum(n):
    numList = []

    x = 0
    y = 1
    z = 0
    total = 0

    if n == 0:
        numList.append(0)
        numList.append(1)
        return numList
    else:
        while z <= n:
            z = x + y
            if z > n:
                break
            if z % 2 == 0:
                numList.append(z)
            x = y
            y = z
        for ele in range(0, len(numList)):
            total = total + numList[ele]
        return "The sum of all even fibonacci numbers below " + str(n) + " is " + str(total) + "."


print(fibo_even_sum(4000000))
