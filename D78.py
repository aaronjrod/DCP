class Node():
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __lt__(self, node):
        return self.data < node.data

    def __repr__(self):
        node = self
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

def merge_linked_helper(l_1, l_2):
    merge_head = Node(-1)
    merge_tail = merge_head
    while l_1 and l_2:
        if l_1 < l_2:
            temp = l_1.next
            merge_tail.next = l_1
            l_1 = temp
            merge_tail = merge_tail.next
        else:
            temp = l_2.next
            merge_tail.next = l_2
            l_2 = temp
            merge_tail = merge_tail.next
    if l_1:
        merge_tail.next = l_1
    if l_2:
        merge_tail.next = l_2
    return merge_head.next

def merge_k(arr):
    while len(arr) > 1:
        i = 0
        while i < len(arr)-1:
            arr[i] = merge_linked_helper(arr[i], arr[i+1])
            arr.pop(i+1)
            i += 1
    return arr[0]

root_1 = Node(100)
root_2 = Node(100)
root_3 = Node(100)
root_4 = Node(100)

for i in range(10, 0, -1):
    root_1, root_1.next = Node(i), root_1
    root_2, root_2.next = Node(i*2), root_2
    root_3, root_3.next = Node(i*3), root_3
    root_4, root_4.next = Node(i*i), root_4

print(merge_k([root_1, root_2, root_3, root_4]))