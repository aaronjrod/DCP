def reverseByDelim(str):
    strWords = []
    i = 0
    for j in range(len(str)):
        if str[j] == " ":
            strWords.append(str[i:j])
            i = j+1
    if i != j+1:
        strWords.append(str[i:j+1])

    out = ""
    while len(strWords) > 1:
        out += strWords.pop()
        out += " "
    out += strWords.pop()

    return out

print(reverseByDelim("hello world here"))
