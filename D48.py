class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data

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
    
    def preorder(self):
        if self.root:
            return self.root.data + self.preorderHelper(self.root.left) + self.preorderHelper(self.root.right)
        return ""
    
    def preorderHelper(self, parent):
        if parent:
            return str(parent.data) + self.preorderHelper(parent.left) + self.preorderHelper(parent.right)
        return ""

def reconstructPre(arr):
    root = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] < root.data:
            print()

def reconstructPreHelper(val):
    print()

pre = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
post = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
tree = BinaryTree()
for item in post:
    tree.insert(item)

print(tree.preorder())