def isSum(arr, k):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False

def isSum2(arr, k):
    myDict = dict()
    for i in range(len(arr)):
        if arr[i] in myDict:
            return True
        myDict[k-arr[i]] = 1
    return False

arr = [10, 15, 3, 7]
k = 17
print(isSum(arr,k))
print(isSum2(arr,k))