# Python program to print DFS traversal for complete graph
class Node():
    def __init__(self, id, children = set()):
        self.id = id
        self.children = children
    
    def add_child(self, node):
        self.children.add(node)
    
    def __repr__(self) -> str:
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

def dfs(root):
    open_list = [root]
    closed_list = {}
    while open_list:
        node = open_list.pop(0)
        closed_list[node] = True
        print(node)

        for child in node.children:
            if child in closed_list or child in open_list:
                continue
            open_list = [child] + open_list

def bfs(root):
    open_list = [root]
    closed_list = {}
    while open_list:
        node = open_list.pop(0)
        closed_list[node] = True
        print(node)

        for child in node.children:
            if child in closed_list or child in open_list:
                continue
            open_list = open_list + [child]

node_list = [Node(x) for x in range(6)]
edge_list = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3), (3, 4)]
for edge in edge_list:
    parent = node_list[edge[0]]
    child = node_list[edge[1]]
    parent.add_child(child)
    
dfs(node_list[0])
print()
bfs(node_list[0])