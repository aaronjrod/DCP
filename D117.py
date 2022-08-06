from queue import Queue

from numpy import empty


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.addHelper(data, self.root)

    def addHelper(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.addHelper(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.addHelper(data, node.right)
   
    def levelOrder(self):
        queue = Queue()
        queue.put(self.root)
        list = []
        while not queue.empty():
            node = queue.get()
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            list.append(node.data)
        return list
         
tree = BinaryTree()
arr = [53,6,56,32,2,6,2,1,3,421,43]
for i in arr:
    tree.add(i)

print(tree.levelOrder())
print()