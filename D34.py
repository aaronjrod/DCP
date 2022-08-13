def min_insertions(string):
    str_len = len(string)
    output = min_insertions_helper(string, 0, str_len-1)
    print(len(output) - str_len)
    return output

# def min_insertions_helper(str, i, j, matrix):
#     if i >= j:
#         return 0
    
#     if matrix[i][j] == "":
#         if str[i] == str[j]:
#             matrix[i][j] = min_insertions_helper(str, i+1, j-1, matrix)
#         else:
#             matrix[i][j] = 1 + min(min_insertions_helper(str, i+1, j, matrix), min_insertions_helper(str, i, j-1, matrix))
    
#     return matrix[i][j]

def min_insertions_helper(str, i, j):
    if i >= j:
        return str
    
    val = ""
    if str[i] == str[j]:
        val = min_insertions_helper(str, i+1, j-1)
    else:
        L = min_insertions_helper(str[:j+1]+str[i]+str[j+1:], i+1, j)
        R = min_insertions_helper(str[:i]+str[j]+str[i:], i+1, j)
        if len(L) > len(R) or (len(L) == len(R) and L > R):
            val = R
        else:
            val = L
    
    return val


arr = ['ab','aa',
        'abcd','abcda','abcde', 
        'race', 'google']
for i in arr:
    print(min_insertions(i))




