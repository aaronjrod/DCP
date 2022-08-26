def helper(arr, x):
    arr = arr.copy()
    arr.pop(x)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def is_non_decreasing(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return helper(arr, i) or helper(arr, i+1)
    return True

arr_list = [[10,5,7], [10,5,1], [1,2,-10, 3,4], [1,2,10,3,4],[1,2,3,3,4],
            [1,2,10,11,3,4],[1,2,10,11,4]]
for arr in arr_list:
    print(is_non_decreasing(arr))