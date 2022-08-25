class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.data)

def return_deepest(node):
    return return_deepest_helper(node, 0)[0]

def return_deepest_helper(node, d):
    if not node:
        return (node, 0)
    if not node.left and not node.right:
        return (node, d)
    d_L = return_deepest_helper(node.left, d+1)
    d_R = return_deepest_helper(node.right, d+1)
    if d_L[1] > d_R[1]:
        return d_L
    return d_R

root = Node('a', Node('b', Node('d')), Node('c'))
print(return_deepest(root))