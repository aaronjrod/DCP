def permute(input, perm):
    arr = []
    for i in range(len(input)):
        arr.append(input[perm[i]])
    return arr

print(permute(["a","b","c"], [2,1,0]))