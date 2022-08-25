def dummy_division(a, b):
    count = 0
    sum = 0
    while sum < a:
        if count > 1 and a-sum > sum:
            sum += sum
            count += count
        else:
            count += 1
            sum += b
    if sum > a:
        return count - 1
    return count
# optimize by storing shit idk
for i in range(10):
    print(dummy_division(i, 2))
print(dummy_division(1000000, 2))