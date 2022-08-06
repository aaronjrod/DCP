def findPalindrome(str):
    list = []
    if checkPalindrome(str):
        return str
    
    list.append(findPalindrome(str[1:]))
    list.append(findPalindrome(str[:len(str)-1]))
    return(max(list, key=len))

def checkPalindrome(str):
    i = 0
    j = len(str) - 1
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

strList = ['anana','aabcdcb', 'bananas', 'ananaracecar','']
for str in strList:
    print(findPalindrome(str))


