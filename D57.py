def break_combine(string, k):
    arr = string.split()
    for i in arr:
        if len(i) > k:
            return None
    i = 0
    while i < len(arr)-1:
        str = arr[i]+" "+arr[i+1]
        if len(str) <= k:
            arr[i] = str
            arr.pop(i+1)
            continue
        i += 1
    return arr

print(break_combine("the quick brown fox jumps over the lazy dog 123456789", k = 10))
print(break_combine("the quick brown fox jumps over the lazy dog", k = 2))