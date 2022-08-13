import random
def game_one(num_iter):
    outcomes = []
    for i in range(num_iter):
        prev = count = 0
        while True:
            val = random.randint(1,6)
            count += 1
            if prev == 5 and val == 6:
                break
            prev = val
        outcomes.append(count)
    return sum(outcomes)/len(outcomes)

def game_two(num_iter):
    outcomes = []
    for i in range(num_iter):
        prev = count = 0
        while True:
            val = random.randint(1,6)
            count += 1
            if prev == 5 and val == 5:
                break
            prev = val
        outcomes.append(count)
    return sum(outcomes)/len(outcomes)

print(game_one(10000))
print(game_two(10000))
