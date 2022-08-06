def reverseByDelim(str, delims):
    strWords = []
    strDelims = []
    i = 0
    for j in range(len(str)):
        if str[j] in delims:
            strWords.append(str[i:j])
            strDelims.append(str[j])
            i = j+1
    if i != j+1:
        strWords.append(str[i:j+1])

    out = ""
    while len(strWords) > 0:
        out += strWords.pop()
        if len(strDelims) > 0:
            out += strDelims.pop(0)

    return out

strList = ["hello/world:here", "hello/world:here/", "hello//world:here"]
delims = [":","/"]
for str in strList:
    print(reverseByDelim(str, delims))
