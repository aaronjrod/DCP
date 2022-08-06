
def power(set):
    powerSet = [[]]
    powerSet = powerSet + [set]

    if len(set) == 1 or len(set) == 0:
        return [set]

    for item in set:
        temp = set.copy()
        temp.remove(item)
        newSet = power(temp)
        for i in newSet:
            if not powerSet.__contains__(i):
                powerSet = powerSet + [i]

    return powerSet


set = [1, 2, 3]
print(power(set))
set = [1, 2, 3, 4]
print(power(set))