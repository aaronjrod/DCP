def LCS(str1, str2):
    matrix = [["" for x in range(len(str2))] for x in range(len(str1))]
    return LCS_helper(str1, str2, 0, 0, matrix)

def LCS_helper(str1, str2, i, j, matrix):
    if i >= len(str1) or j >= len(str2):
        return ""

    if not matrix[i][j]:
        if str1[i] == str2[j]:
            matrix[i][j] = str1[i] + LCS_helper(str1, str2, i+1, j+1, matrix)
        else:
            L = LCS_helper(str1, str2, i+1, j, matrix)
            R = LCS_helper(str1, str2, i, j+1, matrix)
            
            if len(L)>len(R):
                matrix[i][j] = L
            else:
                matrix[i][j] = R
    return matrix[i][j]

def multi_LCS(arr):
    if len(arr) == 1:
        return LCS(arr)
    curr_LCS = LCS(arr[0], arr[1])
    for i in range(2, len(arr)):
        curr_LCS = LCS(curr_LCS, arr[i])
    return curr_LCS
    
arr = ["epidemiologist","refrigeration", "supercalifragilisticexpialodocious"]
print(multi_LCS(arr))
