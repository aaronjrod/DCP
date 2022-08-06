import random

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, data):
        if self.left is None:
            self.left = Node(data)
        elif self.right is None:
            self.right = Node(data)
        else:
            val = random.getrandbits(1)
            if val == 0:
                self.left.add(data)
            else:
                self.right.add(data)    

    def add_rand(self, data):
        val = random.getrandbits(1)
        if val == 0:
            child = self.left
        else:
            child = self.right
        if child:
            child.add_rand(data)
        else:
            child = Node(data)

def subtree_sum(root):
    my_dict = {}
    subtree_sum_helper(root, my_dict)
    return max(my_dict, key=my_dict.get)

def subtree_sum_helper(root, my_dict):
    if root is None:
        return 0
    value = root.data + subtree_sum_helper(root.left, my_dict) + subtree_sum_helper(root.right, my_dict)
    my_dict[value] = my_dict.get(value, 0) + 1
    return value

vals = [-5, 9]
root = Node(5)
for i in vals:
    root.add(i)

print(subtree_sum(root))