from pandas import array


def squareSort(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]
    arr.sort()
    return arr
     
arr = [-9, -2, 0, 2, 3]
print(squareSort(arr))