def best_cost(arr):
    return arr[0][0] + best_cost_helper(arr, 0, 0)

def best_cost_helper(arr, i, j):
    cost_left = 0
    if i+1 < len(arr) and j < len(arr[i+1]):
        cost_left = arr[i+1][j] + best_cost_helper(arr, i+1, j)

    cost_right = 0
    if i+1 < len(arr) and j+1 < len(arr[i+1]):
        cost_right = arr[i+1][j+1] + best_cost_helper(arr, i+1, j+1)
    
    if cost_left > cost_right:
        return cost_left 
    return cost_right

arr = [[1], [2, 3], [1, 5, 1]]
highest_cost = best_cost(arr)
print(highest_cost)

arr = [[1], [2, 5], [1]]
highest_cost = best_cost(arr)
print(highest_cost)