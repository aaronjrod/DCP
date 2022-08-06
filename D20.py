# from collections import deque
# deque([{'data': 'a'}, {'data': 'b'}])
# llist = deque('abc')
# llist.append("f")
# llist.pop()

# llist.appendleft("z")
# llist.popleft()

# https://realpython.com/linked-lists-python/

class Node:
    visited = False

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes=None):
        self.length = 0
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.length += 1
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                self.length += 1
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
        self.length +=1 

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

# llist = LinkedList()
# llist.head = Node("a")
# llist.head.next = Node("b")
# llist.head.next.next = Node("c")

# node = llist.head
# while node is not None:
#     print(node.data)
#     node = node.next

# def dfsHelper(node):
#     if node is not None and not node.visited:
#         print(node.data)
#         node.visited = True
#         dfsHelper(node.next)

# def dfs(graph):
#     dfsHelper(graph.head)

def findIntersectionHelper(nodeA,nodeB):

    if nodeA.next is None:
        if nodeA.data == nodeB.data:
            return nodeA.data
        else:
            return None
    else:
        val = findIntersectionHelper(nodeA.next,nodeB.next)
        if nodeA.data == nodeB.data:
            return nodeA.data
        else:
            return val

def findIntersection(A,B):
    # Get length of each 
    lenA = A.length
    lenB = B.length
    
    nodeA = A.head
    nodeB = B.head
    if lenA > lenB:
        for i in range(0,lenA-lenB):
            nodeA = nodeA.next
    else:
        for i in range(0,lenB-lenA):
            nodeB = nodeB.next
    return findIntersectionHelper(nodeA,nodeB)

A = LinkedList([3,99,10,1,8,10])
B = LinkedList([99,1,8,10])

# for node in A:
#     print(node)
# dfs(A)

print(findIntersection(A,B))
