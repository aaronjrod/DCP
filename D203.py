
def find_pivot(arr):
    if not arr:
        return None
    last = len(arr)-1
    
    val = find_pivot_helper(arr, 0, last)
    if arr[0] <= arr[last]:
        return arr[0]
        
    return val

def find_pivot_helper(arr, i ,j):
    if i+1 == j or i == j:
        return arr[j]
    
    div = int((i+j)/2)
    if arr[i] > arr[div]:
        return find_pivot_helper(arr, i, div)
    return find_pivot_helper(arr, div, j)

arr_list = [[5, 7, 10, 3, 4],
    [5, 7, 8, 10, 3, 4],
    [5, 7, 8, 10, 11, 3, 4],
    [5, 7, 8, 10, 11],
    [5, 3, 4],
    [5, 3],
    [5],
    []]
 
for arr in arr_list:
    print(find_pivot(arr))