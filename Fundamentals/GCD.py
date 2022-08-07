# Python code to demonstrate naive
# method to compute gcd ( recursion )
def gcd_naive(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd_naive(b, a % b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

a = 48
b = 60

print (gcd(a, b))
print(gcd_naive(a, b))