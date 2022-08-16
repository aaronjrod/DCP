class Stack():
    def __init__(self) -> None:
        self.arr = []
    
    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

class Queue():
    def __init__(self) -> None:
        self.stack_a = Stack()
        self.stack_b = Stack()
    
    def enqueue(self, val):
        while self.stack_a.arr:
            self.stack_b.push(self.stack_a.pop())
        self.stack_b.push(val)
        while self.stack_b.arr:
            self.stack_a.push(self.stack_b.pop())

    def dequeue(self):
        return self.stack_a.pop()
        
queue = Queue()
for i in range(5):
    queue.enqueue(i*2)
for i in range(5):
    print(queue.dequeue())
