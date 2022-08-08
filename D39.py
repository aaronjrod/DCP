#https://stackoverflow.com/questions/15111285/explain-the-use-of-yields-in-this-game-of-life-implementation
import itertools

def generate_neighbors(point):
    x, y = point
    neighbors = set()
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (x,y) == (i,j):
                continue
            neighbors.add((i, j))
    return neighbors

def advance(board):    
    positions = board.copy()
    for point in board:
        positions = positions.union(generate_neighbors(point))

    next_state = set()
    for point in positions:
        neighbors = generate_neighbors(point)
        count = sum((neighbor in board) for neighbor in neighbors)

        if count == 3 or (count == 2 and point in board):
            next_state.add(point)
    return next_state

def board_to_string(glider):
    min_x = min(glider, key = lambda x: x[0])[0]
    min_y = min(glider, key = lambda x: x[1])[1]
    max_x = max(glider, key = lambda x: x[0])[0]
    max_y = max(glider, key = lambda x: x[1])[1]

    for i in range(min_x, max_x+1):
        str = ""
        for j in range(min_y, max_y+1):
            if (i, j) in glider:
                str += "*"
            else:
                str += "."
        print(str)

#glider = set([(0,0), (1,0), (2, 0), (0,1), (1,2)])
glider = set([(0,0), (2,1), (1,1), (-1,1), (1,0), (-1,0), (-3, 1), (3,2), (2, 3), (-3, 2), (-2, 0), (-2, 1), (-3, 1)])

print(glider)

for i in range(100):
    board_to_string(glider)
    glider = advance(glider)

    if len(glider) == 0:
        print("Died at " + str(i))
        break
    print()

