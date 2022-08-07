class Node():
    def __init__(self, pos, goal_pos, parent=None):
        self.parent = parent
        self.pos = pos
        # g(self): # of steps taken
        if parent is None:
            self.g = 0
        else:
            self.g = parent.g + 1
        #h(self): Heuristic to get to goal
        self.h = max(abs(pos[0] - goal_pos[0]), abs(pos[1] - goal_pos[1]))
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        return "(" + str(self.pos[0]) + ", "+str(self.pos[1]) + ")"

    def __hash__(self):
        return hash(self.pos)

def generate_children(state, board, goalPos):
    pos = state.pos
    n = (pos[0]+1, pos[1])
    s = (pos[0]-1, pos[1])
    e = (pos[0], pos[1]+1)
    w = (pos[0], pos[1]-1)
    posList = [n, s, e, w]

    children = []
    for pos in posList:
        # If out, quit
        if pos[0] >= len(board) or pos[0] < 0 or pos[1] >= len(board[0]) or pos[1] < 0:
            continue 
        # If in closed list, quit
        if board[pos[0]][pos[1]]:
            continue
        children.append(Node(pos, goalPos, state))

    return children

# Iterative a_star algo
# Change to BFS by looking at g over f
def a_star(board, start, end):
    initial_state = Node(start,end)
    open_list = {initial_state : initial_state.f}
    cur_pos = start

    while end != cur_pos:
        S = min(open_list, key=open_list.get)
        open_list.pop(S)
        children = generate_children(S, board, end)

        # Add children to open list, update if possible
        for child in children:
            if child in open_list:
                if child.f < open_list[child]:
                    open_list.update(child)
            else:
                open_list[child] = child.f

        #Add S to closed list
        board[S.pos[0]][S.pos[1]] = True
        cur_pos = S.pos
    return S

f = False
t = True
board = [[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
for row in board:
    print(row)

start = (0,3)
end = (4,0)
S = a_star(board, start, end)

iter = 0
while S.pos != start:
    iter += 1
    print("("+str(S.pos[0])+", "+str(S.pos[1])+")")
    S = S.parent
print(start)
print(iter)