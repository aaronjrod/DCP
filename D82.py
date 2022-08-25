def read7():
    return "hi"

def readN(n):
    string = ""
    while n > len(string):
        string += read7()
    return string[:n]

print(readN(8))
print(readN(9))