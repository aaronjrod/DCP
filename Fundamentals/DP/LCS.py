def LCS_naive(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return ""
    
    if X[0] == Y[0]:
        return X[0] + LCS_naive(X[1:], Y[1:])

    A = LCS_naive(X[1:], Y[:])
    B = LCS_naive(X[:], Y[1:])
    if len(A) > len(B):
        return A
    return B

# Build a 2x2 table, of values that increment based on equivalent chars
# and pointers that point to the adjacent index of greatest value
def LCS_DP(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for x in range(n+1)] for x in range(m+1)]
    c = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i+1][j+1] = "nw"
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i+1][j+1] = "n"
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i+1][j+1] = "w"
    return b

def print_LCS(b, X):
    return print_LCS_Helper(b, X, len(b)-1, len(b[0])-1)

def print_LCS_Helper(b, X, i, j):
    if i == 0 or j == 0:
        return ""
    if b[i][j] == "nw":
        return print_LCS_Helper(b, X, i-1, j-1) + X[i-1]
    elif b[i][j] == "n":
        return print_LCS_Helper(b, X, i-1, j)
    else:
        return print_LCS_Helper(b, X, i, j-1)

arr_list = [['ABCBDAB', 'ABDCABA']]
for arr in arr_list:
    print(LCS_naive(arr[0],arr[1]))
    b = LCS_DP(arr[0],arr[1])
    print(print_LCS(b, arr[0]))
