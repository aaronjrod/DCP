def longest_subset(arr):
    return longest_subset_helper(arr, [])

def longest_subset_helper(arr, best):
    if len(arr) <= 1:
        return best + arr

    arr_copy = arr.copy()
    for item in arr:
        if item % arr_copy[0] != 0 and arr_copy[0] % item != 0:
            arr_copy.remove(item)
    val = [arr_copy.pop(0)]

    one = longest_subset_helper(arr[1:], best)
    two = longest_subset_helper(arr_copy, best + val)
    
    if len(one) > len(two):
        return one
    return two

arr_list = [ [3, 5, 10, 20, 21],
    [1, 3, 6, 24],
    [42, 10, 5, 3, 18, 21, 12], 
    [], 
    [1], 
    [1,3], 
    [3,5]]

for arr in arr_list:
    print(longest_subset(arr))