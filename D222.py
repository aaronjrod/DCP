def shortest_standard(path):
    output_list = []
    i = 0
    j = 0
    while j < len(path):
        i = j
        while j < len(path) and path[j] != '/':
            j += 1

        if path[i:j] == '..':
            output_list.pop()
            continue
        elif path[i:j] == '.':
            continue
        
        output_list.append(path[i:j])
        j += 1

    output = "/"
    for x in output_list:
        if x:
            output += x + '/'
    return output

print(shortest_standard("/usr/bin/../bin/./scripts/../"))
