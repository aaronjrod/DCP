def longest_subarray(arr):
    return longest_subarray_helper(arr, 0, 0)

def longest_subarray_helper(arr, i, j):
    if j >= len(arr):
        return j - i

    val = arr[j]
    if val not in arr[i:j]:
        return longest_subarray_helper(arr, i, j+1)
    
    k = arr.index(val)
    return max(j - i, longest_subarray_helper(arr, k+1, j+1))

arr_list = [[5, 1, 3, 5, 2, 3, 4, 1], [5, 1, 3, 5, 2, 3]]
for arr in arr_list:
    print(longest_subarray(arr))