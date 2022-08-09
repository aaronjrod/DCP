class Node():
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

def num_unival(node):
    count = 0
    if not node:
        return 0
    if is_unival(node, node.val):
        count += 1
    count += num_unival(node.left)
    count += num_unival(node.right)
    return count

def is_unival(node, val):
    if not node or (node.val == val and is_unival(node.left, val) and is_unival(node.right, val)):
        return True
    return False

node = Node('0', Node('0', Node('0')), Node('1'))
print(num_unival(node))

node = Node('0', Node('1'), Node('0', Node('1',Node('1'),Node('1')), Node('0')))
print(num_unival(node))