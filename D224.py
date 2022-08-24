def find_lowest(arr):
    closed_set = set()
    closed_list = [0]
    count = 1
    for i in range(len(arr)):
        if i < len(arr)-1 and arr[i] == arr[i+1]:
            continue

        open_list = []
        for j in closed_list:
            val = arr[i] + j
            # Because arr is ordered, we know that items will be added to closed_set in an ordered way 
            if val > 0 and val not in closed_set:
                closed_set.add(val)
                open_list.append(val)
                if val == count:
                    count += 1
                else:
                    return count
        closed_list += open_list
    return closed_list.pop()+1

print(find_lowest([-1,1,1,2,3,10]))
print(find_lowest([1,2,3]))
print(find_lowest([]))