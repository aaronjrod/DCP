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
    def __init__(self, val, goal_val, parent=None):
        self.parent = parent
        self.val = val
        # g: Distance from start
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        # h: Heuristic distance to goal
        self.h = max(abs(val[0] - goal_val[0]), abs(val[1] - goal_val[1]))
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
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return "(" + str(self.val[0]) + ", "+str(self.val[1]) + ")"

def generate_children(state, board, goalval):
    val = state.val
    n = (val[0]+1, val[1])
    s = (val[0]-1, val[1])
    e = (val[0], val[1]+1)
    w = (val[0], val[1]-1)
    valList = [n, s, e, w]

    children = []
    for val in valList:
        # If out, quit
        if val[0] >= len(board) or val[0] < 0 or val[1] >= len(board[0]) or val[1] < 0:
            continue 
        children.append(Node(val, goalval, state))

    return children

# Iterative a_star algo
def a_star(world, start, end):
    open_set = set()
    closed_set = set()
    open_heap = Heap()

    initial_state = Node(start, end)
    cur_val = start

    open_set.add(initial_state)
    open_heap.heappush(initial_state)
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j]:
                closed_set.add((i, j))

    while end != cur_val:
        S = open_heap.heappop()
        open_set.remove(S)
        children = generate_children(S, world, end)

        # Add children to open list or update
        for child in children:
            if child.val in closed_set:
                continue
            if child in open_set:
                for curr_child in open_set:
                    break
                if child < curr_child:
                    curr_child.update_parent(S)
            else:
                open_set.add(child)
                open_heap.heappush(child)

        # Add S to closed list
        closed_set.add(S.val)
        cur_val = S.val
    return S

f = False
t = True
board = [[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
for row in board:
    print(row)

start = (0,3)
end = (4,0)
S = a_star(board, start, end)

while S.val != start:
    print(S)
    S = S.parent
print(start)
