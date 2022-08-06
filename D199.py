class Node():
    def __init__(self, data, prev) -> None:
        self.data = data



def return_balanced(str):
    
    root = Node(str[0], None)
    prev = Node(str[1], root)
    for i in range(2, len(str)):
        node = Node(str[i], prev)

def build_tree(str, prev, i):
    if i >= len(str):
        return None
    
    if prev.data == '(' and str[i] == ')':
        prev.data = '()'
    elif str[i] == '(' and prev.data == ')':
        print("fuck")