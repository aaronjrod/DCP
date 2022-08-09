# Counting
def counting_sort(arr, exp1):
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0 for i in range(len(arr))]
    # Initialize count array as 0
    count = [0 for i in range(10)]

    # Store count of occurrences in count[]
    for i in arr:
        index = i // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort
def radix_sort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10

def prepare_list(arr):
    temp_set = set(arr)
    remove_list = []
    for i in temp_set:
        if i <= 0 or i > len(arr):
            remove_list.append(i)
    for i in remove_list:
        temp_set.remove(i)
    return list(temp_set)

def find_missing(arr):
    arr = prepare_list(arr)
    radix_sort(arr)

    n = 1
    while n <= len(arr) and n == arr[n-1]:
        n += 1
    return n

arr_list = [[3, 4, -1, 1, 1], 
            [1,2,5, 0], 
            [1,2,3,4,5,6,6,6,3,21,4,23,7,3,9,7,8,10,11,12,5,14]]
for arr in arr_list:
    print(find_missing(arr))