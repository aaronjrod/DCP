def waterTrapped(ls):
    if not ls:
        return 0
    
    stor = []

    # Assume right wall is infinitely tall, run
    i = 0
    while i < len(ls):
        temp = 0
        lwall = ls[i]
        i += 1

        while i < len(ls) and lwall > ls[i]:
            temp += lwall - ls[i]
            i += 1
        stor.append(temp)
    
    # Check right wall, using last lwall as ref
    rwall = ls[-1]
    if lwall > rwall:
        temp = 0
        i = len(ls)-2

        while i > 0 and rwall > ls[i]:
            temp += rwall - ls[i]
            i -= 1
        stor.pop()
        stor.append(temp)

    return sum(stor)

a1 = [2, 1, 2]
a2 = [3, 0, 1, 3, 0, 2]
a3 = [3, 0, 1, 3, 0, 5]

aList = [a1,a2,a3,[3, 1],[3,1,1],[],[1],[1,1,1,1,0,1]]
for item in aList:
    print(waterTrapped(item))
