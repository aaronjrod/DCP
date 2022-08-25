def get_children(map, point, unexplored):
    row = point[0]
    col = point[1]
    adjacents = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    children = []
    for point in adjacents:
        if point in unexplored:
            unexplored.remove(point)
            if map[point[0]][point[1]]:
                children.append(point)
    return children

def explorer(map):
    unexplored = set()
    count = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            unexplored.add((row, col))

    while unexplored:
        point = unexplored.pop()
        if map[point[0]][point[1]]:
            open_list = [point]
            count += 1
            while open_list:
                point = open_list.pop()
                open_list += get_children(map, point, unexplored)
    return count

map =  [[1, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0], 
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0], 
        [1, 1, 0, 0, 1], 
        [1, 1, 0, 0, 1]]
print(explorer(map))