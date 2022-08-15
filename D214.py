def get_num_bin(n):
    n = str(bin(n))
    count = 0
    max_count = 0
    for i in range(len(n)):
        if n[i] == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

print(get_num_bin(156))