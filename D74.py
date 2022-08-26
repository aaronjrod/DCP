def num_apperances(N, X):
    count = 0
    for i in range(1, N+1):
        if X % i == 0 and i * N >= X:
            count += 1
    return count

arr = [12, 36]
for i in arr:
    print(num_apperances(6, i))