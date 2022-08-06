
def isOpening(char):
    if char in ["(","{","["]:
        return True
    return False

def isMatching(charO,charC):
    if charO == "(" and charC == ")":
        return True
    elif charO == "[" and charC == "]":
        return True
    elif charO == "{" and charC == "}":
        return True
    return False

def isValid(str):
    openList = []
    while len(str) > 0:
        if isOpening(str[0:1]):
            openList.append(str[0:1])
        else:
            if not isMatching(openList.pop(), str[0:1]):
                return False
        str = str[1:]

    if len(openList) > 0:
        return False

    return True

#print(isOpening("{"))
#print(isOpening("}"))


sL = ["[][][][]","[{}]","([])[]({})","([)]","((()","[{]}"]
for str in sL:
    print(isValid(str))