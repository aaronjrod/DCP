import random

def random_blacklist(n, l):
    black_set = set(l)
    while True:
        rand_val = random.randint(0,n-1)
        if rand_val not in black_set:
            return rand_val

for i in range(5):
    #print(random_blacklist(4, [1,2,3]))
    print(random_blacklist(4, [1,2]))