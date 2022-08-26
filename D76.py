def num_ordered_rows(matrix):
    count = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)-1):
            if matrix[i][j] > matrix[i+1][j]:
                count += 1
                break
    return count

matrix_list = [['cba', 'daf', 'ghi'], ['abcdefg'], ['zyx','wvu','tsr']]
for matrix in matrix_list:
    print(num_ordered_rows(matrix))