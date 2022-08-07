def binary_search(arr, val, i, j):
    # Distinguish whether we should insert before or after the left boundary.
    if i == j:
        if arr[i] > val:
            return i
        else:
            return i+1
    if i > j:
        return i
 
    mid = (i+j)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, j)
    elif arr[mid] > val:
        return binary_search(arr, val, i, mid-1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]

        j = i-1
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr

def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
# from unsorted part and putting it at the beginning.
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
 
        for j in range(i+1, len(arr)):
            # Select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swapping the elements to sort the array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr)//2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    i = j = k = 0
    # Merge L and R into arr; conquer
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Adding left-over elements from one of two temp arrays
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
    return arr
 
# Works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, 
# according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort.
def quick_sort_helper(arr, l, r):
    if len(arr) <= 1:
        return arr

    if l < r:
        # Partition; divide/conquer
        # Pick pivot by last element in the array
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                # Swapping values smaller than the pivot to the front
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # Finally swapping the last element with the pointer indexed number
        arr[i], arr[r] = arr[r], arr[i]

        # Divide
        quick_sort_helper(arr, l, i-1)  # Recursively sorting the left values
        quick_sort_helper(arr, i+1, r)  # Recursively sorting the right values
    return arr

def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr)-1)

arr_list = [[12, 11, 13, 5, 6],
            [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54],
            [4, 5, 1, 2, 3],
            []]

for arr in arr_list:
    print(insertion_sort(arr.copy()))
    print(insertion_sort_binary(arr.copy()))   
    print(selection_sort(arr.copy()))
    print(merge_sort(arr.copy()))
    print(quick_sort(arr.copy()))
    arr.sort()
    print(arr)