class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def __repr__(self):
            return self.data

class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root:
            prev_root = self.root
            self.root = Node(data)
            self.root.next = prev_root  
        else:
            self.root = Node(data)

    def swap(self, node1, node2):
        node1.data, node2.data = node2.data, node1.data

    def __repr__(self):
        node = self.root
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

arr_list = [[3,0,8,1,5]]
for arr in arr_list:
    l_list = LinkedList()
    for i in arr:
        l_list.add(i)
print(l_list)

def partition(l_list, k):
    i = l_list.root
    j = i.next
    while j:
        if j.data < k:
            l_list.swap(i, j)
            i = i.next
        j = j.next

partition(l_list, 3)

print(l_list)
