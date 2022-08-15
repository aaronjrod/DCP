class Stack():
    def __init__(self) -> None:
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def peek(self):
        if self.arr:
            arr_len = len(self.arr)
            return self.arr[arr_len-1]
        return None

    def pop(self):
        if self.arr:
            return self.arr.pop()
        return None

class Queue():
    def __init__(self) -> None:
        self.arr = []

    def enqueue(self, val):
        self.arr.append(val)

    def peek(self):
        if self.arr:
            return self.arr[0]
        return None

    def dequeue(self):
        if self.arr:
            return self.arr.pop(0)
        return None

arr = [1, 2, 3, 4]
stack = Stack()
for i in arr:
    stack.push(i)

def some_bs(stack, queue):
    len = 0

    val = stack.pop()    
    while val:
        len += 1
        queue.enqueue(val)
        val = stack.pop()

    div = len // 2

    while div > 0:
        stack.push(queue.dequeue())
        div -= 1

    for i in range(len):
        if i % 2:
            queue.enqueue(stack.pop())
        else:
            queue.enqueue(queue.dequeue())

    val = queue.dequeue() 
    while val:
        stack.push(val)
        val = queue.dequeue() 

queue = Queue()
some_bs(stack, queue)
print("hi")

    