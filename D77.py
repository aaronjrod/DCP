def is_overlapping(interval_a, interval_b):
    return interval_a[1] >= interval_b[0] and interval_b[1] >= interval_a[0]

def merge_overlap(arr):
    open_list = []
    while arr:
        interval = arr.pop()
        repeat = False
        for i in range(len(open_list)):
            if is_overlapping(interval, open_list[i]):
                interval = (min(interval[0], open_list[i][0]), max(interval[1], open_list[i][1]))
                arr.append(interval)
                open_list.pop(i)
                repeat = True
                break
        if not repeat:
            open_list.append(interval)
    return open_list

print(merge_overlap([(1, 3), (5, 8), (4, 10), (20, 25)]))