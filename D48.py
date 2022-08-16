class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data

def reconstruct(pre_ord, in_ord):
    if not pre_ord:
        return
    root = Node(pre_ord.pop(0))
    node = root
    stack = [node]
    while pre_ord:
        if stack[-1].data != in_ord[0]:
            node.left = Node(pre_ord.pop(0))
            node = node.left
        else:
            while stack and stack[-1].data == in_ord[0]:
                node = stack.pop()
                in_ord.pop(0)
            node.right = Node(pre_ord.pop(0))
            node = node.right
        stack.append(node)
    return root

def pre_order(node):
    if not node:
        return ""
    return node.data + pre_order(node.left) + pre_order(node.right) 

def in_order(node):
    if not node:
        return ""
    return in_order(node.left) + node.data + in_order(node.right) 

input_list = [(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']),
                (['a', 'b', 'd', 'c'], ['d', 'b', 'a', 'c'])]

for i in input_list:
    pre_order_val = ''.join(i[0])
    in_order_val = ''.join(i[1])
    root = reconstruct(i[0], i[1])
    print(pre_order(root) == pre_order_val)
    print(in_order(root) == in_order_val)
