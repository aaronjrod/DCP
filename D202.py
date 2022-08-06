
from regex import A


def is_palindrome(num):
    i = 10
    if i > num:
        return True
    while num/i > 10:
        i *= 10
    
    a = int(num / i)
    b = num % 10

    if a==b:
        num = num - a*i
        num /= 10
        return is_palindrome(int(num))
    return False

list= [100, 121, 888, 678, 1, 0, 1001]
for i in list:
    print(is_palindrome(i))