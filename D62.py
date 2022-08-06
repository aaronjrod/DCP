from numpy import zeros

def numWays(matrix):
    return numWaysHelper(matrix,0,0)

def numWaysHelper(matrix,n,m):
    # Base case, check if at edge
    if len(matrix)-1 == n or len(matrix[0])-1 == m:
        matrix[n][m] = 1

    if matrix[n][m] == 0:
        matrix[n][m] = numWaysHelper(matrix,n+1,m) + numWaysHelper(matrix,n,m+1)
    return matrix[n][m]
     

# matrix = [[1,2,3],[4,5,6]]
print(numWays(zeros((2,2))))
print(numWays(zeros((1,1))))

matrix = zeros((5,5))
print(numWays(matrix))
print(matrix)
