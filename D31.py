
def minEditDistance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1) #additions

    if str1[0] == str2[0]:
        return minEditDistance(str1[1:],str2[1:])
    
    # Insertion, deletion, and replacement
    return min(minEditDistance(str1,str2[1:])+1, minEditDistance(str1[1:],str2)+1, minEditDistance(str1[1:],str2[1:])+1)

print(minEditDistance("sitting","kitten"))
print(minEditDistance("sittin","kitten"))
print(minEditDistance("poggers","pog"))
print(minEditDistance("poggers","pogchamp"))