from numpy import ones, zeros

def productArr(arr):
    prod = 1
    for i in range(len(arr)):
        prod *= arr[i]
    for i in range(len(arr)): 
        arr[i] = prod / arr[i]
    return arr

def productArr2(arr):
    out = ones(len(arr))

    for i in range(len(arr)):
        for j in range(len(arr)):
            if j != i:
                out[j] = out[j] * arr[i]
    return out

arrList = [[1, 2, 3, 4, 5], [3,2,1]]
for arr in arrList:
    print(productArr2(arr))