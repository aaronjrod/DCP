class Node():
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self):
        node = self
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

def reverse(root):
    node = root
    prev = None
    while node:
        prev_list = node.next
        node.next = prev
        prev = node
        node = prev_list
    root = prev
    return root

root_1 = Node(100)
for i in range(10, 0, -1):
    root_1, root_1.next = Node(i), root_1

print(root_1)
root_1 = reverse(root_1)
print(root_1)