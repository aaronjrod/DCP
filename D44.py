def inversionCounterPrototype(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def inversionCounter(arr):
    count = 0
    arr = arr.copy()
    
    for i in range(1,len(arr)):
        j = i-1
        while (j >= 0 and arr[i] < arr[j]):
            swap(arr, i, j)
            count += 1
            i -= 1
            j -= 1
    return count

def inversionCounter2(arr):
    count = 0
    arr = arr.copy()
    
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0 and key < arr[j]):
            if (key < arr[j]):
                count += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return count
    
arr1 = [2, 4, 1, 3, 5]
arr2 = [5,4,3,2,1]
print(inversionCounterPrototype(arr1))
print(inversionCounterPrototype(arr2))

print(inversionCounter(arr1))
print(inversionCounter(arr2))

print(inversionCounter2(arr1))
print(inversionCounter2(arr2))