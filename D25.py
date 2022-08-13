def regex_matching(pattern, text):
    return regex_matching_helper(pattern, text, 0, 0)

def regex_matching_helper(pattern, text, i, j):
    if i == len(pattern) and j == len(text):
        return True
    elif i == len(pattern) or j == len(text):
        return False

    if pattern[i] == '*':
        if pattern[i-1] == text[j] or pattern[i-1] == '.':
            return regex_matching_helper(pattern, text, i+1, j) or regex_matching_helper(pattern, text, i, j+1)
        return regex_matching_helper(pattern, text, i+1, j)
    elif pattern[i] == text[j] or pattern[i] == '.':
        return regex_matching_helper(pattern, text, i+1, j+1)
    return False

print(regex_matching("ra.","ray"))      #T
print(regex_matching("ra.","raymond"))  #F
print(regex_matching(".*at","chat"))    #T

print(regex_matching("*****ba*****bab","baaabab"))   #T
print(regex_matching("*****ba*****ab","baaabab"))   #F
print(regex_matching("baaa.ab","baaabab"))   #T
print(regex_matching("ba*ba.","baaabab"))   #T
print(regex_matching("a*ab","baaabab"))   #F