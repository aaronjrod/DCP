def max_contig_sum_2(arr):
    stor = [[0 for x in range(len(arr))] for x in range(len(arr))]
    return max(0, max_contig_sum_helper(arr, 0, len(arr)-1, sum(arr), stor))

def max_contig_sum_helper(arr, i, j, cur_sum, stor):
    if i >= j:
        return cur_sum

    if not stor[i][j]:
        stor[i][j] = max(cur_sum,
        max_contig_sum_helper(arr, i+1, j, cur_sum-arr[i], stor), 
        max_contig_sum_helper(arr, i, j-1, cur_sum-arr[j], stor))

    return stor[i][j]

def max_contig_sum_3(arr):
    stor = [0 for x in range(len(arr))]
    return max_contig_sum_helper_3(arr, 0, 0, stor)

def max_contig_sum_helper_3(arr, i, cur_sum, stor):
    if i >= len(arr):
        return cur_sum

    if not stor[i]:
        cur_sum = max(cur_sum + arr[i], 0)
        stor[i] = max(cur_sum, max_contig_sum_helper_3(arr, i+1, cur_sum, stor))
    return stor[i]

# Kadane’s Algorithm:
def max_contig_sum(arr):
    max_sum = cur_sum = 0

    for i in range(len(arr)):
        cur_sum = max(cur_sum + arr[i], 0)
        max_sum = max(cur_sum, max_sum)
        
    return max_sum

arr_list = [[34, -50, 42, 14, -5, 86], [-5, -1, -8, -9], [34, -50, 42, 14, -5], [-2, -3, 4, -1, -2, 1, 5, -3]]
for arr in arr_list:
    print(max_contig_sum(arr))
    print(max_contig_sum_2(arr))
    print(max_contig_sum_3(arr))