def can_partition(arr):
    return can_partition_helper(arr, 0, 0)

def can_partition_helper(arr, s1, s2):
    if not arr:
        return s1 == s2
    
    arr_copy = arr.copy()
    val = arr_copy.pop()
    return can_partition_helper(arr_copy, s1+val, s2) or can_partition_helper(arr_copy, s1, s2+val)

print(can_partition([15, 5, 20, 10, 35, 15, 10]))
print(can_partition([15, 5, 20, 10, 35]))