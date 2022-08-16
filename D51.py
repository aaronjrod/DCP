import random
k=10

def rand_val(k):
    return random.randint(1, k)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def shuffle(arr):
    n = len(arr)
    for i in range(1, n):
        swap(arr, i, rand_val(n)-1)

for i in range(10):
    arr = [x for x in range(1, 6)]
    #print(arr)
    shuffle(arr)
    print(arr)