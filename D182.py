# Python program to print DFS traversal for complete graph
class Node():
    def __init__(self, id, children):
        self.id = id
        self.children = children
    
    def add_child(self, node):
        self.children.append(node)
    
    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)
    
    def __repr__(self) -> str:
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

# Modified DFS
def is_minimally_connected(root):
    open_list = [root]
    closed_list = {}
    while open_list:
        node = open_list.pop(0)
        closed_list[node] = True

        for child in node.children:
            if child in closed_list or child in open_list:
                return False
            open_list = [child] + open_list
    return True

node_list = [Node(x, []) for x in range(6)]
edge_list = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3), (3, 4)]
for edge in edge_list:
    parent = node_list[edge[0]]
    child = node_list[edge[1]]
    parent.add_child(child)
print(is_minimally_connected(node_list[0]))

node_list = [Node(x, []) for x in range(6)]
edge_list = [(0, 1), (0, 2), (1, 3), (1, 4)]
for edge in edge_list:
    parent = node_list[edge[0]]
    child = node_list[edge[1]]
    parent.add_child(child)
print(is_minimally_connected(node_list[0]))
