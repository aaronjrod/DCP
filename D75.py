def longest_contig(arr):
    return longest_contig_helper(arr, -10000, 0)

def longest_contig_helper(arr, lowest, i):
    if i >= len(arr):
        return 0
    val = 0
    if arr[i] > lowest:
        val = 1 + longest_contig_helper(arr, arr[i], i+1)
    return max(val, longest_contig_helper(arr, lowest, i+1))

print(longest_contig([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))