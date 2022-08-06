from xmlrpc.client import MAXINT, MININT


def maxProfit(arr):
    maxProf = MININT
    buyAt = MAXINT
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if (arr[j]-arr[i] > maxProf):
                maxProf = arr[j]-arr[i] 
                buyAt = arr[i]
    return buyAt

def maxProfit2(arr):
    lMin = MAXINT
    lMax = MININT
    maxProf = MININT
    buyAt = MAXINT

    for i in range(len(arr)):
        if arr[i] > lMax:
            lMax = arr[i]
            if (lMax-lMin > maxProf):
                maxProf = lMax-lMin
                buyAt = lMin

        if arr[i] < lMin:
            lMin = arr[i]
            lMax = MININT
    return buyAt


arrList = [[9, 11, 8, 5, 7, 10], [1, 5, 2, 3, 7, 6, 4, 5], [100, 180, 260, 310, 40, 535, 695],[],[1]]
for arr in arrList:
    print(maxProfit(arr))
    print(maxProfit2(arr))