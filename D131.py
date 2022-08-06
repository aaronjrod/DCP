import random


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.rand = None
    
    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.root = None
        self.length = 0
        self.rand = random

    def insert(self, data):
        temp = self.root
        self.root = Node(data)
        self.root.next = temp

        self.length += 1

        node = self.root
        randVal = self.rand.randrange(0,self.length)
        for i in range(randVal):
            node = node.next
        self.root.rand = node

    def deepClone(self):
        clone = LinkedList()
        node = self.root
        while node is not None:
            clone.insert(node.data)
            node = node.next     
        clone.reverse()
        return clone


    def reverse(self):
        node = self.root
        prev = None
        while node is not None:
            temp = node.next
            node.next = prev
            
            prev = node
            node = temp
        self.root = prev

    def __repr__(self) -> str:
        node = self.root
        string = ""
        while node is not None:
            string += repr(node) + ","
            node = node.next
        return string
    
    def randomPointers(self) -> str:
        node = self.root
        string = ""
        while node is not None:
            string += repr(node.rand) + ","
            node = node.next
        return string

arr = [2,5,36,42,57,32,1]
myList = LinkedList()
for i in arr:
    myList.insert(i)

#Use hash I guess

print(arr)
print(myList)
print(myList.randomPointers())
myList.reverse()
myList2 = myList.deepClone()
print(myList)
print(myList2)