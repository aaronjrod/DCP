INT_MIN = -32767
 
def cut_rod_naive(arr, n):
    if n == 0:
        return 0
    
    max_val = INT_MIN
    for i in range(0, n):
        max_val = max(max_val, arr[i] + cut_rod_naive(arr, n-i-1))

    return max_val

def memoized_cut_rod(arr, n): 
    val = [INT_MIN for x in range(n + 1)]
    return memoized_cut_rod_aux(arr, n, val)
    
def memoized_cut_rod_aux(arr, n, val):
    if n == 0:
        return 0

    if val[n] < 0:
        max_val = INT_MIN
        for i in range(0, n):
            max_val = max(max_val, arr[i] + memoized_cut_rod_aux(arr, n-i-1, val))
        val[n] = max_val

    return val[n]

# Returns the best obtainable price for a rod of length n and arr[] as prices of different pieces
def cut_rod(arr, n):
    # Cache; represents ideal cost per length of rod
    val = [0 for x in range(n + 1)]

    # Build the table val[] in bottom up manner and return the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, arr[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]
 
# Driver program to test above functions
arr_list = [[1, 5, 8, 9, 10, 17, 17, 20], #22
            [1, 5, 8, 9, 10, 17, 17, 20, 24, 30], # 30
            [1, 5, 8, 9], #10
            ] 
for arr in arr_list:
    print(cut_rod(arr, len(arr)))
    print(cut_rod_naive(arr, len(arr)))
    print(memoized_cut_rod(arr, len(arr)))