class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
class LinkedList():

    def __init__(self):
        self.head = None
        self.len = 0
    
    def add(self, node):
        node.next = self.head
        self.head = node
        self.len += 1

    def remove(self, k):
        if k > self.len or k <= 0:
            return None
        
        self.len -= 1

        if k == 1:
            temp = self.head
            self.head = self.head.next
            return temp
        else:
            node = self.head
            for i in range(1,k-1):
                node = node.next
            temp = node.next
            node.next = node.next.next
            return temp      

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

llist = LinkedList()
llist.add(Node(1))
for i in range(1,10,2):
    llist.add(Node(i))

print(llist)
print(llist.remove(1))
print(llist.remove(5))
print(llist.remove(5))
print(llist)
print(llist.remove(2))
print(llist)

