def largest_non_adjacent_sum(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    
    arr[1] = max(arr[0], arr[1])
    i = 2
    while i < len(arr):
        arr[i] = max(arr[i], arr[i]+arr[i-2], arr[i-1])
        i += 1
    return arr[i-1]

arr_list = [[],[1],[1,2],[1,2,3],[2, 4, 6, 2, 5], 
            [5, 1, 1, 5]]
for arr in arr_list:
    print(largest_non_adjacent_sum(arr))