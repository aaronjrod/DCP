# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
# implement a function rand7() that returns an integer from 1 to 7 (inclusive).

import random

def rand5():
    return 1+random.randrange(5)

def rand7():
    i = 22
    while i > 21:
        i = 5 * (rand5() - 1) + rand5()
        
    return i % 7 + 1

sum = 0
numIter = 100000
for i in range(numIter):
    sum += rand7()
print(sum/numIter)
