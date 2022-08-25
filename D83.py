class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.data)

def reverse_tree(node):
    if not node:
        return 
    reverse_tree(node.left)
    reverse_tree(node.right)
    node.left, node.right = node.right, node.left

root = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f')))

reverse_tree(root)
print()