class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
        def __repr__(self):
            return self.data
            
class Queue:
    def __init__(self):
        self.root = None
        self.end = None

    def add(self, data):
        if self.root:
            temp = self.root
            self.root = Node(data)
            temp.prev = self.root
            self.root.next = temp
        else:
            self.root = Node(data)
            self.end = self.root
    
    def remove(self):
        if self.end is None:
            return False
        
        if self.end is self.root:
            temp = self.end
            self.root = None
            self.end = None
            return temp.data 

        temp = self.end
        self.end = self.end.prev
        self.end.next = None
        return temp.data

    def __repr__(self):
        node = self.root
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

queue1 = Queue()
for i in range(7):
    queue1.add(i)
print(queue1)
for i in range(7):
    print(queue1.remove())
print(queue1.remove())
print(queue1)
