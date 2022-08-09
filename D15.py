import random

def random_select(val):
    random_select.count += 1
    if random.randrange(random_select.count) == 0:
        random_select.value = val
    return random_select.value

random_select.value = 0
random_select.count = 0
for i in range(10):
    print(random_select(i))