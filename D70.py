def nth_perf(num):
    rem = 10
    arr = []
    while num > 0:
        arr = [num%10] + arr
        rem -= num%10
        num //= 10
    
    i = 0
    while i < len(arr) and arr[i] < rem:
        i += 1
    arr = arr[:i] + [rem] + arr[i:]
    return arr

arr = [12, 25, 27, 10, 99, 999]
for i in arr:
    print(nth_perf(i))