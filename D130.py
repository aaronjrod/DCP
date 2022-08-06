from xmlrpc.client import MAXINT, MININT

def maxProfit(prices, n, k):
     
    # Bottom-up DP approach
    profit = [[0 for i in range(k + 1)]
                 for j in range(n)]
     
    # Profit is zero for the first
    # day and for zero transactions
    for i in range(1, n):
         
        for j in range(1, k + 1):
            max_so_far = 0
             
            for l in range(i):
                max_so_far = max(max_so_far, prices[i] -
                            prices[l] + profit[l][j - 1])
                             
            profit[i][j] = max(profit[i - 1][j], max_so_far)
     
    return profit[n - 1][k]

def maxProfitHelper(arr, l, r):
    lMin = MAXINT
    lMax = MININT
    maxPro = MININT
    index = 0

    for i in range(l, r):
        if arr[i] < lMin:
            lMin = arr[i]
            lMax = MININT
        if arr[i] > lMax:
            lMax = arr[i]
            if lMax - lMin > maxPro:
                maxPro = lMax - lMin
    return maxPro

arrList = [[5, 2, 4, 0, 1],[3,3,4,6,2,1,1],[4,0,4,5,8]]
for arr in arrList:
    print(maxProfit(arr, len(arr), 2))