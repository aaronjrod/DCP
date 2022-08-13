def palindrome_splitter(string):
    output = []
    while string:
        j = len(string)
        while not is_palindrome(string[:j]):
            j -= 1

        output.append(string[:j])
        string = string[j:]
    return output

def is_palindrome(string):
    i = 0
    j = len(string)-1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

arr = ['racecarannakayak', 'feefsez','abc']
for i in arr:
    print(palindrome_splitter(i))
