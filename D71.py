import random
def rand7():
    return random.randint(1, 7)

def rand5():
    while True:
        val = rand7()
        if val <= 5:
            return val
        
out = [0]*5
num = 100000
for i in range(num):
    out[rand5()-1] += 1
for i in range(len(out)):
    out[i] /= num
print(out)
