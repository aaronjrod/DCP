class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
        def __repr__(self):
            return self.data
            
class Stack:
    def __init__(self):
        self.root = None
    
    def push(self, data):
        if self.root:
            temp = self.root
            self.root = Node(data)
            self.root.next = temp
        else:
            self.root = Node(data)
    
    def pop(self):
        if self.root is None:
            return False

        temp = self.root
        self.root = self.root.next
        return temp.data

    def peek(self):
        if self.root is None:
            return False

        return self.root.data
    
    def __repr__(self):
        node = self.root
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

stack1 = Stack()
for i in range(7):
    stack1.push(i)
print(stack1)
print(stack1.peek())
for i in range(7):
    print(stack1.pop())
print(stack1.pop())
print(stack1.peek())
print(stack1)