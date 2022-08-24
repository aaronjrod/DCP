def next_sparse(num):
    num = list('{0:b}'.format(num))
    str_len = len(num)
    for i in range(len(num)-2, 0, -1):
        if num[i] == '1' and num[i+1] == '1':
            # Set numbers after i to 0
            num[i:] = ['0']*(str_len-i)
            num[i-1] = '1'
            # Set i-1 to 1
            
    return num

#print(next_sparse(21))
print(next_sparse(22))