class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
        def __repr__(self):
            return self.data

class LinkedList:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root:
            prev_root = self.root
            self.root = Node(data)
            prev_root.prev = self.root
            self.root.next = prev_root  
        else:
            self.root = Node(data)

    def remove(self, data):
        if self.root is None:
            return False

        if self.root.data == data:
            if self.root.next:
                self.root = self.root.next
                self.root.prev = None
            else:
                self.root = None
            return True

        node = self.root
        while node:
            if node.data == data:
                if node.next:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    return True
                else:
                    node.prev.next = None
                    return True
            node = node.next
        return False

    def __repr__(self):
        node = self.root
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

list1 = LinkedList()
for i in range(7):
    list1.add(i)
print(list1)
for i in range(7):
    print(list1.remove(i))
print(list1.remove(0))
print(list1)