list= ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "doggggggg"]
k = 16

def justify(strList, k):
    # If only one word in list, return padded
    if len(strList) == 1:
        out = strList[0]
        for i in range(len(strList[0]),k):
            out += " "
        return out

    length = sum(len(s) for s in strList)
    d = (int) ((k-length) / (len(strList) - 1))
    r = (k-length) % (len(strList) - 1)

    out = ""
    for i in range(0,len(strList)):
        out += strList[i]
        # If last word, skip padding
        if i+1 == len(strList):
            continue
        for i in range(0,d):
            out += " "
        if r > 0:
            out += " "
            r -= 1
        
    return out

def justifier(list,k):
    i = 0
    outList = []

    while i < len(list):
        tempList = []
        totalLen = 0
        while i < len(list) and totalLen + len(list[i]) <= k:
            totalLen += len(list[i]) + 1
            tempList.append(list[i])
            i += 1
        outList.append(justify(tempList,k))
        
    return outList

out = justifier(list,k)
print(out)
for item in out:
    print(item)
for item in out:
    print(len(item))
# print(len(out))
