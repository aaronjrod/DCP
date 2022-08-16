from turtle import left


class Node():
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
def in_order(node):
    if not node:
        return ""
    return '('+in_order(node.left) + str(node.val) + in_order(node.right)+')'

root = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))

print(eval(in_order(root)))