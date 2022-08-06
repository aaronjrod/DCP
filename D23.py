class Node():
    def __init__(self, pos, goalPos, parent=None):
        self.parent = parent
        self.pos = pos
        if parent is None:
            self.g = 0
        else:
            self.g = parent.g+1
        self.h = max(abs(pos[0]-goalPos[0]),abs(pos[1]-goalPos[1]))
        self.f = self.g+self.h

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        return "("+str(self.pos[0])+", "+str(self.pos[1])+")"

def generateChildren(state, board, goalPos):
    pos = state.pos
    n = (pos[0]+1,pos[1])
    s = (pos[0]-1,pos[1])
    e = (pos[0],pos[1]+1)
    w = (pos[0],pos[1]-1)
    posList = [n,s,e,w]

    children = []
    for pos in posList:
        if pos[0] >= len(board) or pos[0] < 0 or pos[1] >= len(board[0]) or pos[1] < 0:
            continue 
        if board[pos[0]][pos[1]]:
            continue
        children.append(Node(pos, goalPos, state))

    return children

def sortByF(node):
    return node.f

def astar(board, start, end):
    iter = 0
    initialState = Node(start,end)
    openList = []
    openList.append(initialState)
    curPos = start
    while end != curPos:
        iter += 1
        S = openList.pop()
        children = generateChildren(S,board,end)
        for child in children:
            if child in openList:
                for openListItem in openList:
                    if openListItem is child: #Nice
                        if child.g < openListItem.g:
                            openListItem = child
                            continue
            openList.append(child)

        openList.sort(key=sortByF, reverse = True)
        board[S.pos[0]][S.pos[1]] = True
        curPos = S.pos
    print(iter)
    return S

f = False
t = True
board = [[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f], [f, f, f, f]]

start = (0,3)
end = (4,0)
S = astar(board, start, end)

while S.pos != start:
    print("("+str(S.pos[0])+", "+str(S.pos[1])+")")
    S = S.parent
