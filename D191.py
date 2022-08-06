def min_removed(arr):
    arr.sort(key = lambda x: x[1])
    total = len(arr)
    count = 0
    while arr:
        next = arr.pop(0)
        count += 1
        arr_copy = arr.copy()
        for interval in arr_copy:
            if interval[0] < next[1]:
                arr.remove(interval)
    return total - count

arr = [[7, 9], [2, 4], [5, 8]]
print(min_removed(arr))