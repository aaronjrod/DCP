class Node:
    def __init__(self, val, children=[]) -> None:
        self.val = val
        self.children = children
    
    def __repr__(self) -> str:
        return self.val

def reverse_graph(node):
    queue = [(node, node)]
    closed_list = set()
    while queue:
        p_c = queue.pop(0)
        new_parent = p_c[1]
        prev_parent = p_c[0]
        
        if new_parent not in closed_list:
            for child in new_parent.children:
                queue.append((new_parent, child))
            new_parent.children = [prev_parent]
            closed_list.add(new_parent)
        else:
            new_parent.children.append(prev_parent)

def bfs(root):
    queue = [root]
    closed_list = {root}
    out = [root]
    while queue:
        node = queue.pop()
        for child in node.children:
            if child in closed_list:
                continue
            out.append(child)
            queue.append(child)
            closed_list.add(child)
    return out

d = Node('d')
c = Node('c', [d])
b = Node('b', [c, d])
a = Node('a', [b])
d.children = [a]
print(bfs(a))
reverse_graph(a)
print(bfs(d))

