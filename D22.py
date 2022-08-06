def findWords(string,list):
    if not list:
        return None

    sentence = []
    str = ""
    while len(string) > 0:
        str += string[0]
        string = string[1:]
        if str in list:
            sentence.append(str)
            str = ""
    return sentence

list = ['quick', 'brown', 'the', 'fox', 'bed', 'bath', 'bedbath', 'and', 'beyond']
set = set()
for word in list:
    set.add(word)

sentence = findWords("bedbathandbeyond",set)
print(sentence)

sentence = findWords("thequickbrownfox",set)
print(sentence)
