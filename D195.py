

from re import A


def compute_195(matrix, i1, j1, i2, j2):
    N = len(matrix)
    M = len(matrix[0])
    count = N * M
    A = matrix[i1][j1]
    B = matrix[i2][j2]

    print((i1+1)*(j1+1))
    print((N-i2)*(M-j2))
    count -= (i1+1)*(j1+1)
    count -= (N-i2)*(M-j2)
    
    count -= block(matrix, A, B, 0, j1+1, i1, M)
    count -= block(matrix, A, B, i1, j2+1, i2, M)
    count -= block(matrix, A, B, i1+1, 0, N, j1)
    count -= block(matrix, A, B, i2+1, j1, N, j2)
    return count

def block(matrix, A, B, i1, j1, i2, j2):
    count = 0
    for i in range(i1, i2):
        for j in range(j1, j2):
            val = matrix[i][j]
            if val < A or B < val:
                count += 1
                print(val)
    return count
# matrix =   [[1,  3,  4,  10, 15, 20],
#             [2,  6,  9,  14, 17, 21],
#             [7,  8,  10, 15, 21, 22],
#             [10, 11, 12, 23, 30, 35],
#             [20, 25, 30, 35, 40, 45]]

matrix = [[1,  3,  7,  10, 15, 20],
          [2,  6,  9,  14, 22, 25],
          [3,  8,  10, 15, 25, 30],
          [10, 11, 12, 23, 30, 35],
          [20, 25, 30, 35, 40, 45]]
print(compute_195(matrix, 1,1,3,3))