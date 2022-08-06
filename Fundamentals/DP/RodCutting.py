INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and arr[] as prices of different pieces
def cut_rod_naive(arr, j):
    if j == 0:
        return 0
    
    max_val = INT_MIN
    for i in range(j):
        max_val = max(max_val, arr[i] + cut_rod_naive(arr, j-i-1))

    return max_val

# Top down construction of val, uses pointers
def memoized_cut_rod(arr, n): 
    val = [0 for x in range(n + 1)]
    return memoized_cut_rod_helper(arr, n, val)

# Each subproblem val[j] solved exactly once
def memoized_cut_rod_helper(arr, j, val):
    if j == 0:
        return 0

    if val[j] <= 0:
        max_val = INT_MIN
        # Check every cut to determine optimal val[j]
        for i in range(j):
            max_val = max(max_val, arr[i] + memoized_cut_rod_helper(arr, j-i-1, val))
        val[j] = max_val

    return val[j]

# Bottom up construction of val
# Each subproblem val[j] solved exactly once
def cut_rod(arr, n):
    val = [0 for x in range(n + 1)]

    for j in range(1, n+1):
        max_val = INT_MIN
        # Check every cut to determine optimal val[j]
        for i in range(j):
            max_val = max(max_val, arr[i] + val[j-i-1])
        val[j] = max_val
 
    return val[n]
 
# Driver program to test above functions 
arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
len_list = [0, 4, 8, 10] #[10,22,30]
for len in len_list:
    print(cut_rod(arr, len))
    print(cut_rod_naive(arr, len))
    print(memoized_cut_rod(arr, len))