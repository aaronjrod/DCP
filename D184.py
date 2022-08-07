def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def gcd_arr(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    cur_gcd = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        cur_gcd = gcd(cur_gcd, arr[i])
    return cur_gcd

arr_list = [[42, 56, 14], [48, 64], [], [3]]
for arr in arr_list:
    print(gcd_arr(arr))