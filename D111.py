def findAnagramIndex(W, S):
    indices = []
    for i in range(len(S) - len(W)+1):
        substr = S[i:i+len(W)]
        print(substr)
        if isAnagram(substr, W):
            indices.append(i)
    return indices

def isAnagram(w1, w2):
    d1 = dict()
    d2 = dict()
    for i in range(len(w1)):
        d1[w1[i]] = 1
        d2[w2[i]] = 1
    return d1 == d2

print(isAnagram('car','rac'))
print(isAnagram('car','ric'))
print(findAnagramIndex("ab", "abxaba"))