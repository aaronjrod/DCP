def reach_end(arr, i):
    if len(arr) <= i+1:
        return True
    
    num_skips = arr[i]

    for j in range(i+num_skips, i, -1):
        if reach_end(arr, j):
            return True
    return False

arr_list = [[1, 3, 1, 2, 0, 1],
    [1, 2, 1, 0, 0]]

for arr in arr_list:
    print(reach_end(arr, 0))