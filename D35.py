# Main
def segregateRGB(arr):
    charList = chars(arr)
    i = 0 # Index of last char in sequence

    for char in charList:
        j = i
        while (j < len(arr)):
            if char == arr[j]: # If same
                swap(arr, i, j)
                i += 1
            j += 1

# Get charecters,
def chars(arr):
    charList = []
    for i in arr:
        if i not in charList:
            charList.append(i)
    charList.sort(reverse=True)
    return charList

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

arr1 =  ['G', 'B', 'R', 'R', 'B', 'R', 'G']
arr2 =  ['R', 'R', 'R', 'G', 'G', 'B', 'B']
arr3 =  ['B', 'B', 'B', 'G', 'G', 'B', 'B']
arr4 =  ['B']
arr5 =  []

arrList = [arr1, arr2, arr3, arr4, arr5]
for arr in arrList:
    print(chars(arr))
    segregateRGB(arr)
    print(arr)


