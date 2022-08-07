def smallest_diff(arr):
    return smallest_diff_helper(arr, 0, [], [], 0, 0)

def smallest_diff_helper(arr, i, L, R, sum_L, sum_R):
    if i >= len(arr):
        return [L, R, sum_L, sum_R]

    val = arr[i]
    x = smallest_diff_helper(arr, i+1, L+[val], R, sum_L+val, sum_R)
    y = smallest_diff_helper(arr, i+1, L, R+[val], sum_L, sum_R+val)
    diff = abs(x[3]-x[2]) - abs(y[3]-y[2])
    if diff > 0:
        return y
    return x

arr_list = [[5, 10, 15, 20, 25]]
for arr in arr_list:
    print(smallest_diff(arr))

    