from heapq import merge


class Node():
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next
        self.len = 0
    
    def add(self, val):
        if self.next:
            self.next.add(val)
        else:
            self.next = Node(val)
        self.len += 1

    def __repr__(self) -> str:
        return str(self.val)

class LinkedList():
    def __init__(self, root = None) -> None:
        self.root = root
    
    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.root, self.root.next = Node(val), self.root

def merge_sort(l_list):
    return merge_sort_helper(l_list.root, 0, l_list.len)

def merge_sort_helper(node, i, j):
    if i >= j:
        return node
    div = (i+j) // 2




l_list = LinkedList()
arr = [4, 1,-3,99]
for i in arr[::-1]:
    l_list.add(i)
print("hi")