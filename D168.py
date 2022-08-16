# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given an N by N matrix, rotate it by 90 degrees clockwise.

# For example, given the following matrix:

# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# you should return:

# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
# Follow-up: What if you couldn't use any extra space?

# Move matrix[1][1] to matrix[1][n-1]
# matrix[1][2] to matrix[2][n]
# ... to matrix[1][n-2] to matrix[n-1][n]

# OR:
# For i = 0, j = 1
# while i < n (3)
# matrix[i][j] to matrix[i+1][n-j]
# matrix[i][n-j] to matrix [n-i][n-j]
# matrix[n-i][n-j] to matrix[n-i][j]
# matrix[n-i][j] to matrix[i][j]
# i+= 1
def rotate(matrix):

