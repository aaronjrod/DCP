def min_cost(matrix):
    N = len(matrix)
    k = len(matrix[0])
    storage = [[-1 for x in range(k)] for x in range(N)]
    return min_cost_helper(matrix, 0, None, storage)

# House cannot be same color as prev house
# N by k
#N: Houe num
# k: Previous color
def min_cost_helper(matrix, i, k, storage):
    if i >= len(matrix):
        return 0

    min_cost = 9999
    for j in range(len(matrix[0])):
        if j == k:
            continue
        if storage[i][j] == -1:
            storage[i][j] = min_cost_helper(matrix, i+1, j, storage)
        min_cost = min(matrix[i][j] + storage[i][j], min_cost)
    return min_cost

print(min_cost([[14, 2, 11], [11,14,5], [14,3,10]]))
print(min_cost([[1,2,3], [1,4,6]]))