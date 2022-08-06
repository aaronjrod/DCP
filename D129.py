from math import sqrt

n = 6
numIter = 100
print(sqrt(n))

def binarySearchSqrt(n, numIter):
    l = 0
    u = n
    v = n / 2
    c = numIter
    while c > 0:
        temp = v
        if v*v > n:
            temp = v
            v = (l + v)/2
            u = temp
        elif v*v < n:
            temp = v
            v = (u + v)/2
            l = temp
        else:
            return v
        c -= 1
    return v

print(binarySearchSqrt(n,numIter))