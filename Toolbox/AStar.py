import heapq

class Heap:
    def __init__(self, data=None, key = lambda x:None) -> None:
        self.heap = data or []
        heapq.heapify(self.heap)
        self.key = key
    
    def heappush(self, item):
        if self.key:
            item = (self.key(item), item)
        heapq.heappush(self.heap, item)
    
    def heappop(self):
        return heapq.heappop(self.heap)[1]

class Node():
    def __init__(self, pos, goal_pos, parent=None):
        self.parent = parent
        self.pos = pos
        # g: Distance from start
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        # h: Heuristic distance to goal
        self.h = max(abs(pos[0] - goal_pos[0]), abs(pos[1] - goal_pos[1]))
        # f: Function to minimize
        self.f = self.g + self.h

    def update_parent(self, parent):
        self.parent = parent
        self.g = parent.g + 1
        self.f = self.g + self.h

    # def key(node):
    #     return node.f

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self):
        return "(" + str(self.pos[0]) + ", "+str(self.pos[1]) + ")"

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
        children.append(Node(pos, goalPos, state))

    return children

# Iterative a_star algo
def a_star(board, start, end):
    open_set = set()
    closed_set = set()
    open_heap = Heap()

    initial_state = Node(start, end)
    cur_pos = start

    open_set.add(initial_state)
    open_heap.heappush(initial_state)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                closed_set.add((i, j))

    while end != cur_pos:
        S = open_heap.heappop()
        open_set.remove(S)
        children = generate_children(S, board, end)

        # Add children to open list or update
        for child in children:
            if child.pos in closed_set:
                continue
            if child in open_set:
                for curr_child in open_set:
                    break
                if child < curr_child:
                    curr_child.update_parent(S)
            else:
                open_set.add(child)
                open_heap.heappush(child)

        #Add S to closed list
        closed_set.add(S.pos)
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

while S.pos != start:
    print("("+str(S.pos[0])+", "+str(S.pos[1])+")")
    S = S.parent
print(start)
