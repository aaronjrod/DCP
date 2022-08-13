class Node():
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def add(self, val):  
        if self.val > val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)
            
    def __repr__(self) -> str:
        return str(self.val)

def reconstruct_post_order(arr):
    if not arr:
        return arr
    
    root = Node(arr.pop())
    while arr:
        root.add(arr.pop())
    return root

out = reconstruct_post_order([2, 4, 3, 8, 7, 5])


