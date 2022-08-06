from contextlib import nullcontext


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        
    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = res + self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

root = Node(5)
list = [1,2,3,4,5,6,7,10,8,9]
for item in list:
    root.insert(item)

orderedList = root.inorderTraversal(root)
print(orderedList)
length = len(orderedList)
print(orderedList[length - 2])
