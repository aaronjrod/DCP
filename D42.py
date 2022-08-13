def return_subset(arr, k):
    return return_subset_helper(arr, k, 0, [])
    
def return_subset_helper(arr, k, i, curr_S):
    if k == 0:
        return curr_S
    if k < 0 or i >= len(arr):
        return None
    
    val = arr[i]
    a1 = return_subset_helper(arr, k-val, i+1, curr_S+[val])
    if a1:
        return a1
    return return_subset_helper(arr, k, i+1, curr_S)

print(return_subset( [12, 1, 61, 5, 9, 2, 24] , 24))