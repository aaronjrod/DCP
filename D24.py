class Node:
    def __init__(self, data, parent = None):
        self.left = None
        self.right = None
        self.data = data
        self.locked = False
        self.parent = parent

    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
            else:
                self.data = data
        
    def is_locked(self):
        return self.locked

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(str(self.data)),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def isLockableHelper(self, root):
        res = True
        if root:
            res = self.isLockableHelper(root.left)
            res = res and not self.locked
            res = res and self.isLockableHelper(root.right)
        return res
    
    def isLockable(self):
        return self.left.isLockableHelper(self.left) and self.right.isLockableHelper(self.right)

    def lock(self):
        if self.isLockable():
            self.locked = True
            return True
        return False
    
    def unlock(self):
        if self.isLockable():
            self.locked = False
            return True
        return False

root = Node(5)
list = [1,2,3,4,6,7,8,9]
for item in list:
    root.insert(item)
print(root.inorderTraversal(root))

print(root.is_locked())
print(root.isLockable())
root.lock()
print(root.isLockable())
print(root.is_locked())
root.unlock()
print(root.isLockable())
print(root.is_locked())
