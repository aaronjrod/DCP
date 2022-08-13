class Node():
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def rotate_linked_list(root, k):
    end_node = end = root
    
    while k - 1 > 0:
        end_node = root.next
        k -= 1
    while end.next:
        end = end.next
    
    end.next = root
    root = end_node.next
    end_node.next = None
    return root

root = Node(7,  Node(7,  Node(3,  Node(5, ))))
root = rotate_linked_list(root, 2)
print("hi")