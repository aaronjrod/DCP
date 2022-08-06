def findNonDuplicate(arr):
    while arr:
        val = arr[0]
        i = 0 # Number of vals
        while (arr.__contains__(val)):
            i += 1
            arr.remove(val)
        if i == 1:
            return val

arr = [6, 1, 3, 3, 3, 6, 6]
print(findNonDuplicate(arr))