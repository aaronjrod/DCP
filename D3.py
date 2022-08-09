class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

def serialize(node):
    if not node:
        return '-1 '

    out = repr(node) + " "
    out += serialize(node.left)
    out += serialize(node.right)
    return out

def deserialize(string):
    node_list = string.split()
    return deserialize_helper(node_list)
        
def deserialize_helper(node_list):
    if not node_list:
        return None

    node_val = node_list.pop(0)
    if node_val == -1:
        return None
    return Node(node_val, deserialize_helper(node_list), deserialize_helper(node_list))

node = Node('root', Node('left', Node('left.left')), Node('right'))
out = serialize(node)
print(out)
print(deserialize(out).left.left)
assert deserialize(serialize(node)).left.left.val == 'left.left'