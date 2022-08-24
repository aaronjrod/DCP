def next_sparse(num):
    num = list('{0:b}'.format(num))
    str_len = len(num)

    for i in range(1, str_len-2):
        if num[i+1] != '1':
            i += 1
        elif num[i] == '1':
            num[i:] = ['0']*(str_len-i)
            num[i-1] = '1'
            break

    if str_len >= 2 and num[0] == '1' and num[1] == '1':
        num = ['1'] + ['0']*str_len

    out = ''.join(num)
    return int(out, 2)

arr = [6,4,38,44,21,22,23,0,1]
for i in arr:
    print(next_sparse(i))

#[8,4,40,64,21,32,32,0,1]