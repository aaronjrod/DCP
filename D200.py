def min_stabs(interval_list):
    interval_list.sort(key=lambda x: x[1])
    stab_list = []
    while interval_list:
        stab = interval_list.pop(0)[1]
        stab_list.append(stab)

        list_copy = interval_list.copy()
        for interval in list_copy:
            if interval[0] <= stab and stab <= interval[1]:
                interval_list.remove(interval)
            
    return stab_list    

arr_list = [(1, 4), (4, 5), (7, 9), (9, 12)]

print(min_stabs(arr_list))