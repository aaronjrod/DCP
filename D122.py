def mostCoins(arr):
    return arr[0][0] + max(mostCoinsHelper(arr,0,1), mostCoinsHelper(arr,1,0))

def mostCoinsHelper(arr, i, j):
    if i >= len(arr):
        return 0
    if j >= len(arr[0]):
        return 0
    return arr[i][j] + max(mostCoinsHelper(arr,i,j+1), mostCoinsHelper(arr,i+1,j))

matrix = [[0, 3, 1, 12],
          [2, 0, 50, 4],
          [1, 5, 3, 1]]
#matrix = [[0]]
print(matrix)
print(len(matrix))
print(mostCoins(matrix))