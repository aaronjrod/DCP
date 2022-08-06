def canHop(arr):
    return canHopHelper(arr, 0)

def canHopHelper(arr, index):
    outcomes = []
    numHops = arr[index]
    for i in range(1,numHops+1):
        if index+i == len(arr)-1:
            return True
        outcomes.append(canHopHelper(arr, index+i))
        
    return True in outcomes

arr1 = [2, 0, 1, 0]
arr2 = [2, 3, 0, 0, 2, 0, 0]
arrList = [arr1, arr2, [1, 1, 0, 1], [2, 3, 0, 2, 0, 0, 0], [2, 3, 0, 2, 0, 1, 0], [2, 3, 3, 2, 2, 0, 0]]
for arr in arrList:
    print(canHop(arr))