def max_return(arr, fee):
    return max_return_helper(arr, fee, 0, 0)

def max_return_helper(arr, fee, i, val):
    if i >= len(arr):
        return 0

    if val > 0:
        max_val = -100000
        for j in range(i, len(arr)):
            returns = arr[j] - val - fee
            max_val = max(max_val, returns + max_return_helper(arr, fee, j+1, 0))
        return max_val
        
    return max_return_helper(arr, fee, i+1, arr[i])
            
arr_list = [[1, 3, 2, 8, 4, 10]]

for arr in arr_list:
    print(max_return(arr,2))