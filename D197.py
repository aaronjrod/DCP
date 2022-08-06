def rotate_array(arr, k):
    k = len(arr) - k - 1
    left = arr[:k]
    right = arr[k:]
    return right + left

arr = [1,2,3,4,5,6,7]
for i in range(3):
    print(rotate_array(arr, i))