import math

def minimax(is_max, arr, i, j, a, b, ply, max_depth):
    if ply >= max_depth or i >= j:
        if is_max:
            return arr[i]
        return 0

    if is_max:
        f = lambda a, b, i, j : max(a[i] + b[0], a[j] + b[1])
    else:
        f = lambda a, b, i, j : min(b)

    x = [minimax(not is_max, arr, i+1, j, a, b, ply + 1, max_depth),
            minimax(not is_max, arr, i, j-1, a, b, ply + 1, max_depth)]

    return f(arr, x, i, j)
     
# Driver code
scores = [3, 5, 2, 9]
 
treeDepth = math.log(len(scores), 2)
 
print("The optimal value is : ", end = "")
print(minimax(True, scores, 0, len(scores)-1, 0, 0, 0, 100))
 
# This code is contributed
# by rootshadow