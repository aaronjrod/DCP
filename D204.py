class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

def num_nodes(root):
    max_depth = 0
    node = root
    while node is not None:
        node = node.left
        max_depth += 1
    num_nodes = pow(2,max_depth-1)-1
    
    count = 0
    depth = 1
    node_stack = [[root,depth]]

    while node_stack:
        item = node_stack.pop()
        node = item[0]
        depth = item[1]

        if node is None:
            continue
        elif node.left is None and node.right is None:
            if depth < max_depth:
                break
            else:
                count += 1
        else:
            node_stack.append([node.right, depth+1])
            node_stack.append([node.left, depth+1])
    return num_nodes + count

root = Node(30)
arr = [17,37,11,19,31,38,10]
for i in arr:
    root.add(i)

print(num_nodes(root))

root = Node(30)
arr = [17,37,11,19,31,38,10,12]
for i in arr:
    root.add(i)

print(num_nodes(root))

root = Node(30)
arr = [17,37,11,19,31,38]
for i in arr:
    root.add(i)

print(num_nodes(root))

root = Node(30)
arr = []
for i in arr:
    root.add(i)

print(num_nodes(root))