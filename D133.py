from bisect import insort


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.insertHelper(self.root, data)
        else:
            self.root = Node(data)
    
    def insertHelper(self, parent, data):
        if parent.data < data:
            if parent.right:
                self.insertHelper(parent.right, data)
            else:
                parent.right = Node(data)
        else:
            if parent.left:
                self.insertHelper(parent.left, data)
            else:
                parent.left = Node(data)
    
    def inorder(self):
        return self.inorderHelper(self.root)
    
    def inorderHelper(self, node):
        list = []
        if node:
            list.extend(self.inorderHelper(node.left))
            list.append(node.data)
            list.extend(self.inorderHelper(node.right))
        return list

arr = [10,5,30,22,35]
tree = BinaryTree()
for i in arr:
    tree.insert(i)

print(tree.inorder())

def nextBigger(tree, val):
    arr = tree.inorder()
    if val in arr:
        index = arr.index(val)
        if index < len(arr)-1:
            return arr[index+1]
    return -1

for i in arr:
    print(nextBigger(tree,i))
print(nextBigger(tree,4))
