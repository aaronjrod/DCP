
def find_num_intersect(p, q):
    n = len(p)
    count = 0
    for i in range(n):
        for j in range(i):
            if (q[i] < q[j] and p[j] < p[i]) or (q[i] > q[j] and p[j] > p[i]):
                count+= 1
    return count

p = [2, 5, 0, 1]
q = [3, 1, -4, -5]
print(find_num_intersect(p,q))