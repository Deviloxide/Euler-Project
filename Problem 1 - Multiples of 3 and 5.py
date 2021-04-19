def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left sub-array
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right sub-array
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def multiples_of_3_and_5(num, type):
    numList = []

    three = int((num - (num % 3)) / 3) + 1
    five = int((num - (num % 5)) / 5) + 1

    for i in range(three):
        var1 = i * 3
        numList.append(var1)

    for i in range(five):
        if binary_search(numList, 0, len(numList) - 1, i) == -1:
            numList.append(5 * i)
        else:
            pass

    if type == list:
        if num % 3 == 0 or num % 5 == 0:
            del numList[-1]
        return "All multiples of 3 or 5 are: " + str(numList)

    elif type == sum:
        total = 0
        for ele in range(0, len(numList)):
            total = total + numList[ele]
        if num % 3 == 0 or num % 5 == 0:
            del numList[-1]
        return "The sum of all multiples of 3 or 5 below " + str(num) + " is " + str(total) + "."

    else:
        return "There was a problem."


print(multiples_of_3_and_5(1000, list))

print(multiples_of_3_and_5(1000, sum))

print(multiples_of_3_and_5(1000, "Thanh"))
