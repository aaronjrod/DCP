class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return str(self.data)
    
def is_bst(node):
    if not node:
        return True
    if node.left and node.left.data > node.data:
        return False
    if node.right and node.right.data < node.data:
        return False
    return is_bst(node.left) and is_bst(node.right)

root = Node(5, Node(3, Node(1, Node(0)), Node(4)), Node(7, Node(6), Node(9, Node(8))))
print(is_bst(root))
root = Node(5, Node(3, Node(1, Node(2)), Node(4)), Node(7, Node(6), Node(9, Node(8))))
print(is_bst(root))

