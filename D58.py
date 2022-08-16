
def binary_search(arr, k, i, j):
    while i + 1 < j:
        mid = (i+j) // 2
        if k < arr[mid]:
            j = mid
        else:
            i = mid

    if arr[i] == k:
        return i
    elif arr[j] == k:
        return j
    return None

def find_pivot(arr, k):
    i = pivot = 0
    j = len(arr)-1
    while arr[i] > arr[j] and i + 1 < j:
        pivot = (i+j) // 2
        if arr[pivot] <= arr[j]:
            j = pivot
        else:
            i = pivot

    if k <= arr[len(arr)-1]:
        return binary_search(arr, k, pivot, len(arr)-1)
    return binary_search(arr, k, 0, pivot)

arr = [x for x in range(9)]
for i in range(10):
    print(find_pivot(arr, i))
arr = [13, 18, 25, 2, 8, 10]
for i in arr:
    print(find_pivot(arr, i))
print(find_pivot(arr, 14))
print(find_pivot(arr, 4))