class Node():
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return str(self.data)

def bottom_view(root):
    out_dict = dict()
    bottom_view_helper(root, 0, out_dict)
    return list(out_dict.values())

def bottom_view_helper(node, hd, out_dict):
    if not node:
        return
    bottom_view_helper(node.left, hd-1, out_dict)
    out_dict[hd] = node
    bottom_view_helper(node.right, hd+1, out_dict)

root = Node(5, Node(3, Node(1, Node(0)), Node(4)), Node(7, Node(6), Node(9, Node(8))))
print(bottom_view(root))
    
