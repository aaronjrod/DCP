import random

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def add(self, val):
        if val < self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)
    
    def __repr__(self) -> str:
        return str(self.val)
    
def inorder(root):
    if root is None:
        return ""
    return inorder(root.left) + str(root) + " " + inorder(root.right)

# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
"""Generator function for iterative inorder tree traversal"""
def morris_traversal(root):
    current = root

    while current:
        if current.left is None:
            yield current.val
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            if pre.right is None:
                # Make current as right child of its inorder predecessor
                pre.right = current
                current = current.left
            else:
                # Revert the changes made to restore the original tree.
                # i.e., fix the right child of predecessor
                pre.right = None
                yield current.val
                current = current.right

root = Node(5)
for i in range(10):
    root.add(random.randint(0,10))

print(inorder(root))
for v in morris_traversal(root):
    print(v, end=' ')