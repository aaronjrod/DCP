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
        self.maxVal = None
        
    def push(self, data):
        if self.root:
            if (data > self.maxVal):
                temp = data
                data = 2*data-self.maxVal
                self.maxVal = temp

            temp = self.root
            self.root = Node(data)
            self.root.next = temp
        else:
            self.root = Node(data)
            self.maxVal = data
    
    def pop(self):
        if self.root is None:
            return False

        out = self.root
        self.root = self.root.next

        if out.data > self.maxVal:
            newVal = self.maxVal
            self.maxVal = 2*self.maxVal - out.data
            return newVal

        return out.data
    
    def peek(self):
        if self.root is None:
            return False

        if self.root.data > self.maxVal:
            return self.maxVal

        return self.root.data

    def max(self):
        return self.maxVal

    def __repr__(self):
        node = self.root
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

stack1 = Stack()
arr = [3,5,2,653,253,6,5,532,5,2,32,56,3,22]
for i in arr:
    stack1.push(i)

print(stack1)
print("Max: " + str(stack1.maxVal))
print(stack1.peek())
for i in range(len(arr)):
    print("Max: " + str(stack1.maxVal))
    print(stack1.pop())
print(stack1.pop())
print(stack1.peek())
print(stack1)