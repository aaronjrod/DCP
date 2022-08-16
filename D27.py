
def is_opening(char):
    return char in ["(","{","["]

def is_matching(charO,charC):
    if charO == "(" and charC == ")":
        return True
    if charO == "[" and charC == "]":
        return True
    if charO == "{" and charC == "}":
        return True
    return False

def isValid(str):
    # Treating open_list like a stack
    open_list = []
    while len(str) > 0:
        if is_opening(str[0]):
            open_list.append(str[0])
        else:
            if not is_matching(open_list.pop(), str[0]):
                return False
        str = str[1:]

    if len(open_list) > 0:
        return False

    return True

sL = ["[][][][]","[{}]","([])[]({})","([)]","((()","[{]}"]
for str in sL:
    print(isValid(str))