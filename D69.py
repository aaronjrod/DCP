def largest_prod(arr):
    if len(arr) < 3:
        return -1
    return largest_prod_helper(arr, 0, 3, 1)

def largest_prod_helper(arr, i, count, prod):
    if i >= len(arr) or count == 0:
        return prod
    a = largest_prod_helper(arr, i+1, count-1, prod*arr[i])
    b = largest_prod_helper(arr, i+1, count, prod)
    return max(a, b)

def largest_prod_2(arr):
    n = len(arr)
    if n < 3:
        return -1

    arr.sort()

    return max(arr[0] * arr[1] * arr[n - 1],
               arr[n - 1] * arr[n - 2] * arr[n - 3])

print(largest_prod([-10, 5, -10, 2, 4, 1]))
print(largest_prod_2([-10, 5, -10, 2, 4, 1]))