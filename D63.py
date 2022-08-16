matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]


print(matrix)
targetWord = "FOAM"

# Idea: Find first letter, then check rest
def inMatrix(matrix,word):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if (matrix[i][j] == word[0]):
                if wordFinder(matrix, word, i, j):
                    return True
    return False

def wordFinder(matrix, word, i, j):
    n = len(matrix)
    m = len(matrix[0])
    length = len(word)

    isWordH = True
    isWordV = True

    #Check if is too long first
    if i+length <= n:
        k = 0
        while k < length:
            if matrix[i+k][j] != word[k]:
                isWordH = False
            k += 1
    else:
        isWordH = False

    if isWordH:
        return True

    if j+length <= m:
        k = 0
        while k < length:
            if matrix[i][j+k] != word[k]:
                isWordV = False
            k += 1
    else:
        isWordV = False

    return isWordV
    
print(inMatrix(matrix,"FOAM"))
print(inMatrix(matrix,"FOAD"))
print(inMatrix(matrix,"MASS"))
print(inMatrix(matrix,"ASS"))
print(inMatrix(matrix,"P"))
print(inMatrix(matrix,"Z"))

