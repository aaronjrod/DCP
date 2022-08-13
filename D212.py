def alpha_encode(num):
    encoding = ""
 
    while num > 0:
        rem = num % 26
 
        if rem == 0:
            encoding += 'Z'
            num = num // 26 - 1
        else:
            encoding += chr((rem - 1) + ord('A'))
            num //= 26
 
    return encoding[::-1]

arr = [0, 26, 51, 52, 53, 80, 676, 702, 705]
for i in arr:
    print(alpha_encode(i))
 