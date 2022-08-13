def max_contig_sum(arr):
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

arr_list = [[34, -50, 42, 14, -5, 86], [-5, -1, -8, -9], [34, -50, 42, 14, -5]]
for arr in arr_list:
    print(max_contig_sum(arr))
