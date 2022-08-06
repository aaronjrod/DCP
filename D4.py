from numpy import zeros


def sortArr(arr):
    out = zeros(len(arr)+1)
    for i in range(len(arr)):
        if arr[i] > 0:
            out[arr[i]-1] = arr[i]
    return out

def sortArr2(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            temp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
    return arr

def missingInt(arr):
    arr = sortArr(arr)
    
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    
    n = len(arr)
    if arr[len(arr)-1] == 0:
        n -= 1
    expectedSum = n*(n+1)/2

    return expectedSum - sum

arrList = [[3, 4, -1, 1], [1, 2, 0], [3, 4, 4, 1], [1,3], []]
for arr in arrList:
    print(sortArr2(arr))
    print(missingInt(arr))